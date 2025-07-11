# Automatización de Procesos Operativos – Entel Perú

Este proyecto fue desarrollado durante mi etapa como practicante preprofesional en Gestión de Calidad en Entel Perú S.A., con el objetivo de automatizar flujos manuales relacionados a la validación de datos, integración de fuentes y generación de reportes críticos.

## Contexto

En el área de Gestión de Calidad, varios procesos clave se realizaban de forma manual, consumiendo varias horas por semana del equipo. Estos procesos incluían:

- La extracción y consolidación de archivos desde SharePoint.
- La limpieza y validación de datos financieros, biométricos y de reclamos.
- La generación de reportes para áreas como Riesgos, Seguridad y Gestión de la Información.

## Objetivo

Reducir el tiempo y riesgo operativo mediante la automatización de tareas repetitivas en Python, integradas con herramientas como SharePoint, Power BI y Power Automate.

## 🔧 Solución Implementada

- Desarrollé más de 10 scripts ETL en Python utilizando `pandas`, `numpy` y `sqlalchemy` para limpieza, transformación y carga de datos desde OracleDB.
- Implementé flujos automáticos con **Power Automate** para mover y filtrar archivos entre **SharePoint** y **OneDrive**.
- Sincronización automatizada de reportes con **Power BI**, mejorando la visualización de procesos como:
  - Activaciones biométricas
  - Reclamos de proveedores
  - Ventas al contado y financiadas
- Automatización de reportes analíticos usados para detección de fraude, con envíos programados al área de Seguridad.

## 📈 Impacto

- Reducción del tiempo de procesamiento de datos de hasta 3 horas a menos de 1 hora.
- Reportes críticos disponibles en tiempo real para áreas de decisión.
- Eliminación del 100% de tareas manuales en la consolidación de archivos operativos semanales.

## 🛠 Tecnologías y Herramientas

- Python (`pandas`, `sqlalchemy`, `openpyxl`)
- OracleDB
- SharePoint + Power Automate
- Power BI (DAX, Power Query)
- GitHub (versionado y documentación)

## 🔐 Nota

Por confidencialidad, el código completo no está publicado. Se presentan ejemplos genéricos y estructuras de flujo representativas para fines demostrativos.
