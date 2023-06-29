import os
import deco
import json
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#-------- Para simplificar que las opciones ingresadas sean correctas-------------#
def WhileCondosDecisiones(opcion1,opcion2,leyenda,LeyendaError = "Opción incorrecta"):
    variable = input(f"{leyenda}").upper()
    while variable != opcion1 and variable != opcion2:
        print(LeyendaError)
        variable = input(f"{leyenda}").upper()
    return variable

def EliminarProducto(productos):
    while True:
        contadorParaEliminarProducto = -1       #Para saber el índice del producto que tengo que eliminar
        deco.tablaProductos(productos)
        print("\nIngrese el código del producto que desea eliminar ([0] para volver al menú): ")
        buscarEliminar = input("").upper()
        if buscarEliminar == "0":
            os.system("cls")
            break

        for producto in productos:
            contadorParaEliminarProducto += 1
            if producto["codigo"] == buscarEliminar:

                # Nos aseguramos que el usuario no se equivoco de producto
                BanderaEliminarProducto = WhileCondosDecisiones("SI","NO",f"¿Está seguro que desea eliminar este producto {(producto['producto']).title()}? (SI/NO): ")
                print("-"*40)
                if BanderaEliminarProducto =="SI":
                        productos.pop(contadorParaEliminarProducto)
                        print("-"* 40)
                        print(f"          El producto: {(producto['producto']).title()} ha sido eliminado de la lista")
                        print("-"* 40)
                        listaP = open("ProductosAlmacen.json", "w")
                        json.dump(productos, listaP, indent=2)
                        listaP.close()
                        break

                elif BanderaEliminarProducto =="NO":
                    break
        else:
                print("-"*40)
                print("Código no encontrado")
                print("-"*40)

        # Por si el usurio quiere eliminar otro producto
        seguirEliminarProducto = WhileCondosDecisiones("SI","NO","¿Desea eliminar otro producto? (SI/NO): ")

        if seguirEliminarProducto == "NO":
                break
            
def codigo(frase="Ingrese código del producto, el código debe tener el formato 'A0000' ([0] para volver al menú): "):
    productos = open("ProductosAlmacen.json", "r")
    lista = json.load(productos)
    productos.close()
    while True:
        codigo = input(frase).upper()

        # ------ Salida ------ #
        if codigo == "0":
            os.system("cls")
            break
        # ------ Fase de verificacion ------ #
        if len(codigo) < 5:
            print("Código muy corto, debe tener el formato 'A0000'")
            continue
        elif codigo[0] not in abecedario:
            print("El primer caracter tiene que ser una letra")
            continue
        elif len(codigo) > 5:
            print("El código debe de tener el formato 'A0000' ")
            continue
        try:
            int(codigo[1:])
        except:
            print("Los cuatro últimos caracteres deben de ser numeros")
            continue
        
        while True:
            for producto in lista:
                if codigo == producto["codigo"]:
                        print("El código seleccionado ya existe. Por favor ingrese otro código o ingrese en modificar.")
                        codigo = input("Ingrese código del producto: ").upper()
                        break
            else:
                break
        if codigo != producto["codigo"]:
             break
    return codigo
            
def agregarProducto(lista):
    while True:
        # ------ Agregado del nuevo producto ------ #
        while True:
            codNuevo = codigo("\nIngrese el código nuevo: ")
            if codNuevo == "0":
                print("El código no puede ser (0)")
            else:
                print("Código generado")
                break
        producto = input("\nIndique un producto: ") # bebida sin alcohol "Gaseosa"

        while True:
            try:
                cantidad = int(input("\nIngrese una cantidad: ")) # 50
                break
            except:
                   print("¡La cantidad debe ser un número entero!".upper())
        categoria = input("\nIngrese una categoría: ") # "Coca"
        precio = float(input("\nIngrese un precio: ")) # 50
        nuevoProducto = {"producto": producto, 
                            "categoria":categoria,
                            "codigo":codNuevo,
                            "cant":cantidad,
                            "precio":precio}
        lista.append(nuevoProducto)
        deco.tablaCompleta()
        cant = str(nuevoProducto['cant'])
        prec = str(nuevoProducto['precio'])
        print(f"│{nuevoProducto['codigo']:^8}│ {(nuevoProducto['producto']).title():<44}│ {(nuevoProducto['categoria']).title():<18}│{cant:^10}│${prec:^11}│")
        print("└────────┴─────────────────────────────────────────────┴───────────────────┴──────────┴────────────┘")


        Productos = open("ProductosAlmacen.json","w")
        json.dump(lista,Productos, indent= 2)
        Productos.close()
        # ------ Condicion para continuar ------ #
        seguir = input("¿Desea agregar otro producto? (SI/NO): ")
        seguir = seguir.upper()

        while seguir != "SI" and seguir != "NO":
            seguir = input("¿Desea agregar otro producto? (SI/NO): ")

        if seguir == "NO":
            break

def ModificarProducto(lista):
    codigoOp = input("\nCódigo del producto a modificar([ENTER] para volver al menu): ").title()
    for productoMod in lista:
        if productoMod == "":
            break

        if productoMod['codigo'] == codigoOp:
            deco.tablaCompleta()
            cant = str(productoMod['cant'])
            prec = str(productoMod['precio'])
            print(f"│{productoMod['codigo']:^8}│ {(productoMod['producto']).title():<44}│ {(productoMod['categoria']).title():<18}│{cant:^10}│${prec:^11}│")
            print("└────────┴─────────────────────────────────────────────┴───────────────────┴──────────┴────────────┘")
            
            print("\nEscriba el nuevo nombre o presione [ENTER] para NO modificar\n")
            producto = input(f"Producto Actual ({productoMod['producto']}): ")
            if producto == "":
                producto = productoMod['producto']
            print("\nEscriba nueva categoría o presione [ENTER] para NO modificar\n")
            categoria = input(f"Categoria Actual ({productoMod['categoria']}): ")
            if categoria == "":
                categoria = productoMod['categoria']
            print("\nEscriba nueva cantidad o presione [ENTER] para NO modificar\n")
            cantidad = input(f"Cantidad Actual ({productoMod['cant']}): ")
            if cantidad == "":
                cantidad = productoMod['cant']
            print("\nEscriba nuevo precio o presione [ENTER] para NO modificar\n")
            precio = input(f"Precio Actual (${productoMod['precio']}): ")
            if precio == "":
                precio = productoMod['precio']
            cambiaCod = input(f"\nCódigo Actual ({productoMod['codigo']}). ¿Desea Cambiarlo? (SI/NO): ").upper()

            productoMod['producto'] = producto
            productoMod['categoria'] = categoria
            if cambiaCod == "SI":
                codNuevo = codigo("Ingrese el código: ")
                if codNuevo == "0":
                     productoMod['codigo'] = productoMod['codigo']
                else:
                     productoMod['codigo'] = codNuevo
            else:
                productoMod['codigo'] = productoMod['codigo']
                
            productoMod['cant'] = int(cantidad)
            productoMod['precio'] = float(precio)

            Productos = open("ProductosAlmacen.json","w")
            json.dump(lista,Productos, indent= 2)
            Productos.close()
            break            
    else:
        print()
        print(f"{codigoOp} no fue encontrado en los Productos")