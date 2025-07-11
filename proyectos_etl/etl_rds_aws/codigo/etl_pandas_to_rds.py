import pandas as pd
import pandas as pd
from sqlalchemy import create_engine,text
from unidecode import unidecode
from glob import glob
import sys

#Credenciales de ACCESO
DB_USER = "postgres"
DB_PASS = "####"
DB_HOST = "####"
DB_PORT = "5432"
DB_NAME = "postgres"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require")


#PRIMERO EXTRAEMOS LA DATA

try:
    archivos = glob('../data/ventas_2024_*.csv')
    if not archivos:
        raise FileExistsError('No se encontraron los archivos necesarios')
    
    df = pd.concat([pd.read_csv(f) for f in archivos], ignore_index=True)
    print('Archivos cargados')

except Exception as e:
    print (f'Error al extraer: {e}')

# TRANSFORMAMOS LA DATA

try:
    def limpiar_texto(texto):
        if pd.isnull(texto):
            return texto
        texto = str(texto).strip().lower()
        texto = unidecode(texto)
        return texto
    
    columnas_t = ["producto", "categoria", "metodo_pago", "ciudad", "vendedor"]
    for col in columnas_t:
        df[col] = df[col].apply(limpiar_texto)
    
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df = df.dropna(subset=["cliente_id", "producto", "fecha"])
    df["monto_total"] = df["monto"] * (1 - df["descuento_aplicado"])
    df["monto_total"] = df["monto_total"].round(2)
    df["reembolsado"] = df["reembolsado"].astype(bool)
    df = df.drop_duplicates()

    print(f"LIMPIEZA Y TRANSFORMACION completada.")

except Exception as e:
    print(f" Error en la transformacion: {e}")
    sys.exit(1)


# CARGA A LA BD EN AWS
'''
try:
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    )

    df.to_sql("ventas_resumen", engine, if_exists="replace", index=False)
    print(f"✅ Datos cargados correctamente a 'ventas_resumen'.")
except Exception as e:
    print(f"❌ Error en LOAD: {e}")
    sys.exit(1)
'''
#comprobamos
try:
    sql = """
    SELECT 
        categoria,
        metodo_pago,
        COUNT(*) AS total_ventas,
        ROUND(AVG(monto_total)::numeric, 2) AS promedio_monto_total,
        SUM(monto_total) AS suma_total
    FROM ventas_resumen
    GROUP BY categoria, metodo_pago
    ORDER BY suma_total DESC
    LIMIT 10;
    """
    df_check = pd.read_sql(sql, engine)
    print(df_check)
except Exception as e:
    print("Error al verificar datos:", e)
