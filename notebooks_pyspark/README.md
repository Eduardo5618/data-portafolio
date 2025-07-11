# Notebooks de Práctica con PySpark

Este módulo forma parte de mi portafolio de datos y contiene notebooks prácticos desarrollados con PySpark, enfocados en tareas comunes de ingeniería de datos: lectura de archivos, limpieza, joins, agregaciones y manipulación de fechas a gran escala.

Los ejemplos están pensados para correr en modo local y utilizar datasets ficticios que simulan escenarios reales en entornos de negocio.

---

## 📘 Temario

| Notebook                           | Descripción                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| `01_spark_basico.ipynb`            | Configuración de Spark, lectura de CSVs, filtros y transformaciones simples |
| `02_transformaciones_avanzadas.ipynb` | `withColumn`, `when`, limpieza de strings, renombrar y conversión de tipos |
| `03_joins_y_ventanas.ipynb`        | Joins (`inner`, `left`), `row_number()`, `lag()`, `lead()`, `partitionBy`  |
| `04_aggregations_pivot_fechas.ipynb`| `groupBy`, agregaciones, `pivot()`, manejo y truncado de fechas            |

---

## 🧰 Tecnologías usadas

- Apache Spark 3.x
- PySpark
- Python 3.9+
- Jupyter Notebooks

> 💡 Todos los notebooks están comentados y pueden ejecutarse en local usando datasets de prueba incluidos en la carpeta `datasets/`.
