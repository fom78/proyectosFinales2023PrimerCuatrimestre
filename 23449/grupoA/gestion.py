import json
import random
import os
import time


dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)

def cargarProductos(): #Cargar lista desde el archivo JSON.
  try:
    archivo=open("listaProductos.json","r",encoding="utf-8")
    datos=json.load(archivo)
    archivo.close()
  except FileNotFoundError:
    datos=[]
  return datos

def guardarProductos(listado): #Guardar lista en el archivo JSON.

    archivo=open("listaProductos.json","w",encoding="utf-8")
    listado=json.dump(listado,archivo,ensure_ascii=False,indent=4)
    archivo.close()

def generarCod(cadena): #Función para generar un código.
  datos=cargarProductos()
  codigo= cadena[0].upper()+str(random.randint(1000,9900))
  for producto in datos:
    if codigo==producto["codigo"]:
      filtro=[]
      for producto in datos:
        if codigo[0] in producto["codigo"]:
          filtro.append(producto["codigo"])
      nvoNum=int(max(filtro).strip(codigo[0]))+1
      codigo=codigo[0]+str(nvoNum)
  return codigo

def buscarCod(listado,llave,cod): #Buscar código en la lista
	for producto in listado:
		if producto[llave]==cod:
			return producto

def inputEntero(cadena): #robada al profe
	while True:
		try:
			entero=int(input(cadena))
			return entero
		except:
			print("Sólo números")

def decorar(nro): #Distintas decoraciones
  if nro==1:
    print(":"*60)
    print ("."*60)
    print(":"*60)
  elif nro==2:
    print("#"*50)
  elif nro==3:
    print("-"*23)

def ingresarNuevoProducto(): #Función para INGRESAR PRODUCTO.
  datos=cargarProductos()
  nombre = input("Ingrese NOMBRE:")
  categoria = input("Ingrese CATEGORIA:")
  while True:
    try:
      cantidad=int(input("Ingrese la CANTIDAD de productos: "))
      break
    except:
      print("VALOR NO VALIDO!!!Ingrese un número ")  
  
  nacional = input("Es NACIONAL el producto?>>> (s/n):")
  if nacional.upper()=="S":
    nacional = True
  else:
    nacional = False
  codigo=generarCod(nombre)
   
  producto={"codigo":codigo,
            "nombre":nombre.capitalize(),
            "categoria":categoria.capitalize(),
            "cantidad":cantidad,
            "nacional":nacional
           }
  decorar(3)
  print(":::PRODUCTO INGRESADO:::")
  print("Codigo: ", producto["codigo"])
  print("Nombre: ", producto["nombre"])
  print("Categoria: ", producto["categoria"])
  print("Cantidad: ", producto["cantidad"])
  if producto["nacional"]:
    print("Producto Nacional")
  else:
    print("Producto Importado")
  decorar(3)
  datos.append(producto)
  guardarProductos(datos)
  print("El producto", nombre, "fue ingresado con exito")
  pregunta=input ("Desea ingresar otro producto? S/N ")
  if pregunta.upper()=="S":
    ingresarNuevoProducto()

def modificarProducto(): #Función para MODIFICAR PRODUCTO.
  datos=cargarProductos()
  codigoBuscar=input("Ingrese el codigo del elemento a modificar: ")
  codigoBuscar=codigoBuscar.capitalize()
  producto=buscarCod(datos,"codigo",codigoBuscar)
  if producto:
    decorar(3)
    print(":::PRODUCTO ENCONTRADO:::")
    print("Ingrese dato para modificar o ENTER para avanzar")
    nombre=input("Ingrese NOMBRE nuevo: ")
    if nombre=="":
      nombre=producto["nombre"]
    else:
      producto["nombre"]=nombre.capitalize()
    
    while True:
      try:
        cantidad=int(input("Ingrese CANTIDAD nueva: "))
        break
      except:
        print("Sólo números...")
    if cantidad=="":
      cantidad=producto["cantidad"]
    else:
      producto["cantidad"]=cantidad
    
    categoria=input("Ingrese CATEGORIA nueva: ")
    if categoria=="":
      categoria=producto["categoria"]
    else:
      producto["categoria"]=categoria.capitalize()

    nacional=input("¿Es NACIONAL el producto?: ")
    if nacional=="":
      producto["nacional"]=producto["nacional"]
    elif nacional.upper()=="S":
      producto["nacional"]=True
    else:
      producto["nacional"]= False
    guardarProductos(datos)
  else:   
    print("No existe un producto con ese código")
  pregunta=input ("¿Desea modificar otro producto? (S/N): ")
  if pregunta.upper()=="S":
    modificarProducto()

