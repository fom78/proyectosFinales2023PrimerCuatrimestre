import os
import time
import json

carpeta = os.path.dirname(__file__)
os.chdir(carpeta)

def productoNuevo(stocks):
	while True:
			# Solicitar los detalles del nuevo producto
		codigo = input("Ingrese el código del producto: ")
		codigo=codigo.upper()
		# Validar si el código ya existe en el stock
	
		for producto in stocks:
			if producto["codigo"] == codigo:
				print("¡Error! El código del producto ya existe.")
				time.sleep(2)
				break
		else:
			if len(codigo) == 5 and codigo[0].isalpha() and codigo[1:].isdigit():
				producto = input("Ingrese nombre del producto: ")
				categoria = input("Categoría del producto: ")

			# Validar el precio como número decimal
				while True:
					try:
						precio = float(input("Ingrese el precio: "))
						break
					except ValueError:
						print("Error: El precio debe ser un número decimal. Intente nuevamente.")

			# Validar la cantidad como número decimal
				while True:
					try:
						cantidad = float(input("Ingrese la cantidad: "))
						break
					except ValueError:
						print("Error: La cantidad debe ser un número decimal. Intente nuevamente.")

				
				while True:
					nacional = input("¿Es el producto nacional? (s/n): ")
					if nacional.lower() == "s":#aca valida si es nacional o no
						nacional = True
						break
					elif nacional.lower() == "n":
						nacional = False
						break
										
					else:
						print("Opcion invalida debe ser s o n")
				stock = {
					"codigo": codigo,
					"producto": producto,
					"categoria": categoria,
					"precio": precio,
					"cantidad": cantidad,
					"nacional": nacional
					}#aca se crea el diccionario con los valores cargados
				stocks.append(stock)
				archivo = open("stocks.json", "w")
				json.dump(stocks, archivo, indent=2)
				archivo.close()
				print("Producto agregado con éxito")
				time.sleep(2)
				continuar = input("Desea agregar otro artículo? (s/n): ")
				if continuar.lower() == "s":
					True
				elif continuar.lower() == "n":
					break
				else:
					os.system('cls')
					print("Opción inválida")
					time.sleep(2)
			else:
				os.system('cls')
				print("Código inválido")
				time.sleep(2)


def modificar(stocks):
	codigoBuscar = input("Ingrese el codigo a buscar: ")
	codigoBuscar=codigoBuscar.upper()
	if len(codigoBuscar) == 5 and codigoBuscar[0].isalpha() and codigoBuscar[1:].isdigit():#aca se controla que el codigo contenga 5 digitos 
		for productos in stocks:#aca se itera el stock
			if codigoBuscar == productos["codigo"]:
				print("Ingrese el dato o enter para continuar (excepto en el precio y cantidad)")
				codigo = input(f"Codigo actual({productos['codigo']}): ")
				if codigo == "":#en caso de apretar enter conserva valor
					codigo=productos["codigo"]
				producto = input(f"Producto actual({productos['producto']}): ")
				if producto == "":#en caso de apretar enter conserva valor
					producto=productos["producto"]
				categoria = input(f"Categoria actual({productos['categoria']}): ")
				if categoria == "":#en caso de apretar enter conserva valor
					categoria =productos["categoria"]
				while True:
					try:#aca se controla que si o si se agregue un valor en numeros
						precio = float(input(f"Precio actual({productos['precio']}): "))
						precio=productos["precio"]
						break
					except:
						print("Tiene que ingresar un número (el actual o uno nuevo) !!!!")
				
				while True:
					try:
						cantidad = float(input(f"Cantidad actual({productos['cantidad']}): "))
						cantidad=productos["cantidad"]
						break
					except:
						print("Tiene que ingresar un número (el actual o uno nuevo)!!!!")
				
				nacional = input(f"Nacional actual({productos['nacional']}): ")
				if nacional == "":#en caso de apretar enter conserva valor
					nacional=productos["nacional"]

				productos["codigo"]=codigo.upper()
				productos["producto"]=producto
				productos["categoria"]=categoria
				productos["precio"]=precio
				productos["cantidad"]=cantidad
				productos["nacional"]=nacional
				#arriba se agregan los valores modificados al diccionario
				archivo = open("stocks.json", "w")
				json.dump(stocks, archivo, indent=2)
				archivo.close()
				print("Articulo modificado con exito")
				time.sleep(2)
				break

		else:
			print("Codigo inexsistente")
			time.sleep(2)
	else:
		print("Código incorrecto")
		time.sleep(2)


def eliminar(stocks):
	codigo = input("Ingrese el codigo del producto a eliminar: ")
	codigo=codigo.upper()
	for producto in stocks:#aca se itera el stock
		if producto["codigo"] == codigo:#si coincide el codigo procede a eliminarlo
			stocks.remove(producto)
			archivo = open("stocks.json", "w")
			json.dump(stocks, archivo, indent=2)
			archivo.close()
			print("Producto eliminado")
			time.sleep(2)
			break
	else:# aca se entra en caso de que no coincida el codigo
		print("Código inexistente")




