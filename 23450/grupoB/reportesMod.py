import json
import deco
import os
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ----------- Reporte Mostrar producto por codigo ----------------------- #
def productoPorCodigo():
    productos = open("ProductosAlmacen.json", "r")
    listaProductos = json.load(productos)
    productos.close()
    os.system("cls")
    deco.decorarConCuadrado("Selección de producto por código".upper())
    listCodigo=[] 
    for producto in listaProductos:
        listCodigo.append({producto['codigo']})
        deco.decorarConCuadradoCh(producto['codigo'])
    
    while True:
        seleccionDecodigo = input("\nSeleccione el código del producto que desea ver: ").upper()
        for producto in listaProductos:
            if producto['codigo'] == seleccionDecodigo:
                cant = str(producto['cant'])
                prec = str(producto['precio'])
                deco.tablaCompleta()
                print(f"│{producto['codigo']:^8}│ {(producto['producto']).title():<44}│ {(producto['categoria']).title():<18}│{cant:^10}│${prec:^11}│")
                print("├────────┼─────────────────────────────────────────────┼───────────────────┼──────────┼────────────┤")
        # ------ Condicion para continuar ------ #
        seguir = input("\n¿Desea ver otro producto? (SI/NO): ")
        seguir = seguir.upper()

        while seguir != "SI" and seguir != "NO":
            seguir = input("\n¿Desea ver otro producto? (SI/NO): ")

        if seguir == "NO":
            os.system("cls")
            break

# ------------- Reporte Mostrar producto por Cantidad  ------------------------ #
def productoPorCantidad():
    productos = open("ProductosAlmacen.json", "r")
    listaProductos = json.load(productos)
    productos.close()
    os.system("cls")
    deco.decorarConCuadrado("Selección de producto por cantidad".upper())
    listaCant = []
    for producto in listaProductos:
        if listaCant == []:
            listaCant.append(producto['cant'])

        if not (producto['cant'] in listaCant):
            listaCant.append(producto['cant'])

    
    print("\n¿Cómo quiere ver los productos?")
    print("\n[1] Mayor a menor")
    print("\n[2] Menor a mayor")

    eleccion = int(input("\nOpción ([0] volver al menú): "))

    while eleccion != 0 and eleccion != 1 and eleccion != 2:
        eleccion = int(input("\nOpción: "))
        
    while True:
        if eleccion == 1:
            listaCant.sort(reverse=True)

            deco.tablaCantidad()
            for cantidad in listaCant:
                for producto in listaProductos:
                    if cantidad == producto['cant']:
                        cant = str(producto['cant'])
                        print(f"│{cant:^10}│ {(producto['producto']).title():<44}│")
                        print("├──────────┼─────────────────────────────────────────────┤")
  
            eleccion = int(input("\n[2] Menor a mayor / [0] Volver al menú: "))

            while eleccion != 0 and eleccion != 2:
                eleccion = int(input("\n[2] Menor a mayor / [0] Volver al menú: "))
        
        elif eleccion == 2:
            listaCant.sort()

            deco.tablaCantidad()
            for cantidad in listaCant:
                for producto in listaProductos:
                    if cantidad == producto['cant']:
                        cant = str(producto['cant'])
                        print(f"│{cant:^10}│ {(producto['producto']).title():<44}│")
                        print("├──────────┼─────────────────────────────────────────────┤")

            eleccion = int(input("\n[1] Mayor a menor / [0] Volver al menú: "))

            while eleccion != 0 and eleccion != 1:
                eleccion = int(input("\n[1] Mayor a menor / [0] Volver al menú: "))
        
        if eleccion == 0:
            os.system("cls")
            break

# ------------ Reporte Mostrar producto por Nombre ------------------------- #
def productoPorNombre():
    productos = open("ProductosAlmacen.json", "r")
    listaProductos = json.load(productos)
    productos.close()
    os.system("cls")
    deco.decorarConCuadrado("selección de producto por nombre".upper())

    deco.tablaCompleta()
    for letra in abecedario.lower():
        for producto in listaProductos:
            if producto['producto'][0] == letra:
                cant = str(producto['cant'])
                prec = str(producto['precio'])
                print(f"│{producto['codigo']:^8}│ {(producto['producto']).title():<44}│ {(producto['categoria']).title():<18}│{cant:^10}│${prec:^11}│")
                print("├────────┼─────────────────────────────────────────────┼───────────────────┼──────────┼────────────┤")

    seguir = int(input("\nEscriba [0] para volver al menú: "))
    seguir = seguir
    os.system("cls")

    while seguir != 0:
        seguir = int(input("\nEscriba [0] para volver al menú: "))

# ------------ Reporte Mostrar producto por Categoria --------------------- #
def productoPorCategoria():
    productos = open("ProductosAlmacen.json", "r")
    listaProductos = json.load(productos)
    productos.close()
    os.system("cls")
    deco.decorarConCuadrado("selección de producto por categoría".upper())

    listaCategorias = []
    for producto in listaProductos:
        if listaCategorias == []:
            listaCategorias.append(producto['categoria'])
            
        if not (producto['categoria'] in listaCategorias):
            listaCategorias.append(producto['categoria'])

    listaCategorias.sort()

    while True:

        for categoria in listaCategorias:
            deco.decorarConCuadradoCh(categoria)

        seleccionDeCategoria = input("\nSeleccione una de las categorías anteriores: ").title()
        os.system("cls")
        deco.decorarConCuadrado(seleccionDeCategoria)

        deco.tablaCategoria()
        for producto in listaProductos:
            if seleccionDeCategoria.lower() == producto['categoria'.lower()]:
                print(f"│ {(producto['categoria']).title():<18}│ {(producto['producto']).title():<44}│")
                print("├───────────────────┼─────────────────────────────────────────────┤")

        # ------ Condicion para continuar ------ #
        seguir = input("\n¿Desea ver otra categoría? (SI/NO): ")
        seguir = seguir.upper()

        while seguir != "SI" and seguir != "NO":
            seguir = input("\n¿Desea ver otra categoría? (SI/NO): ")

        if seguir == "NO":
            os.system("cls")
            break

def staff():
    staff = ["Adrian Scianca","Alejandro Chifflets","Antonella Tigri","Augusto René Ajalla","Carlos Gomez","David Guillermo Cometto","Diego Luque","Eva Maria Villarreal","Gabriel Choque","Juan Manuel Pinto","Juan Pablo Lapachet","Magaly Magdalena Patiño","Mailén Jurado","Micaela Sosa","Octavio Luis Baratto","Renán Medina","Yael Rodriguez"]
    print("\n                GESTIÓN DE PRODUCTOS - CaC 2023")
    print("""
                             \|||/
                             (o o)
    ----------------------ooO-(_)-Ooo-----------------------
    ###############      STAFF Grupo "B"     ###############
    ########################################################""")

    for user in staff:
        print(f"    *** {user:^48} ***")
    print("    ########################################################")
    print("\nPresione [ENTER] para salir")
    input("")
    os.system("cls")