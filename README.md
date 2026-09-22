# Analizador Interactivo de CSV y JSON con Python

Este proyecto es una herramienta interactiva para análisis de datos en formato **CSV** o **JSON**, desarrollada con **Python**, **pandas** y **matplotlib**.  
Permite seleccionar archivos mediante una ventana gráfica, convertir JSON a CSV automáticamente, generar reportes estadísticos y crear gráficos de forma automática o manual.

---

## 🚀 Funcionalidades principales

### ✔ Selección de archivo mediante ventana
El usuario elige el archivo desde el explorador de archivos, sin necesidad de escribir rutas manualmente.

### ✔ Conversión automática de JSON → CSV
Si el archivo seleccionado es JSON, se convierte automáticamente a CSV para su análisis.

### ✔ Limpieza básica de datos
Se eliminan filas con valores nulos para evitar errores en el análisis.

### ✔ Generación de reporte estadístico
Se crea un archivo `reporte.txt` con estadísticas descriptivas del dataset.

### ✔ Dos modos de gráficos
- **Automático:** genera histograma y gráfico de línea (si existe columna `fecha`).
- **Manual:** permite elegir entre:
  - Histograma  
  - Línea  
  - Barras  
  - Dispersión  

### ✔ Carpeta dedicada para resultados
Todos los archivos generados (reporte, gráficos y CSV convertido) se guardan en:

