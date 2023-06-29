import json

def menuIngreso():            
    print('''
    ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                               ░░░▒▒▒▓▓▓ SISTEMA DE GESTION DE STOCK GC23450 ▓▓▓▒▒▒░░░                           ║  
    ╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
    ║                                                   ¡Bienvenido!                                                  ║
    ║─────────────────────────────────────────────────────────────────────────────────────────────────────────────────║
    ║ 1. Ingreso por primera vez.                                                                                     ║
    ║ 2. Log In                                                                                                       ║
    ║ 0. Salir                                                                                                        ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    ''')

def menuPrincipal():         
    print('''
    ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                               ░░░▒▒▒▓▓▓ SISTEMA DE GESTION DE STOCK GC23450 ▓▓▓▒▒▒░░░                           ║  
    ╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
    ║ 1. Gestion de productos.                                                                                        ║
    ║ 2. Reportes.                                                                                                    ║
    ║ 0. Log out / Cambiar usuario                                                                                    ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    ''')

def menuGestion():         
    print('''
    ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                               ░░░▒▒▒▓▓▓ SISTEMA DE GESTION DE STOCK GC23450 ▓▓▓▒▒▒░░░                           ║  
    ╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
    ║ 1. Ingresar nuevo producto.                                                                                     ║
    ║ 2. Listado de productos.                                                                                        ║
    ║ 3. Modificar un producto.                                                                                       ║
    ║ 4. Eliminar un producto.                                                                                        ║
    ║ 0. Volver al menu principal.                                                                                    ║ 
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    ''')    

def menuReportes():         
    print('''
    ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                               ░░░▒▒▒▓▓▓ SISTEMA DE GESTION DE STOCK GC23450 ▓▓▓▒▒▒░░░                           ║  
    ╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
    ║ 1. Mostrar productos nacionales.                                                                                ║
    ║ 2. Mostrar productos importados.                                                                                ║
    ║ 3. Mostrar stock de productos en orden alfabetico.                                                              ║
    ║ 4. Mostrar productos por categoria.                                                                             ║
    ║ 0. Volver al menu principal.                                                                                    ║ 
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    ''')    

def tabla():                  # Esta tabla se utilizara para los listados de reportes
   print('╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗')
   print('║                               ░░░▒▒▒▓▓▓ SISTEMA DE GESTION DE STOCK GC23450 ▓▓▓▒▒▒░░░                           ║')
   print('╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣')
   print('║ Producto                                    │ Codigo    │ Categoria          │ Stock     │ Origen               ║')
   print('║─────────────────────────────────────────────┼───────────┼────────────────────┼───────────┼──────────────────────║')

def decorar(titulo):  # decora con bolitas negras
    print("•"*30)
    print(titulo)
    print("•"*30)
def decorarDos(titulo): # decora con bolitas vacias
    print("o"*30)
    print(titulo)
    print("o"*30)
def decorarTres(titulo): # decora con bolitas negras sin repetir
    print("•"*30)
    print(titulo)

