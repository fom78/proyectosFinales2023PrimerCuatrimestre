import json
import os
import time

carpeta = os.path.dirname(__file__)
os.chdir(carpeta)


def tabla():#funcion tabla
	print("+--------+----------------+-------------------+--------+----------+----------+")
	print("| Codigo |    Producto    |     Categoria     | Precio | Cantidad | Nacional |")
	print("+--------+----------------+-------------------+--------+----------+----------+")

def mostrarProductos(stocks):#funcion para mostrar todos los productos
	if not stocks:  # Verifica si el stock está vacío
		print("El stock está vacío")
		time.sleep(2)
	else:
		tabla()
		for i in stocks:
			# Imprimir los detalles del producto
			codigo = i["codigo"]
			producto = i["producto"]
			categoria = i["categoria"]
			precio = i["precio"]
			cantidad = i["cantidad"]
			nacional = i["nacional"]
			print(f"| {codigo:<7}|{producto:^16}| {categoria:^18}|{precio:^8}|{cantidad:^10}|{nacional:^10}|")
			print("+--------+----------------+-------------------+--------+----------+----------+")
		continuar2 = input("¿Continuar? Presione enter: ")

def mostrarProductosNacionales(stocks):#funcion para mostrar productos nacionales 
	os.system('cls')
	print("Productos Nacionales")
	if not stocks:  #si no detecta nada cargado al stock entra aca
		print("No hay productos nacionales")
		time.sleep(2)
	else:# aca entra en caso de encontrar valores en el stock
		for producto in stocks:
			if producto["nacional"]:# aca imprime los nacionales en caso de ser True
				print(f"codigo: {producto['codigo']}")
				print(f"producto: {producto['producto']}")
				print(f"categoria: {producto['categoria']}")
				print(f"precio: {producto['precio']}")
				print(f"cantidad: {producto['cantidad']}")
				print("-----------------------------")
		continuar2 = input("¿Continuar? Presione enter: ")

def mostrarProductosImportados(stocks):# funcion para mostrar productos importados
	os.system('cls')
	print("Productos Importados")
	if not stocks: #si no detecta nada cargado al stock entra aca 
		print("No hay productos importados")
		time.sleep(2)
	else:# aca entra en caso de encontrar valores en el stock
		for producto in stocks:
			if not producto["nacional"]:# aca imprime los nacionales en caso de ser False
				print(f"codigo: {producto['codigo']}")
				print(f"producto: {producto['producto']}")
				print(f"categoria: {producto['categoria']}")
				print(f"precio: {producto['precio']}")
				print(f"cantidad: {producto['cantidad']}")
				print("-----------------------------")
		continuar2 = input("¿Continuar? Presione enter: ")

def mostrarProductosCantidad(stocks):# funcion para mostrar productos por cantidad
	os.system('cls')
	print("Productos Ordenados por Cantidad")
	medida=input("¿Desea que la busqueda sea por mayor o menor?: ")
	medida=medida.lower()
	if medida == "mayor":# aca controla que se haya elegido mayor en la opcion sea mayor
		cantidad = float(input("Ingrese una cantidad: "))
		productosConCantidad = False
		for producto in stocks:#aca se itera el stock 
			if producto["cantidad"] > cantidad:# de ser mayor entra por aca
				productosConCantidad = True
				print(f"Codigo: {producto['codigo']}")
				print(f"Producto: {producto['producto']}")
				print(f"Categoria: {producto['categoria']}")
				print(f"Precio: {producto['precio']}")
				print(f"Cantidad: {producto['cantidad']}")
				print("-----------------------------")
			
		if not productosConCantidad:# en caso de no encontrar de la cantidad ingresada entra aca
			productosConCantidad = False
			print("No hay productos con cantidad mayor a la ingresada")
		continuar2 = input("¿Continuar? Presione enter: ")
	elif medida=="menor":# aca entra en caso de ingresar menor
		cantidad = float(input("Ingrese una cantidad: "))
		productosConCantidad = False
		for producto in stocks:
			if producto["cantidad"] < cantidad:#de ser menor entra por aca
				productosConCantidad = True
				print(f"Codigo: {producto['codigo']}")
				print(f"Producto: {producto['producto']}")
				print(f"Categoria: {producto['categoria']}")
				print(f"Precio: {producto['precio']}")
				print(f"Cantidad: {producto['cantidad']}")
				print("-----------------------------")
			
		if not productosConCantidad:#en caso de no encontrar de la cantidad ingresada entra aca
			productosConCantidad = False
			print("No hay productos con cantidad mayor a la ingresada")
		continuar2 = input("¿Continuar? Presione enter: ")
	else:
		print("Debe ingresar mayor o menor")
		time.sleep(2)
		
def mostrarProductosCategoria(stocks):# funcion para separar los productos por categoria
	os.system('cls')
	categorias = set(producto["categoria"] for producto in stocks)
	print("Categorias Disponibles")
	for categoria in categorias:
		print(categoria)# aca si itera y se imprime la categorias agregadas al sistema
	print("----------------------------------")
	categoriaElegida = input("Ingrese el nombre de la categoria: ")
	os.system('cls')
	print(f"Productos en la Categoria '{categoriaElegida}'")
	for producto in stocks:# aca se itera el stock
		if producto["categoria"] == categoriaElegida:#aca si la categoria elegida coincide se imprimen los valores
			print(f"codigo: {producto['codigo']}")
			print(f"producto: {producto['producto']}")
			print(f"precio: {producto['precio']}")
			print(f"cantidad: {producto['cantidad']}")
			print("-----------------------------")
	continuar2 = input("¿Continuar? Presione enter: ")

