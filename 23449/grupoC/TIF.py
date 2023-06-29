import Funciones_menu
from crud import cargar_datos


productos = cargar_datos()

while True:
  titulo = "====BIENVENIDOS A LA FERRETERÍA===="
  print(titulo.center(50," "))
  cadena = "====GESTIÓN DE STOCK===="
  print(cadena.center(50, " "))
  print("\n1-Gestión de Productos")
  print("2-Reportes")
  print("0-Salir")

  opcion = int(input("Ingrese la opción deseada: "))

  if opcion == 1:
    Funciones_menu.sesion_ferreteria(productos)
  elif opcion == 2:
    Funciones_menu.reportes(productos)
  elif opcion == 0:
    print("¡¡¡Hasta Luego!!!")
    break
  
  else:
    print("Opción inválida. Volvé a intentarlo")