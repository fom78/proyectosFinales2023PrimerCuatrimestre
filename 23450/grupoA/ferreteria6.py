
import os
import time
import json
import moduloNegocio
import moduloReportes

carpeta = os.path.dirname(__file__)
os.chdir(carpeta)

def usuarioNuevo():#funcin para cargar nuevos usuarios
	usuario=open("usuarios.json","w")
	nomUs=input("Ingrese el nombre del nuevo usuario: ")
	contUs=input("Ingrese la contraseña: ")
	
	while True:
		tipoUs=input("Ingrese el tipo de usuario (administrador o usuario): ")
		if tipoUs=="administrador":
			tipoUs="administrador"
			break
		elif tipoUs=="usuario":
			tipoUs="usuario"
			break
		else:
			print("Debe escribir el tipo correctamente!!")

	usuarioNuevo={"usuario":nomUs,#creacion de diccionario con los datos
	  			"contrasenia":contUs,
	  			"tipo":tipoUs}
	usuarios.append(usuarioNuevo)
	archivo=open("usuarios.json","w")
	json.dump(usuarios,archivo, indent=2)
	archivo.close()
	print("Usuario agregado con exito")
	time.sleep(2)
	return usuarios

def modificarUsuario(listado):# aca se modifica el usuario en caso de querer hacerlo administrador usuario
	usuarioBuscar=input("Ingrese el nombre del usuario a modificar: ")
	for usuario in listado:#aca se itera los usuarios para buscar el usuario a modificar
		if usuarioBuscar in usuario.values():
			tipoUs=input("Ingrese el nuevo tipo de usuario(administrador o usuario): ")
			usuario["tipo"]=tipoUs
			archivoUsuario= open("usuarios.json","w")
			json.dump(listado,archivoUsuario, indent = 2)
			archivoUsuario.close()
			os.system("cls")
			print("Usuario modificado con éxito")
			time.sleep(2)
			break
	else:
		print("Usuario inexistente")
		time.sleep(2)								

def decorar(negocio):#decoracion para el negocio a administrar
	print("#"*80)
	print(f"#{negocio:^78}#")
	print("#"*80)
	return

def decorarMenu(nombreMenu):#decorar los menues del programa
	print("#"*80)
	print(f"#{nombreMenu:^78}#")
	print("#"*80)

try:# aca se controla si se entra al sistema por segunda vez
	archivoUsuario= open("usuarios.json","r")
	usuarios=json.load(archivoUsuario)
	archivoUsuario.close()
	archivo = open('nombre.txt', 'r')
	contenido = archivo.read()
	archivo.close()
except:#aca entra la primera vez para colocar el nombre usuario y contraseña por primera vez.
	usuarios=[]
	negocio=[]
	print("Bienvenido por primera vez a su sistema de gestión")
	print("Empecemos!!!!")
	nombre=input("Ingrese el nombre del negocio a administrar: ")
	negocioNom = open('nombre.txt', 'w')
	negocioNom.write(nombre)
	negocioNom.close()
	archivo = open('nombre.txt', 'r')
	contenido = archivo.read()
	archivo.close()
	decorar(contenido)
	usuario=input("Ingrese su usuario (ATENCION!!!! al ser la primera vez se a crear como administrador): ")
	contrasenia=input("Ingrese su contraseña: ")
	usuario={
		"usuario":usuario,
		"contrasenia":contrasenia,
  		"tipo":"administrador"}
	usuarios.append(usuario)
	archivoUsuario= open("usuarios.json","w")
	usuarios=json.dump(usuarios,archivoUsuario, indent = 2)
	archivoUsuario.close()
	os.system("cls")
	
try:# en caso de ya tener stocks se entra por aca para cargar el mism al sistema
	global stocks
	archivoStocks= open("stocks.json","r")
	stocks=json.load(archivoStocks)
	archivoStocks.close()
	
except:# en caso de no haber  stock se crea una lista vacia
	stocks=[]

def menuReportes():# funcion de menu de reportes para cualquier tipo de usuario
	while True:
		try:	
			os.system('cls')
			nombreMenu="Menú de reportes"
			decorarMenu(nombreMenu)
			print("\t1 - Mostrar Productos Nacionales")
			print("\t2 - Mostrar Productos Importados")
			print("\t3 - Mostrar Productos por Cantidad")
			print("\t4 - Mostrar Productos por Categoría")
			print("\t5 - Mostrar todos los productos")
			print("\t6 - Exportar todos los productos a .csv")
			print("\t0 - Volver al menú anterior")
			opcion = int(input("Ingrese una opción: "))
			if opcion == 0:
				break
			elif opcion == 1:
				moduloReportes.mostrarProductosNacionales(stocks)
			elif opcion == 2:
				moduloReportes.mostrarProductosImportados(stocks)
			elif opcion == 3:
				moduloReportes.mostrarProductosCantidad(stocks)
			elif opcion == 4:
				moduloReportes.mostrarProductosCategoria(stocks)
			elif opcion== 5:
				moduloReportes.mostrarProductos(stocks)
			elif opcion==6:
				os.system('python moduloCsv.py')
			else:
				print("Opción inválida. Intente nuevamente.")
				time.sleep(2)
		except:
			print("La opción debe ser un número")
			time.sleep(2)


