import pandas as pd
import matplotlib.pyplot as plt
import os
import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pathlib import Path

# === Crear carpeta interna "reporte" dentro del proyecto ===
ruta_base = Path(__file__).resolve().parent.parent  # carpeta analizador_csv
ruta_reporte = ruta_base / "reporte"
os.makedirs(ruta_reporte, exist_ok=True)

def seleccionar_archivo():
    print("Abriendo ventana para seleccionar archivo...")

    Tk().withdraw()

    ruta = askopenfilename(
        title="Selecciona un archivo CSV o JSON",
        filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json"), ("All files", "*.*")]
    )

    if not ruta:
        print("No seleccionaste ningún archivo. Saliendo...")
        exit()

    print(f"Archivo seleccionado: {ruta}")
    return ruta

def convertir_json_a_csv(ruta_json):
    with open(ruta_json, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    ruta_csv = ruta_reporte / "datos_convertidos.csv"
    df.to_csv(ruta_csv, index=False)
    print(f"JSON convertido a CSV: {ruta_csv}")
    return ruta_csv

def cargar_datos():
    ruta = seleccionar_archivo()

    if ruta.lower().endswith(".json"):
        ruta = convertir_json_a_csv(ruta)

    elif not ruta.lower().endswith(".csv"):
        print("Formato no soportado. Solo CSV o JSON.")
        exit()

    df = pd.read_csv(ruta)
    print("\nPrimeras filas del dataset:")
    print(df.head())

    df = df.dropna()
    return df

def generar_reporte(df):
    stats = df.describe()

    ruta_archivo = ruta_reporte / "reporte.txt"
    with open(ruta_archivo, "w") as f:
        f.write("REPORTE DE ANALISIS\n\n")
        f.write(str(stats))

    print(f"\nReporte generado en: {ruta_archivo}")

def grafico_automatico(df):
    col_num = df.select_dtypes(include="number").columns[0]

    # Histograma
    plt.figure(figsize=(8,5))
    plt.hist(df[col_num], bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Histograma de {col_num}")
    plt.savefig(ruta_reporte / "grafico_histograma.png")
    plt.close()

    # Línea si existe fecha
    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"])
        df = df.sort_values("fecha")

        plt.figure(figsize=(10,5))
        plt.plot(df["fecha"], df[col_num], color="green")
        plt.title(f"Evolución de {col_num} en el tiempo")
        plt.savefig(ruta_reporte / "grafico_linea.png")
        plt.close()

    print("Gráficos automáticos generados en carpeta 'reporte'.")

def grafico_manual(df):
    print("\n=== Tipos de gráfico disponibles ===")
    print("1. Histograma")
    print("2. Línea")
    print("3. Barras")
    print("4. Dispersión")

    opcion = input("Selecciona el tipo de gráfico (1-4): ").strip()

    col_num = df.select_dtypes(include="number").columns[0]

    if opcion == "1":
        plt.hist(df[col_num], bins=20, color="orange")
        plt.title(f"Histograma de {col_num}")
        plt.savefig(ruta_reporte / "manual_histograma.png")

    elif opcion == "2":
        if "fecha" not in df.columns:
            print("No existe columna 'fecha'. No se puede generar gráfico de línea.")
            return
        df["fecha"] = pd.to_datetime(df["fecha"])
        df = df.sort_values("fecha")
        plt.plot(df["fecha"], df[col_num], color="blue")
        plt.title(f"Línea de {col_num}")
        plt.savefig(ruta_reporte / "manual_linea.png")

    elif opcion == "3":
        plt.bar(range(len(df[col_num])), df[col_num], color="purple")
        plt.title(f"Gráfico de barras de {col_num}")
        plt.savefig(ruta_reporte / "manual_barras.png")

    elif opcion == "4":
        if len(df.select_dtypes(include="number").columns) < 2:
            print("Se necesitan dos columnas numéricas para dispersión.")
            return
        col2 = df.select_dtypes(include="number").columns[1]
        plt.scatter(df[col_num], df[col2], color="red")
        plt.title(f"Dispersión: {col_num} vs {col2}")
        plt.savefig(ruta_reporte / "manual_dispersion.png")

    else:
        print("Opción inválida.")
        return

    plt.close()
    print("Gráfico manual generado en carpeta 'reporte'.")

def main():
    df = cargar_datos()
    generar_reporte(df)

    print("\n=== Selección de modo de gráficos ===")
    print("1. Automático")
    print("2. Manual")

    modo = input("Selecciona el modo (1-2): ").strip()

    if modo == "1":
        grafico_automatico(df)
    elif modo == "2":
        grafico_manual(df)
    else:
        print("Modo inválido.")

    print(f"\nAnálisis completado. Archivos guardados en:\n{ruta_reporte}")

if __name__ == "__main__":
    main()
