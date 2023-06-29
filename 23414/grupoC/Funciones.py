import json 
import os
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)

def deco(caracter,repeticion):
   print (caracter*repeticion)

def menuInicioA():
    print("")
    deco(":",50)
    print("##### Inicia tu sesion #####")
    print("[1] Crear Usuario")
    print("[2] Iniciar Sesion")
    print("[0] Salir")
      
def mostrarMenuA():
    print ("")
    deco(":",50)
    print("##### Gestión de Stock #####")
    print("[1] Gestion de productos")
    print("[2] Mostrar reportes")
    print("[0] Salir")
        
def mostrarMenuB():
    print("")
    deco(":",50)
    print("##### Menu de productos #####")
    print("[1] Agregar producto")
    print("[2] Modificar producto")
    print("[3] Eliminar producto")
    print("[0] Volver al Menu Principal")
    

def opcion_numero():
    while True:
        try:
          opcion = int (input("opcion seleccionada: "))
          return opcion
        except:
         print ("Elije una opcion correcta")

def datos_empleados():
    try:
        file = open("lista-empleados.json", "r")
        empleados = json.load(file)
        file.close()
    except FileNotFoundError:
        empleados= []
    return empleados        

def alta(listado):
 print("")
 deco(":",50)
 print("***Alta usuario***")
 while True:
    try:
        dni = int(input ("Ingrese su DNI: "))
        break
    except:
        print("El DNI debe ser solamente numerico")
 
 
 contrasenia = (input ("Ingrese una contraseña númerica: "))
        
 empleado = {
  "dni" : dni,
  "contrasenia" : contrasenia
 }
 print ("Usuario guardado")  

 listado.append(empleado)
 file = open("lista-empleados.json", "w")
 json.dump(listado, file, indent=1)
 file.close

def sesion(empleados): 
    print("")
    deco(":",50)
    print("***Inicio sesión***")
    empleados = datos_empleados()
    
    while True:
        try:
            dni = int(input("Ingrese su DNI: "))
            break
        except ValueError:
            print("El DNI debe ser solamente numérico")

    contrasenia = input("Ingrese su contraseña: ")
    for empleado in empleados:
        if dni == empleado["dni"] and contrasenia == empleado["contrasenia"]:
            print("Bienvenido")
            return True
    else:
        print("Datos incorrectos")
        return False


def datos_productos():
    try:
        with open("productos.json", "r") as file:
            productos = json.load(file)
            file.close()
    except FileNotFoundError:
        productos = []

    return productos

def agregarProducto(listado):
    print("")
    deco(":",50)
    print("/// Agregar producto ///")
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("La cantidad del producto debe ser números enteros.")

    nombre = input("Ingrese el nombre: ")
    categoria = input("Ingrese la categoría: ")

    EsNacional = input("El producto es Nacional (s/n): ")
    if EsNacional == "s":
        EsNacional = True
    else:
        EsNacional = False

    producto = {
        "codigo": codigo(listado),
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "EsNacional": EsNacional
    }

    print(f"El producto ({producto}) ha sido agregado.") # para confirmar
    listado.append(producto)
    
    with open("productos.json", "w") as file:
        json.dump(listado, file, indent=3)
      
def modificarProducto(listado, producto): #modificar producto

    print("/// MODIFICAR EL PRODUCTO ///")
    while True:
        try:
            codigo = int(input(f"Ingrese el nuevo código del producto para modificar el anterior ({producto['codigo']}): "))
            cantidad = int(input(f"Ingrese la cantidad ({producto['cantidad']}): "))
            break
        except ValueError:
            print("El código y la cantidad del producto deben ser números enteros.")

    producto["codigo"] = codigo
    producto["nombre"] = input(f"Ingrese el nombre ({producto['nombre']}): ")
    producto["categoria"] = input(f"Ingrese la categoría ({producto['categoria']}): ")
    producto["cantidad"] = cantidad

    EsNacional = input("El producto es Nacional (s/n) : ")
    if EsNacional == "s":
        producto["EsNacional"] = True
    else:
        producto["EsNacional"] = False

    with open("productos.json", "w") as file:
        json.dump(listado, file, indent=2)
    
    print("Producto modificado correctamente.")
        
def eliminarProducto(listado):
   print("")
   deco(":",50)
   print("/// Eliminar Producto ///")
   listado = datos_productos()
   codigoBorrado = int(input("Ingresa el codigo del producto a borrar: "))
   indice = 0
    
   for p in listado:
        if codigoBorrado == p ["codigo"]:
            print("producto eliminado con exito")
            listado.pop(indice)
            break
        indice = indice + 1   
   else:
        print("El producto no se encuentra en el listado")
    
   file = open ("productos.json", "w")
   json.dump(listado,file, indent=2)
   file.close()

def codigo(listado):
    maximo = -1
    for producto in listado:
        if producto["codigo"] > maximo:
            maximo = producto["codigo"]
    siguiente = maximo + 1
    return siguiente


def menuDelPrograma():

 while True: #GESTION DE STOCK ===============================================================
    mostrarMenuA()
    opcion = opcion_numero() 
    
    if opcion == 1: #MENU DE PRODUCTOS ======================================================
        while True:
            mostrarMenuB()
            opcion = opcion_numero()
            
            if opcion == 1: #AGREGAR UN PRODUCTO
                productos = datos_productos()
                agregarProducto(productos)
                
            elif opcion == 2: #MODIFICAR EL PRODUCTO
                    print("")
                    deco(":",50)
                    print("/// MODIFICAR PRODUCTO ///")
                    productos = datos_productos()

                    codigoBusqueda = int(input("Ingrese el código del producto: "))
                    for producto in productos:
                         if codigoBusqueda == producto["codigo"]:
                            modificarProducto(productos, producto)
                            break
                            
            elif opcion == 3: #ELIMINAR PRODUCTOS ===============================================
                print("ELIMINAR PRODUCTO")
                producto = datos_productos()
                eliminarProducto(producto)
            elif opcion == 0: #VOLVER ATRAS ====================================================
                break    
            
            else:
                print("ingrese una opcion valida.")
    elif opcion == 2: #MOSTRAR PRODUCTOS ======================================================
        print("///Reportes///")
        print("""
        [1] Lista de productos
        [2] Listado de codigos
        [3] Listado por categoria
        [0] Salir
        """)
        opcion = opcion_numero()
        
        if opcion == 1:
           print ("Lista de productos")
           productos= datos_productos()
           for producto in productos:
             print(f"Producto: {producto['codigo']} -- Nombre: {producto['nombre']} -- Categoria: {producto['categoria']} -- Cantidad: {producto['cantidad']} -- EsNacional: {producto['EsNacional']}")
    
        elif opcion == 2:
            print ("Listado de codigos")
            for producto in productos:
             print (f"{producto['codigo']} -- {producto['nombre']}")

        elif opcion == 3:
            print ("Listado de categoria") 
            productos = datos_productos()
            categoria = input("Categoria a ver: ")
            for producto in productos:
               if categoria.lower() == producto['categoria'].lower():
                print (f"{producto['nombre']}") 

        elif opcion == 0:
            break     

        else:
            print("ingrese una opcion valida.")

    elif opcion == 0: #VOLVER ATRAS ===========================================================
                break
    
