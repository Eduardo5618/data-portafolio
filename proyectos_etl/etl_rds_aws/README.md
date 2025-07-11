# Proyecto ETL – Carga de Ventas a AWS RDS

Este proyecto muestra un flujo ETL profesional usando Python y Pandas para cargar datos de ventas desde archivos CSV a una base de datos PostgreSQL alojada en AWS RDS.

## 📁 Estructura

etl_rds_aws/
├── data/
│ ├── ventas_2024_01.csv
│ └── ventas_2024_02.csv
├── schema/
│ └── schema.sql
├── source/
│ └── etl_pandas_to_rds.py
├── output/
│ └── resumen_cargado.xlsx (opcional)
└── requirements.txt

markdown
Copiar
Editar

## 🔧 Requisitos

- Python 3.8+
- Instancia de PostgreSQL en AWS RDS
- Acceso abierto en las reglas de entrada (IP autorizada)

Instalación de librerías:

```bash
pip install -r requirements.txt