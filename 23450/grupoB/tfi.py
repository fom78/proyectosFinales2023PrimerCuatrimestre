def elegirOpcionMenu ():  #Muestra menú principal y devuelve la opción que eligió el usuario
    print(" ")
    print("BIENVENIDO A PEDIDOS B YA!")
    print(" ")
    print("Menú principal:")
    print("[1] Gestión de pedidos")
    print("[2] Reportes")
    print("[0] Salir")
    return int(input("Elija una opción: "))

def menuGestion ():  #Muestra menú de gestión de pedidos y devuelve la opción que eligió el usuario
    print(" ")
    print("1. GESTIÓN DE PEDIDOS")
    print(" ")
    print("[1] Ingresar pedido")
    print("[2] Modificar pedido")
    print("[3] Eliminar pedido")
    print("[0] Volver")
    return int(input("Elija una opción: "))

def productosDisponibles ():
    #Armo tupla de productos (ahora solo hago de la categoría de bebidas, después agregamos el resto)
    productos = (
        #Categoría 0 (bebidas)
        (#(bebidas sin alcohol)
            {"nombre": "Aquarius pomelo 500 mL", "precio": 300},
            {"nombre": "Coca-cola 500 mL", "precio": 350},
        ),
        (#(bebidas con alcohol)
            {"nombre": "Fernet 0.75 L", "precio": 2500},
            {"nombre": "Cerveza Antares caravana lata 473 mL ", "precio": 600},
        ),
    )
    return productos

def ingresarUnProducto():
    print(" ")
    print("1. Bebidas (después agregaba otros)")
    categoriaProducto = int(input("Seleccione la categoría a la que pertenece el producto: "))
    if categoriaProducto == 1:
        i = 0  #corresponde a la categoría de bebidas en el array de productos
        subCategoria = int(input("Seleccione 1 para bebidas sin alcohol o 2 para bebidas con alcohol: "))
        if subCategoria == 1:
            j = 0  #corresponde con el índice de bebidas sin alcohol
            k = 0
            for unProducto in productos[j]:   #NO OLVIDAR DE MODIFICAR CUANDO SE AGREGUEN MÁS CATEGORÍAS
                k += 1
                print(f"{k}- ")
                print(unProducto["nombre"])  #lo pongo así porque sino me salta error cuando lo hago con f-string
            r = int(input("Seleccione un producto de los disponibles: "))
            k = 0
            for x in productos[j]:
                if k == r-1:
                    p = x
                k += 1
        else:
            print("Ya continuaremos agregando productos...")
    else:
        print("ya vamos a agregar otros productos...")

    cant = int(input("Ingrese la cantidad que desea pedir: "))
    prod = {
        "nombre" : p["nombre"],
        "cantidad" : cant,
        "precioProductos" : cant * p["precio"],  #acordarse de agregar la i cuando se agreguen más categorías!!
    }

    print("###################")
    print("PARA CHEQUEAR QUE SE INGRESÓ BIEN EL PRODUCTO")
    for i in prod.values():
        print(i)
    print("###################")
    return prod

def ingresarProductos():
    listaProductosIngresados = []
    cantProductos = int(input("Ingrese la cantidad de productos distintos que desea ingresar: "))
    while (cantProductos <= 0):
        cantProductos = int(input("Ingrese una cantidad mayor a cero"))
    for i in range(cantProductos):
        print(f"Producto número {i+1}:")
        productoNuevo = ingresarUnProducto()  #Se ingresa un producto nuevo en forma de diccionario
        listaProductosIngresados.append(productoNuevo)
    print("PEDIDO INGRESADO EXITOSAMENTE")
    return listaProductosIngresados

def agregarPedido ():
    nuevoPedido = {
        "codigo": int(input("ingrese el número entero del código del pedido: ")),
        "productos": ingresarProductos(),  #array de diccionario con producto-cantidad-precio por producto total
        "contacto": 1,  #lo dejo así pero hay que hacer las funciones
        "ubicacion": 1,
        "precio total": 1, 
    }
    return nuevoPedido

    

############# ALGORITMO PRINCIPAL ##################################3

usuarioAdmin = "abc"
contraseniaAdmin = "123"
primerIngreso = False

while (not primerIngreso) :
    usuarioIngresado = str(input("Ingrese el usuario:"))
    contraseniaIngresada = str(input("Ingrese la contraseña:"))
    if (usuarioIngresado != usuarioAdmin or contraseniaIngresada != contraseniaAdmin):
        print("Usuario o contraseña incorrecto.")
        print(" ")
    else:
        primerIngreso = True


opcionMenu = 1 #Solo para que ingrese si o si al while la primera vez
pedidos = []  #los pedidos se guardan en lista de diccionario vacía
productos = productosDisponibles() 


while (opcionMenu != 0):
    opcionMenu = elegirOpcionMenu()  # 1 para gestión de pedidos, 2 para reportes y 0 para salir
    while (opcionMenu < 0 or opcionMenu > 2):
        opcionMenu = int(input(("OPCIÓN INVÁLIDA. Por favor, ingrese 1, 2 ó 0: ")))
    if (opcionMenu == 1): #Gestión de pedidos
        opcionMenuGestion = menuGestion()  # 1 para añadir pedido, 2 para modificar, 3 para eliminar y 0 para volver
        while (opcionMenu < 0 or opcionMenu > 2):
            opcionMenu = int(input(("OPCIÓN INVÁLIDA. Por favor, ingrese 1, 2, 3 ó 0: ")))
        if (opcionMenuGestion != 0):
            if (opcionMenuGestion == 1): #añadir pedido
                crearPedido = agregarPedido()
                pedidos.append(crearPedido)
            elif (opcionMenuGestion == 2): #modificar pedido
                print("Acá va la función de modificar pedido")
            elif (opcionMenuGestion == 3): #eliminar pedido
                print("Acá va la función para eliminar pedido")
    elif (opcionMenu == 2): #Reportes
        print("Acá va la función de mostrar menú reportes, leer la opción que elige el usuario y luego las funciones para cada una de las opciones de reportes con un if-elif-else")



#Al salir del while
print(" ----- ")
print("Hasta la próxima!")