def altaProducto(productos): 
    while True:
        print('''
        ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                               ░░░▒▒▒▓▓▓ SISTEMA DE GESTION DE STOCK GC23450 ▓▓▓▒▒▒░░░                           ║  
        ╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║ Tipo de producto             │  Descripcion                                                                     ║
        ║──────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────║
        ║ 1. Cocina                    │  Utensillos para cocinar, vajilla, cubiertos, etc.                               ║
        ║ 2. Decoracion                │  Relojes, cuadros, imanes, carteles, accesorios, etc.                            ║
        ║ 3. Baño (banio)              │  Accesorios para el baño, jaboneras, cortinas, dispensers de jabon, etc.         ║
        ║ 4. Electrodomestico          │  Batidoras, cafeteras, minipimers, hervidoras, wafleras, tostadoras, etc.        ║
        ║ 5. Reposteria                │  Torteras, budineras, moldes varios, mangas, etc.                                ║
        ║ 0. Cancelar                                                                                                     ║
        ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
        
        decorar("Ingreso de nuevo producto") 
        print('')
        try:
            opcProd = int(input("Ingresa la categoria del producto: "))
        
            if opcProd == 0:
                print('Operacion cancelada.')
                break
            
            elif opcProd == 1:
                acumulaCodigo = 1000
                codigoProducto = 0
                tipoProducto = "cocina"
                for producto in productos:
                    while producto["Categoria"] == "cocina" and producto["Codigo"] == acumulaCodigo:
                        acumulaCodigo += 1
                codigoProducto = acumulaCodigo

            elif opcProd == 2:
                acumulaCodigo = 2000
                codigoProducto = 0
                tipoProducto = "decoracion"
                for producto in productos:
                    while producto["Categoria"] == "decoracion" and producto["Codigo"] == acumulaCodigo:
                        acumulaCodigo += 1
                codigoProducto = acumulaCodigo

            elif opcProd == 3:
                acumulaCodigo = 3000
                codigoProducto = 0
                tipoProducto = "banio"
                for producto in productos:
                    while producto["Categoria"] == "banio" and producto["Codigo"] == acumulaCodigo:
                        acumulaCodigo += 1
                codigoProducto = acumulaCodigo

            elif opcProd == 4:
                acumulaCodigo = 4000
                codigoProducto = 0
                tipoProducto = "electro"
                for producto in productos:
                    while producto["Categoria"] == "electro" and producto["Codigo"] == acumulaCodigo:
                        acumulaCodigo += 1
                codigoProducto = acumulaCodigo

            elif opcProd == 5:
                acumulaCodigo = 5000
                codigoProducto = 0
                tipoProducto = "reposteria"
                for producto in productos:
                    while producto["Categoria"] == "reposteria" and producto["Codigo"] == acumulaCodigo:
                        acumulaCodigo += 1
                codigoProducto = acumulaCodigo

            else:
                print('Opcion no valida. Por favor reintente.')
                continue
        except ValueError:
            print('La opcion debe ser numerica. Por favor, reintente.')
            continue

        codigo = codigoProducto
        categoria = tipoProducto
        nombre = input("Ingresa el nombre del producto: ")
        origen = input("Ingrese pais de origen del producto: ").casefold()
        
        while True:
            try:
                stock = int(input("Ingrese stock del producto: "))
                break
            except ValueError:
                print("El stock debe ser un entero. Por favor, reintente.")
        producto = {
            "Codigo":codigo,
            "Nombre":nombre.casefold(),
            "Categoria":categoria.casefold(),
            "Stock":stock, 
            "Origen":origen
        }
        productos.append(producto)
        arch = open("productos.json","w")
        json.dump(productos,arch,indent=2)
        arch.close()
        
        nuevoProd = input("¿Desea agregar otro producto? (s/n): ")
        if nuevoProd in "sS":
            continue
        else:
            break

def eliminarProducto(listado,borrar):
    decorar("Eliminando producto...")
    listado.remove(borrar)
    arch = open("personas.json","w")
    json.dump(listado,arch,indent=2)
    arch.close()
    print('')
    decorarDos("El producto fue eliminado con exito.")

def modificarProducto(listado,elemento): 
    decorar(f"Modificando {elemento}")
    while True:
        print('')
        nuevoNom = input(f'El nombre que tiene actualmente es {elemento["Nombre"]}. Ingrese nuevo nombre de producto: ')
        while True:
            try:
                nuevoStock = int(input(f'El stock que tiene actualmente es {elemento["Stock"]}. Ingrese nueva cantidad de stock: '))
                break
            except:
                print('El stock debe ser numerico. Por favor reintente.')
                continue
        
        nuevoOrigen =  input(f'El origen que tiene actualmente es {elemento["Origen"]}. Ingrese nuevo origen: ')

        elemento["Nombre"] = nuevoNom
        elemento["Stock"] = nuevoStock
        elemento["Origen"] = nuevoOrigen
        
        arch = open("productos.json","w")
        json.dump(listado,arch,indent=2)
        arch.close()
        break

def altaUsuario(listado): 
    while True:
        decorar("Primer ingreso")
        try:
            dniNuevo = int(input("Ingresa tu DNI como usuario (presione 0 para cancelar): "))
        
        except ValueError:
            print('El DNI debe ser numerico. Por favor reintente.')
            continue
        
        if dniNuevo == 0:
                break

        claveNueva = input("Ingresa una clave de 4 numeros (presione 0 para cancelar): ")
        if claveNueva == '0':
            break

        if len(claveNueva) != 4:
            print('La clave debe ser de 4 numeros. Por favor, reintente.')
        else:
            try:
                int(claveNueva)
                break        
            except ValueError:
                print('La clave debe ser de 4 numeros. Por favor, reintente.')
                continue
    
        usuarioNuevo = {
            "Usuario":dniNuevo,
            "Clave":claveNueva,
        }
        
        listado.append(usuarioNuevo)
        arch = open("usuarios.json","w")
        json.dump(listado,arch,indent=2)
        arch.close()
