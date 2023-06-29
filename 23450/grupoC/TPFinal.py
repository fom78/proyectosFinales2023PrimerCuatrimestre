import json
import moduloTPF as m

file1 = open("usuarios.json","r")
usuarios = json.load(file1)
file1.close()

file2 = open("productos.json","r")
productos = json.load(file2)
file2.close()

errorValor = "La opcion ingresada debe ser un numero. Por favor reintente."

while True:
    m.menuIngreso()
      
    try:
        opcionIngreso=int(input("Seleccione 1 si es su primer ingreso o 2 para loguearse: "))
        
        if opcionIngreso==0:
            print('')
            print("Usted ha salido del sistema, muchas gracias!")
            break
        
        elif opcionIngreso==1:
            m.altaUsuario(usuarios)
        
        elif opcionIngreso==2:
            print('')
            dni = int(input("Ingresa tu DNI: "))
            print('')
            clave = int(input("Ingresa su clave de 4 digitos: "))
            
            for usuario in usuarios:            
                if (usuario["Usuario"]==dni and usuario["Clave"]==clave):
                    m.decorar("Bienvenido al sistema")
                    
                    while True:
                        m.menuPrincipal()
                        try:
                            opcion = input("Ingrese opcion: ")
                            
                            if opcion == "0":
                                print("Usted ha salido del sistema, muchas gracias!")
                                break
                            
                            elif opcion == "1":
                                while True:
                                    m.menuGestion()
                                    try:
                                        opcionDos=input("Ingrese una opcion del Menu: ")
                                        
                                        if opcionDos=="1":
                                            m.altaProducto(productos)
                                        
                                        elif opcionDos=="2":
                                            m.decorar("Listado de productos actual")
                                            for producto in productos:
                                                print(producto)
                                        
                                        elif opcionDos=="3":
                                            while True:
                                                print('')
                                                print('¡¡Atencion!! No es posible cambiar el codigo o tipo de producto.')
                                                print('Si estos datos son incorrectos, debe borrar el producto y crear uno nuevo.')
                                                print('')
                                                print('¿Como desea buscar el producto a modificar?')
                                                print('1. Por codigo de producto')
                                                print('2. Por nombre de producto')
                                                print('0. Cancelar')
                                                print('')
                                                
                                                try:
                                                    opcModif = int(input('Su opcion: '))
                                                    
                                                    if opcModif == 0:
                                                        print('Operacion cancelada.')
                                                        break
                                                    
                                                    elif opcModif == 1:     # Con esta opcion, se busca el producto a modificar con el codigo de producto.
                                                        prodBuscar = int(input('Ingrese codigo de producto: '))
                                                        for producto in productos: 
                                                            if prodBuscar == producto["Codigo"]:
                                                                check = input((f'Se procede modificar a {producto["Nombre"]}, cuyo codigo es {producto["Codigo"]}. ¿Esta seguro? (s/n) '))
                                                                if check in "Ss":
                                                                    m.modificarProducto(productos,producto)
                                                                    break
                                                                else:
                                                                    print('Operacion cancelada.')
                                                                break

                                                        else:
                                                            print('Producto no hallado. Por favor reintente.')
                                                            continue
                                                        break

                                                    elif opcModif == 2:   # Con esta opcion, se busca el producto a modificar con el nombre de producto.
                                                        prodBuscar = input('Ingrese nombre de producto: ')
                                                        for producto in productos: 
                                                            if prodBuscar in producto["Nombre"]:
                                                                check = input((f'Se procede modificar a {producto["Nombre"]}. ¿Esta seguro? (s/n) '))
                                                                if check in "Ss":
                                                                    m.modificarProducto(productos,producto)
                                                                    break
                                                                else:
                                                                    print('Operacion cancelada.')
                                                                break
                                                            
                                                        else:
                                                            print('Producto no hallado. Por favor reintente.')
                                                            continue
                                                        break

                                                except:
                                                    print(errorValor)
                                                    continue
                                                
                                                try:
                                                    codigo = input("Ingrese el codigo del producto: ")
                                                    for prod in productos:
                                                        if codigo == prod["Codigo"]: 
                                                            m.modificarProducto(productos,prod)
                                                            break
                                                    else:
                                                        print("El codigo no existe")
                                                        continue

                                                except:
                                                    print(errorValor)
                                                    continue
                                        
                                        elif opcionDos=="4":
                                            while True:
                                                print('')
                                                print('¿Como desea buscar el producto a borrar?')
                                                print('1. Por codigo de producto')
                                                print('2. Por nombre de producto')
                                                print('0. Cancelar')
                                                print('')
                                                
                                                try:
                                                    opcBorr = int(input('Su opcion: '))
                                                    
                                                    if opcBorr == 0:
                                                        print('Operacion cancelada.')
                                                        break
                                                    
                                                    elif opcBorr == 1:     # Con esta opcion, se busca el producto a borrar con el codigo de producto.
                                                        prodBuscar = int(input('Ingrese codigo de producto: '))
                                                        for producto in productos: 
                                                            if prodBuscar == producto["Codigo"]:
                                                                check = input((f'Se procede elimnar a {producto["Nombre"]}, cuyo codigo es {producto["Codigo"]}. ¿Esta seguro? (s/n) '))
                                                                if check in "Ss":
                                                                    m.eliminarProducto(productos, producto)
                                                                    break
                                                                else:
                                                                    print('Operacion cancelada.')
                                                                    break

                                                        else:
                                                                print('Producto no hallado. Por favor reintente.')
                                                                continue
                                                        break

                                                    elif opcBorr == 2:   # Con esta opcion, se busca el producto a eliminar con el nombre de producto.
                                                        prodBuscar = input('Ingrese nombre de producto: ')
                                                        for producto in productos: 
                                                            if prodBuscar in producto["Nombre"]:
                                                                check = input((f'Se procede eliminar a {producto["Nombre"]}. ¿Esta seguro? (s/n) '))
                                                                if check in "Ss":
                                                                    m.eliminarProducto(productos,producto)
                                                                    break
                                                                else:
                                                                    print('Operacion cancelada.')
                                                                    break
                                                            
                                                        else:
                                                            print('Producto no hallado. Por favor reintente.')
                                                            continue
                                                        break

                                                except:
                                                    print(errorValor)
                                                    continue

                                        elif opcionDos=="0":
                                            m.decorar("Volviendo al menu anterior...")
                                            break
                                    except:
                                        print(errorValor)
                                        continue
                                          
                            
                            elif opcion == "2":
                                while True:
                                    m.menuReportes()
                                    try:
                                        opcionTres=input("Ingrese una opcion del Menu: ")
                                        
                                        if opcionTres=="0":
                                            m.decorar("Volviendo al menu anterior...")
                                            break
                                        if opcionTres=="1":
                                            cant=0
                                            m.tabla()
                                            for producto in productos:
                                                pais="Argentina"
                                                if producto["Origen"].casefold() == pais.casefold():
                                                    cant+=1
                                                    print(f"║ {producto['Nombre'].casefold():<44}│ {producto['Codigo']:<10}│ {producto['Categoria']:<19}│ {producto['Stock']:<10}│ {producto['Origen'].casefold():<21}║")
                                            print('╚', end='')
                                            print('═'*113, end='')
                                            print('╝')
                                            print('')      
                                            m.decorar(f"Hay {cant} tipo/s de producto/s de origen nacional en stock.")        
                                            continue
                                        
                                        elif opcionTres=="2":
                                            cant=0
                                            m.tabla()
                                            for producto in productos:
                                                if producto["Origen"].casefold() != "Argentina".casefold():
                                                    cant+=1
                                                    print(f"║ {producto['Nombre'].casefold():<44}│ {producto['Codigo']:<10}│ {producto['Categoria'].casefold():<19}│ {producto['Stock']:<10}│ {producto['Origen'].casefold():<21}║")
                                            print('╚', end='')
                                            print('═'*113, end='')
                                            print('╝')
                                            print('')      
                                            m.decorar(f"Hay {cant} tipo/s de producto/s de origen importado en stock")
                                            continue
                                        
                                        elif opcionTres=="3":
                                            ordenados=sorted(productos,key=lambda o:o["Stock"])
                                            for producto in ordenados:
                                                m.decorarTres(f"Hay {producto['Stock']} unidades en stock de {producto['Nombre'].upper()}")
                                            continue
                                        
                                        elif opcionTres=="4":
                                            print('''
                                                •	Cocina
                                                •	Banio
                                                •	Decoracion
                                                •	Electrodomestico
                                                •	Reposteria
                                                ''')
                                            categ = input("Ingrese la categoria a filtrar: ")
                                            m.tabla()
                                            for producto in productos:
                                                if producto["Categoria"].upper() == categ.upper():
                                                    print(f"║ {producto['Nombre'].casefold():<44}│ {producto['Codigo']:<10}│ {producto['Categoria'].casefold():<19}│ {producto['Stock']:<10}│ {producto['Origen'].casefold():<21}║")
                                            print('╚', end='')
                                            print('═'*113, end='')
                                            print('╝')
                                            print('')
                                            continue
                                    except:
                                        print(errorValor)

                        except:
                            print(errorValor)
                            continue            
                
            else:
                print('')
                print("      :(           ")
                print("El usuario ingresado no esta en la base")
                print('')
                continue
    
    except:
        print(errorValor)
        continue




