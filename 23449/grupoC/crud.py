import json

def cargar_datos():
  datos = open("productos.json", "r")
  productos = json.load(datos)
  datos.close()
  return productos

def guardar_datos(lista):
  with open("productos.json", "w") as archivo:
    json.dump(productos_por_codigo(lista), archivo, indent=2)

def mostrar_datos(lista):
  print("\nMostrando productos!!")
  for producto in lista:
    print(f"""
          Codigo = {producto['codigo']}
          Nombre = {producto['nombre']}
          Categoria = {producto['categoria']}
          Origen = {producto['origen']}""")

def eliminar_producto(lista):
  cod_eliminar = input("\nIngrese el codigo del producto a Eliminar: ")
  cod_eliminar = cod_eliminar.title()
  for producto in lista:
    if cod_eliminar == producto['codigo']:
      lista.remove(producto)
      return lista

def agregar_producto(lista):
  print("Categorias existentes: (C)onstruccion - (J)ardin - (H)erramientas - (I)luminacion - (V)arios ")
  codigo = input("\nIngrese codigo formato (X000): ")
  cont = True
  while cont:
    for producto in lista:
      if codigo==producto["codigo"]:
        print("el codigo ya existe")
        codigo = input("\nIngrese otro codigo formato (X000): ") #Pide ingresar nuevamente el codigo.
        break
    else:
      cont = False
  #falto contemplar el ingreso de un codigo ya existente!!!
  codigo = codigo.title()
  nombre = input("Ingrese nombre: ")
  nombre = nombre.title()
  print("Categorias existentes: Construccion - Jardin - Herramientas - Iluminacion - Varios ")
  categoria = input("Ingrese categoria: ")
  categoria = categoria.title()
  cantidad = int(input("Ingrese cantidad: "))
  origen = input("El producto es Nacional o Importado?: ")
  origen = origen.title()
  
  producto={"codigo":codigo,"nombre":nombre,"categoria":categoria,"cantidad":cantidad,"origen":origen}
  
  lista.append(producto)
  print("Producto Agregado con exito!!!")

def modificar_producto(lista):
  mostrar_datos(lista)
  cod_modificar = input("\nIngrese el codigo del producto a Modificar: ")
  cantidad_productos = len(lista)
  contador_productos = 0
  for producto in lista:
    if cod_modificar.capitalize() == producto['codigo']:
      print(f"\nModificar nombre de {producto['nombre']}? ")
      nuevo_nombre = input("Ingrese nuevo nombre (si no desea modificar presione 'ENTER'): ")
      if nuevo_nombre == "":
        nuevo_nombre = producto['nombre']
      else:
        nuevo_nombre=nuevo_nombre.title()
      print(f"\nLa cantidad del producto es {producto['cantidad']}. Modificar? ")
      nueva_cantidad = (input("Si no desea modificar presione 'ENTER': "))
      if nueva_cantidad == "":
        nueva_cantidad = producto['cantidad']
      else:
        nueva_cantidad = int(nueva_cantidad)
      print(f"\nLa categoria del producto es {producto['categoria']}. Modificar? ")
      nueva_categoria = input("Si no desea modificar presione 'ENTER': ")
      if nueva_categoria == "":
        nueva_categoria = producto['categoria']
      else:
        nueva_categoria=nueva_categoria.title()
      print(f"\nEl producto es de origen: {producto['origen']}, Modificar? ")
      nuevo_origen = input("Si no desea modificar presione 'ENTER': ")
      if nuevo_origen == "":
        nuevo_origen = producto['origen']
      else:
        nuevo_origen=nuevo_origen.title()
      
      producto ={
        "codigo":producto['codigo'],
        "nombre":nuevo_nombre,
        "categoria":nueva_categoria,
        "cantidad":nueva_cantidad,
        "origen":nuevo_origen
      }
      lista[contador_productos] = producto
      print(f"Producto modificado con exito!!")
      break
    else:
      contador_productos = contador_productos + 1
      if contador_productos == cantidad_productos:
        print(f"EL codigo: {cod_modificar.capitalize()} ingresado no pertenece a ningun producto en el Catalogo")

def productos_por_codigo(lista):
  ordenadas_por_codigo = sorted(lista, key=lambda x:x['codigo'])

  return ordenadas_por_codigo