def eliminarProducto(): #Función para ELIMINAR PRODUCTO.
  datos=cargarProductos()
  codigoBuscar=input("Ingrese el código del producto que desea eliminar: ")  
  codigoBuscar=codigoBuscar.capitalize()
  producto=buscarCod(datos,"codigo",codigoBuscar)
  if producto:
    print(":::PRODUCTO ENCONTRADO:::")
    print("Nombre: ", producto["nombre"])
    print("Codigo: ", producto["codigo"])
    decorar(3)
    opcion=input("¿Desea eliminarlo? (S/N): ")
    if opcion.upper()=="S":
      datos.remove(producto)
      print(":::PRODUCTO BORRADO:::")
      guardarProductos(datos)
  else:
    print("No existe un producto con ese código")
  pregunta=input("Desea eliminar otro producto? (S/N): ")
  if pregunta.upper()=="S":
    eliminarProducto()
 
def verProductoPor(llave,valor): #Mostrar productos segun key y value
  datos=cargarProductos()
  for producto in datos:
    if producto[llave]==valor:
      time.sleep(0.3)
      print("Codigo: ", producto["codigo"])
      print("Nombre: ", producto["nombre"])
      print("Categoria: ", producto["categoria"])
      print("Cantidad: ", producto["cantidad"])
      if producto["nacional"]:
        print("Producto Nacional")
        os.system("pause")
      else:
        print("Producto Importado")
        os.system("pause")
      decorar(3)
    
  decorar(2)

def categoriasXNro(nro):
  if nro==1:
    catBuscada="Accesorios para el hogar"
  if nro==2:
    catBuscada="Construccion"
  if nro==3:
    catBuscada="Cerraduras y Seguridad"
  if nro==4:
    catBuscada="Ferreteria de jardin"
  if nro==5:
    catBuscada="Electricidad"
  if nro==6:
    catBuscada="Fontaneria"
  if nro==7:
    catBuscada="Pintura y accesorios"
  if nro==8:
    catBuscada="Material de fijacion"
  if nro==9:
    catBuscada="Equipos de seguridad"
  if nro==10:
    catBuscada="Herramientas electricas"
  if nro==11:
    catBuscada="Herramientas manuales"
  return catBuscada

def verInventario(): 
  datos=cargarProductos() # Lista
  # Acceso a los datos de cada producto
  for producto in datos:
    print("Codigo: ", producto["codigo"])
    print("Nombre: ", producto["nombre"])
    print("Categoria: ", producto["categoria"])
    print("Cantidad: ", producto["cantidad"])
    if producto["nacional"]:
      print("Producto Nacional")
    else:
      print("Producto Importado")
    decorar(3)
  time.sleep(0.3)  
  decorar(2)

def stockLim():
  datos=cargarProductos()
  decorar(2)
  print("Productos con bajo stock")
  for producto in datos:
    if producto["cantidad"] <= 20 and producto["cantidad"] >=1:
      time.sleep(0.5)
      print("Producto:", producto["nombre"])
      print("Cantidad:", producto["cantidad"])
      print("Código:", producto["codigo"])
      print("Categoría:", producto["categoria"]) 
      decorar(3)
  decorar(2)
