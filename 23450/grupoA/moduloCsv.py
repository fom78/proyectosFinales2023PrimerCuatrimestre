
import os
import json
import csv
import time
carpeta = os.path.dirname(__file__)
os.chdir(carpeta)

# Cargar datos desde el archivo JSON
with open("stocks.json", "r") as archivoJson:
    datosJson = json.load(archivoJson)

# Exportar los datos como un archivo CSV
with open("stocks.csv", "w", newline="") as archivoCsv:
    escritorCsv = csv.writer(archivoCsv)
    
    # Escribir encabezados en el archivo CSV
    encabezados = ["Codigo", "Producto", "Categoria", "Precio", "Cantidad", "Nacional"]
    escritorCsv.writerow(encabezados)
    
    # Escribir cada fila de datos en el archivo CSV
    for producto in datosJson:
        codigo = producto["codigo"]
        nombre = producto["producto"]
        categoria = producto["categoria"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        nacional = producto["nacional"]
        
        fila = [codigo, nombre, categoria, precio, cantidad, nacional]
        escritorCsv.writerow(fila)

print("Los datos se han exportado correctamente como archivo CSV.")
time.sleep(2)

							