while True:# aca empieza la gestion de del programa de gestion
	os.system('cls')
	negocio=contenido
	decorar(negocio)
	print(f"\t Bienvenido al sistema de {contenido}")
	print ("Selecciona una opción")
	print ("\t1 - Ingrese al menu de su negocio con usuario y contraseña")
	print ("\t0 - Salir")
	while True:
		try:
			opcion=int(input(": "))#aca se ingresa la opcion elegida
			break
		except ValueError:
			print("La opción debe ser un número")
			time.sleep(2)
	if opcion==1:
		user=input("Ingrese su usuario: ")
		contrasenia=input("Ingrese su contraseña: ")
		archivoUsuario= open("usuarios.json","r")
		usuarios=json.load(archivoUsuario)
		archivoUsuario.close()
		for usuario in usuarios:#aca se itera la lista de usuarios
			if user in usuario.values():#aca se controla si el valor de la variable user existe dentro de los valores de usuario
				if contrasenia in usuario.values():#aca se controla si el valor de la variable contrasenia existe dentro de los valores de usuario
					if "administrador" in usuario.values():# aca se controla si el usuario esta como "usuario" o "administrador"
						os.system('cls')
						while True:
							os.system('cls')
							nombreMenu="Menú de su negocio"
							decorarMenu(nombreMenu)
							print ("Selecciona una opción")
							print ("\t1 - Menú de gestion de su negocio")
							print ("\t2 - Menú de reportes de stocks de su negocio")
							print ("\t3 - Menú de gestión de usuarios")
							print ("\t0 - Cerrar sesión")
							while True:
								try:
									opcion1=int(input(": "))
									break
								except ValueError:
									print("La opción debe ser un número")
									time.sleep(2)
							if opcion1==0:#cerrar sesion
								os.system('cls')
								break
							elif opcion1==1:# menu de gesion para ingresar modificar y eliminar productos
								while True:
									os.system('cls')
									nombreMenu1="Menú de gestion de su negocio"
									decorarMenu(nombreMenu1)
									print ("Selecciona una opción")
									print ("\t1 - Ingresar un nuevo producto")
									print ("\t2 - Modificar un producto")
									print ("\t3 - Eliminar un producto")
									print ("\t0 - Volver al menú anterior")
									while True:
										try:
											opcion2=int(input(": "))
											break
										except ValueError:
											print("La opción debe ser un número")
											time.sleep(2)
										

									if opcion2==1:
										moduloNegocio.productoNuevo(stocks)
										
									elif opcion2==2:
										moduloNegocio.modificar(stocks)
											
									elif opcion2==3:
										moduloNegocio.eliminar(stocks)
									elif opcion2==0:
										break
									else:
										print("Opción incorrecta")
										time.sleep(2)			
							elif opcion1==2:
								menuReportes()#menu para visualizar los distintos stocks
													
							elif opcion1==3:# con esta opcion se agregan usuarios o se modifica el tipo
								while True:
									os.system('cls')
									nombreMenu2="Menú de gestión de usuarios"
									decorarMenu(nombreMenu2)
									print ("Selecciona una opción")
									print ("\t1 - Ingresar un nuevo usuario")
									print ("\t2 - Modificar un usuario")
									print ("\t0 - Volver al menú anterior")
									while True:
										try:
											opcion3=int(input(": "))
											break
										except ValueError:
											print("La opción debe ser un número")
											time.sleep(2)
									if opcion3==0:
										break
									elif opcion3==1:
										usuarioNuevo()#funcion para agregar usuarios
									elif opcion3==2:
										modificarUsuario(usuarios)#funcion para modificar el tipo de usuario
									else:
										print("Opción incorrecta")
										time.sleep(2)	

							else:
								print("Opción incorrecta")
								time.sleep(2)				
						break
					elif "admnistrador" not in usuario.values():#si el usuario no es administrador ingresara por aca para la gestion de stocks nada mas
						
						while True:
							os.system('cls')
							decorar(contenido)
							print(f"\t Bienvenido al sistema de {contenido}")
							print ("Selecciona una opción")
							print ("\t1 - Menú reportes de stock")
							print ("\t0 - Cerrar sesión")
							while True:
								try:
									opcion2=int(input(": "))
									break
								except ValueError:
									print("La opción debe ser un número")
									time.sleep(2)
							os.system('cls')
							if opcion2==0:#cerrar sesion
								break
							elif opcion2==1:
								menuReportes()#aca va al menu de reportes de stocks que son iguales para ambos usuarios
							else:
								print("Opción incorrecta")
								time.sleep(2)
								
					break				

										
				else:# aca se entra en caso de colocar mal la contraseña
					os.system('cls')
					print("Contraseña inválida")
					time.sleep(2)
					os.system("cls")
					break			
							
		else:# aca entra en caso de no tener usuario o colocarlo mal
			os.system("cls")
			print("Usuario inválido")
			time.sleep(2)
			os.system("cls")
			continue
	elif opcion==0:# salir de todo el programa
		os.system('cls')
		break
	else:
		print("Opción incorrecta")
		time.sleep(2)
print("Gracias por usar nuestro Software de Gestión")
time.sleep(2)						
						
					