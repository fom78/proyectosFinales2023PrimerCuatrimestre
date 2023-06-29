def mostrar_productos_nacionales(lista):
  for producto in lista:
    if producto["origen"] == "Nacional":
      mostrar_produ(producto)
      print("")

def mostrar_productos_importados(lista): 
  print("Productos Importados: ")
  for producto in lista:
    if producto["origen"] == "Importado":
      mostrar_produ(producto)
      print("")

def mostrar_productos_por_categoria(lista):
  print ("Categorias: \n1- Construccion \n2- Herramienta \n3- Jardin \n4- Iluminacion \n5- Varios")
  miCategoria = input("Ingrese el numero de la categoria: ")
  for producto in lista:
    if miCategoria == "1":
      if producto['categoria'] == "Construccion":
        print("\nCATEGORIA: ", producto ["categoria"])
        mostrar_produ(producto)
        print("")
    elif miCategoria == "2":
      if producto['categoria'] == "Herramienta":
        print("\nCATEGORIA: ", producto ["categoria"])
        mostrar_produ(producto)
        print("")
    elif miCategoria == "3":
      if producto['categoria'] == "Jardin":
        print("\nCATEGORIA: ", producto ["categoria"])
        mostrar_produ(producto)
        print("")
    elif miCategoria == "4":
      if producto['categoria'] == "Iluminacion":
        print("\nCATEGORIA: ", producto ["categoria"])
        mostrar_produ(producto)
        print("")
    elif miCategoria == "5":
      if producto['categoria'] == "Varios":
        print("\nCATEGORIA: ", producto ["categoria"])
        mostrar_produ(producto)
        print("")

def mostrar_produ(item):
  print("Nombre: ", item ["nombre"])
  print("Código: ", item ["codigo"])
  print("Origen: ", item ["origen"])
  if item["cantidad"] > 0:
    print("HAY STOCK!")
  else:
    print("NO HAY STOCK!")
  print("")