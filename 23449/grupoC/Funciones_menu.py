import crud
import Funciones_secundarias
import getpass
import os


def sesion_ferreteria(lista):
  while True:
    print("\nINICIE SESIÓN PARA CONTINUAR!")
    usuario = input("\nIngrese Usuario: ") #ferreteria
    usuario = usuario.title()
    contraseña = getpass.getpass("Ingrese Contraseña: ") #ferreteria2023
    if usuario == "Ferreteria" and contraseña == "ferreteria2023":
      os.system ("cls")
      print(f"Usuario: {usuario}")
      print(f"Contraseña: {'*' * len(contraseña)}")
      print("\nSe ha iniciado la sesión!")
      gestion_productos(lista)
      break
    elif usuario != "Ferreteria" or contraseña != "ferreteria2023":
      print("\nUSUARIO O CONTRASEÑA INCORRECTOS!")

def gestion_productos(lista):
  while True:
    cadena2 = "====PRODUCTOS===="
    print(cadena2.center(50, " "))
    print("\n1-Ingresar nuevo producto")
    print("2-Modificar un producto")
    print("3-Eliminar un producto")
    print("Pesione 0 para volver al menú principal")

    opcion_gestion_productos = int(input("Ingrese una opción (Numerica): "))

    if opcion_gestion_productos == 1:
      print("Agregar productos")
      crud.agregar_producto(lista)
      os.system ("cls")
      print("Producto agregado!!!")
      crud.guardar_datos(lista)
    elif opcion_gestion_productos == 2:
      print("Modificar producto")
      crud.modificar_producto(lista)
      os.system ("cls")
      print("Producto Modificado!!!")
      crud.guardar_datos(lista)
    elif opcion_gestion_productos == 3:
      print("Eliminar producto")
      crud.eliminar_producto(lista)
      os.system ("cls")
      print("Producto eliminado con exito!!!")
      crud.guardar_datos(lista)
    elif opcion_gestion_productos == 0:
      break
    else:
      print("Opción Inválida. Inténtelo Nuevamente!")

def reportes(lista):  
  while True:   

    cadena3 = "====REPORTES===="
    print(cadena3.center(50, " "))
    print("\n1-Mostrar productos nacionales")
    print("2-Mostrar produtos importados")
    print("3-Mostrar productos por categoría")
    print("0-Menú Principal")

    opcion_reportes = int(input("\nIngrese una opción (Numerica): "))
  
    if opcion_reportes == 1: 
      Funciones_secundarias.mostrar_productos_nacionales(lista)
    elif opcion_reportes == 2:
      Funciones_secundarias.mostrar_productos_importados(lista)

    elif opcion_reportes == 3:
      Funciones_secundarias.mostrar_productos_por_categoria(lista)
    elif opcion_reportes == 0:
      break
    else:
      print("Opción Inválida. Intente nuevamente")