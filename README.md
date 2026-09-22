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


---

analizador_interactivo/reporte/

## 📁 Estructura del proyecto

analizador_csv/
── data/
── reporte/
   ── reporte.txt
   ── grafico_histograma.png
   ── grafico_linea.png
   ── manual_histograma.png
   ── manual_linea.png
   ── manual_barras.png
   ── manual_dispersion.png
   ── datos_convertidos.csv
── src/
   ── analizador_interactivo.py
── README.md


---

## 🧠 Tecnologías utilizadas

- **Python 3**
- **pandas**
- **matplotlib**
- **tkinter** (para selección de archivo)
- **pathlib** (manejo de rutas)
- **json** (lectura y conversión de JSON)

---

## ▶ Cómo ejecutar el proyecto

1. Instala las dependencias:
pip install pandas matplotlib


2. Ejecuta el script:
python src/analizador_interactivo.py


3. Selecciona el archivo CSV o JSON desde la ventana emergente.

4. Elige el modo de gráficos:
- Automático  
- Manual  

5. Revisa los resultados en la carpeta:
analizador_csv/reporte/


---

## 📊 Ejemplo de uso

- Seleccionas un archivo `ventas.csv`
- El programa limpia los datos
- Genera estadísticas descriptivas
- Crea gráficos automáticos o manuales
- Guarda todo en la carpeta `reporte`

---

## 🎯 Objetivo del proyecto

Este proyecto demuestra habilidades prácticas en:

- Manipulación de datos  
- Limpieza y análisis con pandas  
- Visualización con matplotlib  
- Interacción con el usuario  
- Conversión de formatos (JSON → CSV)  
- Organización profesional de proyectos  

Ideal para roles **junior de análisis de datos**, **Python scripting**, o **automatización básica**.

---

## 📬 Autor

**carret**  
Python Developer & Data Enthusiast



