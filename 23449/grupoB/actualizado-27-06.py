import json
import os

print (__file__)
dirdetrabajo = os.path.dirname(__file__)
os.chdir(dirdetrabajo)

#Utilizando JSON, creamos la lista de productos disponibles a partir de los datos existentes en un archivo .json
with open ('./stock.json','r',encoding='UTF-8') as file:
    productos = json.load(file)

#Creamos la variable del usuario que conserva si es un usuario administrador o no, su nombre de usuario y su correo.
sesion_iniciada = False
sesion_administrador = False
sesion_username = ""
sesion_mail = ""

#Creamos la variable del carrito, que sera utilizada si el usuario inicia sesion y le agrega productos.
carrito= []

#Creamos la clase que servira para construir nuevos productos:
class constructor_producto:
    def __init__(self,codigo, nombre, precio, esNacional, stock, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.esNacional = esNacional
        self.stock = stock
        self.categoria = categoria
    def a_diccionario(self):
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'precio': self.precio,
            'esNacional': self.esNacional,
            'stock': self.stock,
            'categoria': self.categoria
        }

#Creamos una funcion que limpie la consola del usuario cuando es necesario.
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#Creamos la funcion que corresponde al menu principal. Desde aqui, derivaremos al usuario segun si entra como invitado o como usuario registrado.
def menu_principal():
    marco = ' '*20 +'#'*20
    print(marco)
    print(' '*19,f'#{"Menú Principal":^18s}#')
    print(marco)
    print('''
    [1] Continuar como invitado.
    [2] Iniciar sesión.
    [3] Crear un nuevo usuario.
    [0] Salir
    ''')
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        menu_invitado()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        crear_usuario()
    elif opcion == '0':
        print('Gracias por usar nuestro app. ¡Adiós!')
        return
    else:
        limpiarPantalla()
        print(f"'{opcion}' no es una opción válida. Por favor, ingrese una opción válida.")
        menu_principal()

#Creamos la funcion que correspondera al usuario invitado, este solamente podra acceder a la visualizacion de los productos.
def menu_invitado():
    marco = ' '*20 +'#'*20
    print(marco)
    print(' '*19,f'#{"Menú Invitado":^18s}#')
    print(marco)
    print('''
    [1] Ver productos disponibles.
    [0] Salir
    ''')
    opcion = input("Elija una opción: ")
    if opcion == '1':
        limpiarPantalla()
        menu_reportes(menu_invitado)
    elif opcion == '0':
        print('Gracias por usar nuestro app. ¡Adiós!')
        return
    else:
        limpiarPantalla()
        print(f"'{opcion}' no es una opción válida. Por favor, ingrese una opción válida.")
        menu_invitado()

#Creamos la funcion que correspondera al usuario registrado. Este, ademas de visualizar los productos, podra armar un carrito y comprarlo, pero no modificar los productos directamente.
def menu_usuario():
    marco = ' '*20 +'#'*20
    print(marco)
    print(' '*19,f'#{"Menú Usuario":^18s}#')
    print(marco)
    print('''
    [1] Ver productos disponibles.
    [2] Realizar su compra.
    [0] Salir
    ''')
    opcion = input("Elija una opción: ")
    if opcion == '1':
        limpiarPantalla()
        menu_reportes(menu_usuario)
    elif opcion == '2':
        limpiarPantalla()
        menu_carrito()	 
    elif opcion == '0':
        print('Gracias por usar nuestro app. ¡Adiós!')
        return
    else:
        limpiarPantalla()
        print(f"'{opcion}' no es una opción válida. Por favor, ingrese una opción válida.")
        menu_usuario()
        
#Creamos la funcion que corresponde al menu de usuario administrador. Este, ademas de visualizar los productos, podra gestionar el stock y ver los carritos de las compras realizadas por otros usuarios.
def menu_administrador():
    marco = ' '*20 +'#'*20
    print(marco)
    print(' '*19,f'#{"Menú Administrador":^18s}#')
    print(marco)
    print('''
    [1] Ver productos disponibles.
    [2] Gestionar el Stock.
    [3] Ver Carritos Comprados.
    [0] Salir
    ''')
    opcion = input("Elija una opción: ")
    if opcion == '1':
        limpiarPantalla()
        menu_reportes(menu_administrador)
    elif opcion == '2':
        limpiarPantalla()
        menu_gestion_productos()
    elif opcion == '3':
        limpiarPantalla()
        mostrar_pedidos()	 
    elif opcion == '0':
        print('Gracias por usar nuestro app. ¡Adiós!')
        return
    else:
        limpiarPantalla()
        print(f"'{opcion}' no es una opción válida. Por favor, ingrese una opción válida.")
        menu_usuario()

#Creamos la funcion que corresponde al menu de reportes.
def menu_reportes(menu_anterior):
    marco = ' '*20 +'#'*20
    print(marco)
    print(' '*19,f'#{"Reporte":^18s}#')
    print(marco)
    print('''
    [1] Mostrar todos los productos.
    [2] Búsqueda de productos por nombre.
    [3] Mostrar productos nacionales.
    [4] Mostrar productos importados.
    [5] Mostrar productos según una cantidad.
    [6] Mostrar productos por categoría.
    [0] Volver al menú principal.
    ''')
    opcion = input("Elija una opción: ")
    if opcion == '1':
        limpiarPantalla()
        mostrar_stock(productos)
        menu_reportes(menu_anterior)
    elif opcion == '2':
        filtrar_productos_nombre(menu_anterior)
    elif opcion == '3':
        limpiarPantalla()
        print('''
<<<<<<<<<<<<<<<<< A continuación se mostrarán todos los productos de origen Nacional >>>>>>>>>>>>>>>>>>''')
        filtrar_productos_nacionalidad(True)
        menu_reportes(menu_anterior)
    elif opcion == '4':
        limpiarPantalla()
        print('''
<<<<<<<<<<<<<<<<< A continuación se mostrarán todos los productos de origen Importado >>>>>>>>>>>>>>>>>>''')
        filtrar_productos_nacionalidad(False)
        menu_reportes(menu_anterior)
    elif opcion == '5':
        limpiarPantalla()
        filtrar_productos_cantidad(productos,menu_anterior)
    elif opcion == '6':
        limpiarPantalla()
        filtrar_productos_categoria(productos,menu_anterior)
    elif opcion == '0':
        limpiarPantalla()
        menu_anterior()
    else:
        limpiarPantalla()
        print(f"'{opcion}' no es una opción válida. Por favor, ingrese una opción válida.")
        menu_reportes(menu_anterior)

#Creamos la funcion que corresponde al menu del carrito.
def menu_carrito():
    marco = ' '*20 +'#'*20
    print(marco)
    print(' '*19,f'#{"Menú Carrito":^18s}#')
    print(marco)
    print('''
    [1] Agregar producto al carrito.
    [2] Mostrar Productos del carrito.
    [3] Modificar cantidad de producto en el carrito.
    [4] Eliminar producto del carrito.
    [5] Realizar la compra.
    [0] Volver al menú anterior.
    ''')
    opcion = input("Elija una opción: ")
    if opcion == "1":
        limpiarPantalla()
        agregar_carrito()
    elif opcion == "2":
        limpiarPantalla()
        mostrar_carrito(carrito)
        menu_carrito()
    elif opcion == "3":
        limpiarPantalla()
        modificar_carrito()
    elif opcion == "4":
        limpiarPantalla()
        eliminar_carrito()
    elif opcion == "5":
        limpiarPantalla()
        comprar_carrito()
    elif opcion == "0":
        limpiarPantalla()
        menu_usuario()
    else:
        limpiarPantalla()
        print(f"'{opcion}' no es una opción válida. Por favor, ingrese una opción válida.")
        menu_carrito()

#Creamos la funcion que corresponde al menu de gestion de productos.
def menu_gestion_productos():
    marco = ' '*20 +'#'*20
    print(marco)
    print(' '*19,f'#{"Productos":^18s}#')
    print(marco)
    print('''
    [1] Ingresar nuevo producto.
    [2] Modificar un producto.
    [3] Eliminar un producto.
    [0] Volver al menú principal.
    ''')
    opcion = input("Elija una opción: ")
    if opcion == '1':
        limpiarPantalla()
        ingresar_producto()
    elif opcion == '2':
        limpiarPantalla()
        modificar_producto()
    elif opcion == '3':
        limpiarPantalla()
        eliminar_producto()
    elif opcion == '0':
        limpiarPantalla()
        menu_administrador()
    else:
        limpiarPantalla()
        print(f"'{opcion}' no es una opción válida. Por favor, ingrese una opción válida.")
        menu_gestion_productos()

#Creamos la funcion que permite al usuario ingresar un nuevo producto. Verifica que el codigo ingresado sea de formato correcto.
def ingresar_producto():
    codigo = verificar_codigo_producto()
    nombre = verificar_nombre_producto()
    precio = verificar_int_producto('precio')
    esNacional = verificar_nacionalidad_producto()
    stock = verificar_int_producto('stock')
    categoria = verificar_categoria_producto()
    nuevo_producto = constructor_producto(codigo, nombre, precio, esNacional, stock, categoria)
    nuevo_producto = nuevo_producto.a_diccionario()
    productos.append(nuevo_producto)
    with open ('./stock.json','w',encoding='UTF-8') as file:
        json.dump(productos, file,indent=4) 
    print("\t<<<<<<<<<<<<<<<<<Carga exitosa>>>>>>>>>>>>>>>>>>")
    otraVez  = input('¿Quieres ingresar otro producto? S/N: ').lower()
    if otraVez == 'n':
        limpiarPantalla()
        menu_gestion_productos()
    else:
        print(' ')
        ingresar_producto()

#Creamos las funciones que permitiran verificar los diferentes valores que se asignaran al producto.
def verificar_codigo_producto():
    codigo = input("Ingrese el código del producto que desea agregar: ").upper()
    if len(codigo) != 4 or not codigo[0].isupper() or not codigo[1].isdigit() or not codigo[2].isdigit() or not codigo[3].isdigit():
        print('El formato del código no es el correcto. Por favor, ingrese el código con el formato "A999".')
        return verificar_codigo_producto()
    else:
        for producto in productos:
            if producto["codigo"] == codigo:
                print("El código ya existe. Por favor, ingrese un nuevo código.")
                return verificar_codigo_producto()
        return codigo

def verificar_nombre_producto():
    nombre = input("Ingrese el nombre del producto: ")
    if len(nombre) <= 0:
        print('Por favor, ingrese un nombre válido.')
        return verificar_nombre_producto()
    else:
        for producto in productos:
            if producto["nombre"] == nombre:
                print("Ya existe un producto bajo el mismo nombre. Por favor, ingrese un nuevo nombre.")
                return verificar_nombre_producto()
        return nombre

def verificar_int_producto(param):
    numero = input(f"Ingrese el {param} del producto: ")
    try:
        numero = int(numero)
        return numero
    except ValueError:
        print(f'Por favor, ingrese un {param} válido.')
        return verificar_int_producto(param)

def verificar_nacionalidad_producto():
    esNacional = input("¿El producto es Nacional? S/N: ").lower()
    if esNacional == 's':
        return True
    elif esNacional == 'n':
        return False
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
        return verificar_nacionalidad_producto()
    
def verificar_categoria_producto () :
    print('¿A qué categoría corresponde el producto?')
    print('''
    [1] Construcción.
    [2] Ferretería.
    [3] Electricidad.
    [4] Herramientas
    ''')
    categoria = input("Ingrese la categoria a la que corresponde el producto: ")
    if categoria == '1':
        categoria = 'Construccion'
        return categoria
    elif categoria == '2':
        categoria = 'Ferreteria'
        return categoria
    elif categoria == '3':
        categoria = 'Electricidad'
        return categoria
    elif categoria == '4':
        categoria = 'Herramientas'
        return categoria
    else:
        limpiarPantalla()
        print(f"'{categoria}' no es una opción válida. Por favor, ingrese una opción válida.")
        return verificar_categoria_producto()

#Creamos la funcion que permitira al usuario modificar los productos existentes.
def modificar_producto():
    mostrar_stock(productos)
    codigo = input("""  -- Ingrese 'x' para volver al menu anterior -- 
    Ingrese el código del producto que desea modificar: """).upper()   
    if codigo == 'X':
        limpiarPantalla()
        return menu_gestion_productos()
    elif len(codigo) != 4 or not codigo[0].isupper() or not codigo[1].isdigit() or not codigo[2].isdigit() or not codigo[3].isdigit():
        print('El formato del código no es el correcto. Por favor, ingrese el código con el formato EJEMPLO: A999.')
        print(' ')
        modificar_producto()
    else:
        producto_encontrado = None
        for producto in productos:
            if producto["codigo"] == codigo:
                producto_encontrado = producto
                break
        if producto_encontrado is None:
            print("El código de producto ingresado no es válido.")
            return modificar_producto()
        else:
            modificar_producto_submenu(producto_encontrado)
            with open ('./stock.json','w',encoding='UTF-8') as file:
                json.dump(productos,file,indent=4)
            print('''
<<<<<<<<<<<<<<<<< El producto ha sido modificado correctamente. >>>>>>>>>>>>>>>>>>''')
            otraVez  = input('¿Quieres modificar otro producto? S/N: ').lower()
            if otraVez == 'n':
                limpiarPantalla()
                menu_gestion_productos()
            else:
                print(' ')
                modificar_producto()

#Creamos una funcion apra que modificar un atibuto no obligue al usuario a escribir reiteradamente el codigo
def modificar_producto_submenu(producto_encontrado):
    print(' ')
    print('¿Qué atributo desea modificar?')
    print('''
    [1] Codigo.
    [2] Nombre.
    [3] Precio.
    [4] Origen.
    [5] Stock.
    [6] Categoria.
    ''')
    atributo = input("Ingrese la opcion correspondiente al atributo que desea modificar: ")
    if atributo == '1':
        producto_encontrado['codigo'] = verificar_codigo_producto()
    elif atributo == '2':
        producto_encontrado['nombre'] = verificar_nombre_producto()
    elif atributo == '3':
        producto_encontrado['precio'] = verificar_int_producto('precio')
    elif atributo == '4':
        producto_encontrado['esNacional'] = verificar_nacionalidad_producto()
    elif atributo == '5':
        producto_encontrado['stock'] = verificar_int_producto('stock')
    elif atributo == '6':
        producto_encontrado['categoria'] = verificar_categoria_producto()
    else:
        print(f"'{atributo}' no es una opción válida. Por favor, ingrese una opción válida.")
        return modificar_producto_submenu(producto_encontrado)

#Creamos la funcion que permitira al usuario eliminar un producto existente.
def eliminar_producto():
    mostrar_stock(productos)
    producto_existente = False
    codigo = input("""  -- Ingrese 'x' para volver al menu anterior -- 
    Ingrese el código del producto que desea eliminar. Recuerde que esta accion no tiene vuelta atras: """).upper()
    if codigo == 'X':
        limpiarPantalla()
        return menu_gestion_productos()
    elif len(codigo) != 4 or not codigo[0].isupper() or not codigo[1].isdigit() or not codigo[2].isdigit() or not codigo[3].isdigit():
        print('El formato del código no es el correcto. Por favor, ingrese el código con el formato EJEMPLO: A999.')
        print(' ')
        return eliminar_producto()
    else:
        for producto in productos:
            if producto['codigo'] == codigo:
                confirmar = input(f'¿Realmente desea eliminar el producto {producto["nombre"]}? S/N: ').lower()
                if confirmar == 's':
                    productos.remove(producto)
                    producto_existente = True
                    with open ('./stock.json','w',encoding='UTF-8') as file:
                        json.dump(productos,file,indent=4)
                    break
                else:
                    return eliminar_producto()
    if producto_existente:
        print("""
<<<<<<<<<<<<<<<<<Producto eliminado correctamente.>>>>>>>>>>>>>>>>>>""")
    else :
        print("El código del producto no existe.")
    otraVez  = input('¿Quieres eliminar otro producto? S/N: ').lower()
    if otraVez == 'n':
        menu_gestion_productos()
    else:
        print(' ')
        eliminar_producto()

#Creamos una funcion que mostrara todos los productos en stock..
def mostrar_stock(lista):
    print("             ","="*126)
    print(f'                  {"Codigo":<7s}     {"Nombre del producto":<35s}     {"Precio":<10s}     {"Origen":<10s}     {"Stock Disponible":<16s}     {"Categoria":<15s}  ')
    print("             ","-"*126)
    for producto in lista:
        if (producto['esNacional']): 
            print(f'                  {producto["codigo"]:^7s}     {producto["nombre"]:<35s}     {producto["precio"]:<10.2f}     {"Nacional":<10s}     {producto["stock"]:<16d}     {producto["categoria"]:<15s}  ')
        else:
            print(f'                  {producto["codigo"]:^7s}     {producto["nombre"]:<35s}     {producto["precio"]:<10.2f}     {"Importado":<10s}     {producto["stock"]:<16d}     {producto["categoria"]:<15s}  ')
    print("             ","-"*126)

#Creamos la funcion que filtrara productos por su nombre, segun input del usuario.
def filtrar_productos_nombre(menu_anterior):
    resultados_busqueda = []
    buscar = input("""  -- Ingrese 'x' para volver al menu anterior -- 
    Ingrese el nombre  del producto que desea buscar: """).lower()
    if buscar == 'x':
        return menu_reportes(menu_anterior)
    else:
        for producto in productos:
            if buscar in producto['nombre'].lower():
                resultados_busqueda.append(producto)
        if len(resultados_busqueda) == 0 :
            print(f'El término "{buscar}" no arrojó resultados para su búsqueda.')
        else:
            mostrar_stock(resultados_busqueda)
        otraVez  = input('¿Desea realizar otra búsqueda? S/N: ').lower()
        if otraVez == 'n':
            return menu_reportes(menu_anterior)
        else:
            print(' ')
            filtrar_productos_nombre(menu_anterior)

#Creamos la funcion que filtrara productos segun su nacionalidad, que sera pasada como un parametro de valor booleano.
def filtrar_productos_nacionalidad(valor):
    print("             ","="*111)
    print(f'                  {"Codigo":<7s}     {"Nombre del producto":<35s}     {"Precio":<10s}     {"Stock Disponible":<16s}     {"Categoria":<15s}  ')
    print("             ","-"*111)
    for producto in productos: 
        if producto['esNacional'] == valor:
            print(f'                  {producto["codigo"]:^7s}     {producto["nombre"]:<35s}     {producto["precio"]:^10.2f}     {producto["stock"]:^16d}     {producto["categoria"]:<15s}  ')
    print("             ","-"*111)

#Creamos la funcion que filtrara productos segun su cantidad.
def filtrar_productos_cantidad(lista,menu_anterior):
    cantidad_minima = int(input("Ingrese la cantidad mínima de stock que desea: "))
    cantidad_maxima = int(input("Ingrese la cantidad máxima de stock que desea: "))
    print("             ","="*126)
    print(f'                  {"Codigo":<7s}     {"Nombre del producto":<35s}     {"Precio":<10s}     {"Origen":<10s}     {"Stock Disponible":<16s}     {"Categoria":<15s}  ')
    print("             ","-"*126)
    for producto in lista:
        if cantidad_minima <= producto["stock"] and producto["stock"] <= cantidad_maxima:
            if (producto['esNacional']): 
                print(f'                  {producto["codigo"]:^7s}     {producto["nombre"]:<35s}     {producto["precio"]:<10.2f}     {"Nacional":<10s}     {producto["stock"]:<16d}     {producto["categoria"]:<15s}  ')
            else:
                print(f'                  {producto["codigo"]:^7s}     {producto["nombre"]:<35s}     {producto["precio"]:<10.2f}     {"Importado":<10s}     {producto["stock"]:<16d}     {producto["categoria"]:<15s}  ')
    print("             ","-"*126)
    otraVez  = input('¿Desea filtrar nuevamente los productos? S/N: ').lower()
    if otraVez == 'n':
        menu_reportes(menu_anterior)
    else:
        print(' ')
        filtrar_productos_cantidad(lista,menu_anterior)

#Creamos la funcion que filtrara productos segun su categoria.
def filtrar_productos_categoria(lista,menu_anterior):
    print('¿Qué categoría de productos desea visualizar?')
    print('''
    [1] Construcción.
    [2] Ferretería.
    [3] Electricidad.
    [4] Herramientas
    [0] Volver al Menú anterior.
    ''')
    categoria = input("Ingrese la categoria de productos que desea ver: ")
    if categoria == '0':
        return
    elif categoria == '1':
        categoria = 'Construccion'
    elif categoria == '2':
        categoria = 'Ferreteria'
    elif categoria == '3':
        categoria = 'Electricidad'
    elif categoria == '4':
        categoria = 'Herramientas'
    else:
        limpiarPantalla()
        print(f"'{categoria}' no es una opción válida. Por favor, ingrese una opción válida.")
        return filtrar_productos_categoria(lista)
    print("             ","="*126)
    print(f'                  {"Codigo":<7s}     {"Nombre del producto":<35s}     {"Precio":<10s}     {"Origen":<10s}     {"Stock Disponible":<16s}     {"Categoria":<15s}  ')
    print("             ","-"*126)
    for producto in lista:
        if producto["categoria"] == categoria:
            if (producto['esNacional']): 
                print(f'                  {producto["codigo"]:^7s}     {producto["nombre"]:<35s}     {producto["precio"]:<10.2f}     {"Nacional":<10s}     {producto["stock"]:<16d}     {producto["categoria"]:<15s}  ')
            else:
                print(f'                  {producto["codigo"]:^7s}     {producto["nombre"]:<35s}     {producto["precio"]:<10.2f}     {"Importado":<10s}     {producto["stock"]:<16d}     {producto["categoria"]:<15s}  ')
    print("             ","-"*126)
    otraVez  = input('¿Desea filtrar nuevamente los productos? S/N: ').lower()
    if otraVez == 'n':
        menu_reportes(menu_anterior)
    else:
        print(' ')
        filtrar_productos_categoria(lista,menu_anterior)

#Creamos una funcion que permita al usuario agregar productos al carrito.
def agregar_carrito ():
    mostrar_stock(productos)
    producto_carrito = {}
    codigo = input("""  -- Ingrese 'x' para volver al menu anterior -- 
    Ingrese el código del producto que desea agregar a su carrito: """).upper()   
    if codigo == 'X':
        limpiarPantalla()
        return menu_carrito()
    elif len(codigo) != 4 or not codigo[0].isupper() or not codigo[1].isdigit() or not codigo[2].isdigit() or not codigo[3].isdigit():
        print('El formato del código no es el correcto. Por favor, ingrese el código con el formato EJEMPLO: A999.')
        print(' ')
        agregar_carrito()
    else:
        for producto in productos:
            if producto['codigo'] == codigo:
                cantidad = verificar_disponibilidad(producto['stock'])
                producto_carrito = {
                    'codigo' : producto['codigo'],
                    'nombre' : producto['nombre'],
                    'precio' : producto['precio'],
                    'stock' : producto['stock'],
                    'cantidad' : cantidad
                }
                carrito.append(producto_carrito)
                break
    if producto_carrito:
        print("""
<<<<<<<<<<<<<<<<<Producto agregado al carrito correctamente.>>>>>>>>>>>>>>>>>>""")
    else :
        print("El código del producto no existe.")
    otraVez  = input('¿Quieres agregar otro producto a tu carrito? S/N: ').lower()
    if otraVez == 'n':
        menu_carrito()
    else:
        print(' ')
        agregar_carrito()

#Creamos una funcion que permita verificar que la cantidad solicitada de producto sea adecuada al stock disponible.
def verificar_disponibilidad(stock):
    cantidad = input('Por favor, ingrese la cantidad de unidades del producto que desea ingresar a su carrito: ')
    try:
        cantidad = int(cantidad)
        if cantidad > 0 and cantidad <= stock:
            return cantidad
        else:
            print('Por favor, ingrese una cantidad válida.')
            return verificar_disponibilidad(stock)
    except ValueError:
        print('Por favor, ingrese una cantidad válida.')
        return verificar_disponibilidad(stock)

#Creamos la funcion que nos muestre los productos que tenemos en el carrito
def mostrar_carrito (list):
    costo_total = 0
    print("             ","="*120)
    print(f'                  {"Codigo":<7s}     {"Nombre del producto":<35s}     {"Stock":<10s}     {"Precio":<10s}     {"Cantidad":<10s}     {"Subtotal":<15s}  ')
    print("             ","-"*120)
    for producto in list:
        subtotal = producto["precio"] * producto["cantidad"]
        costo_total = costo_total + subtotal
        print(f'                  {producto["codigo"]:^7s}     {producto["nombre"]:<35s}     {producto["stock"]:<10d}     {producto["precio"]:<10.2f}     {producto["cantidad"]:<10d}     {subtotal:>19.2f}')
    print("             ","-"*120)
    print("             ","TOTAL: ",f"{costo_total:>112.2f}")
    print("             ","="*120)

#Creamos la funcion que permita al usuario modificar las cantidades de los productos en el carrito.
def modificar_carrito():
    mostrar_carrito(carrito)
    codigo = input("""  -- Ingrese 'x' para volver al menu anterior -- 
    Ingrese el código del producto que desea modificar: """).upper()   
    if codigo == 'X':
        limpiarPantalla()
        return menu_carrito()
    elif len(codigo) != 4 or not codigo[0].isupper() or not codigo[1].isdigit() or not codigo[2].isdigit() or not codigo[3].isdigit():
        print('El formato del código no es el correcto. Por favor, ingrese el código con el formato EJEMPLO: A999.')
        return modificar_carrito()
    else:
        producto_encontrado = None
        for producto in carrito:
            if producto["codigo"] == codigo:
                producto_encontrado = producto
                break
        if producto_encontrado is None:
            print("El código de producto ingresado no es válido.")
            return modificar_carrito()
        else:
            nueva_cantidad = verificar_disponibilidad(producto_encontrado['stock'])
            producto_encontrado['cantidad'] = nueva_cantidad
    otraVez  = input('¿Quieres modificar otro producto? S/N: ').lower()
    if otraVez == 'n':
        limpiarPantalla()
        return menu_carrito()
    else:
        print(' ')
        return modificar_carrito()

#Creamos la funcion que permita al usuario eliminar un producto del carrito.
def eliminar_carrito():
    mostrar_carrito(carrito)
    producto_existente = False
    codigo = input("""  -- Ingrese 'x' para volver al menu anterior -- 
    Ingrese el código del producto que desea eliminar. Recuerde que esta accion no tiene vuelta atras: """).upper()
    if codigo == 'X':
        limpiarPantalla()
        return menu_carrito()
    else:
        for producto in carrito:
            if codigo == producto['codigo']:
                confirmar = input(f'¿Realmente desea eliminar el producto "{producto["nombre"]}" de su carrito? S/N: ').lower()
                if confirmar != 's': 
                    return eliminar_carrito()
                else:
                    carrito.remove(producto)
                    producto_existente = True
    if producto_existente:
        print("""
<<<<<<<<<<<<<<<<<Producto eliminado correctamente.>>>>>>>>>>>>>>>>>>""")
    else :
        print("El código del producto no existe.")
    otraVez  = input('¿Quieres eliminar otro producto? S/N: ').lower()
    if otraVez == 'n':
        menu_carrito()    
    else:
        eliminar_carrito()

#Creamos la funcion que permita al usuario realizar la compra y descontar las cantidades de cada producto del stock.
def comprar_carrito():
    for item in carrito:
        for producto in productos:
            if producto['codigo'] == item['codigo']:
                producto['stock'] = producto['stock'] - item['cantidad']
                break
    with open (r'stock.json','w',encoding='UTF-8') as file:
        json.dump(productos, file,indent=2) 
    nuevo_carrito = {
        "username": sesion_username,
        "mail" : sesion_mail,
        "productos": carrito}
    with open(r"pedidos.json", "r+",encoding='UTF-8') as file:
        compras = json.load(file)
        compras.append(nuevo_carrito)
        file.seek(0)
        file.write(json.dumps(compras, indent=4))
    print('''
<<<<<<<<<<<<<<<<<Se ha realizado la compra satisfactoriamente. En breves, recibira un correo con los datos de pago. Muchas gracias. >>>>>>>>>>>>>>>>>>
        ''')
    menu_usuario()

#Creamos la funcion que permita al usuario iniciar sesion.
def iniciar_sesion():
    global sesion_iniciada
    global sesion_administrador
    global sesion_username
    global sesion_mail
    
    with open (r"usuarios.json", "r")as file:
        usuarios = json.load(file)
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        
        for user in usuarios:
            if sesion_iniciada == False:
                if user["username"] == usuario and user["password"] == contraseña:
                    sesion_iniciada = True
                    sesion_username = user['username']
                    sesion_mail = user['mail']
                    if user['administrator'] == True:
                        sesion_administrador = True
        
        if sesion_iniciada == True:
            print(f'¡Bienvenido {sesion_username}!')
            if sesion_administrador == False:
                menu_usuario()
            else:
                menu_administrador()
        else:
            print("Alguno de los datos ingresados es incorrecto.")
            otraVez  = input('¿Desea intentarlo nuevamente? S/N: ').lower()
            if otraVez == 'n':
                menu_principal()
            else:
                iniciar_sesion()

#Creamos la funcion que permitira crear un nuevo usuario.
def crear_usuario():
    nuevo_usuario = {}
    print('''
    En primer lugar, ingrese su Nombre de Usuario. El mismo no debera existir en nuestra base de datos. No distingue entre mayusculas y minusculas.
            ''')
    username = verificar_username()
    print('''
    En segundo lugar, ingrese su mail. El mismo no debera existir en nuestra base de datos y debe tener un formato válido (incluir '@' y '.com'). No distingue entre mayúsculas y minúsculas.
        ''')
    mail = verificar_mail()    
    print('''
    En tercer lugar, ingrese su contraseña. La misma debe contar con al menos 8 caracteres, una mayúscula, una minúscula y un número.
    ''')
    contrasena = verificar_contrasena()
    nuevo_usuario = {
        "username" : username,
        "password" : contrasena,
        "mail" : mail,
        "administrator" : False
    }
    with open(r"usuarios.json", "r+",encoding='UTF-8') as file:
        usuarios = json.load(file)
        usuarios.append(nuevo_usuario)
        file.seek(0)
        file.write(json.dumps(usuarios, indent=4))
    print('''
El usuario ha sido creado exitosamente. Por favor, inicie sesion para confirmar el usuario.''')
    iniciar_sesion()

#Creamos las funciones que verificaran la existencia del nombre de usuario y del mail en la base de datos.
def verificar_username():
    with open (r"usuarios.json", "r") as file:
        usuarios = json.load(file)
        username = input('Nombre de Usuario deseado: ').lower()
        if len(username) == 0:
            print('Por favor, ingrese un nombre de usuario.')
            return verificar_username()
        else:
            for user in usuarios:
                if user["username"] == username:
                    print(f'El Nombre de Usuario "{username}" ya existe en nuestra base de datos. Por favor, ingrese un nombre de usuario válido.')
                    return verificar_username()
        return username

def verificar_mail():
    with open (r"usuarios.json", "r")as file:
        usuarios = json.load(file)
        mail = input('Su dirección de mail es: ').lower()
        if len(mail) < 8 or not '@' in mail or not '.com' in mail:
            print(f'El mail "{mail}" no tiene un formato válido.')
            return verificar_mail()
        else:
            for user in usuarios:
                if user["mail"] == mail:
                    print(f'El mail "{mail}" ya existe en nuestra base de datos. Por favor, ingrese otro mail.')
                    return verificar_mail()
        return mail

#Creamos la funcion que verifica la contrasena 
def verificar_contrasena():
    primera_contrasena = input('Nueva contraseña: ')
    contrasena_valida = False
    if len(primera_contrasena) < 8:
        print('La contraseña no tiene la longitud adecuada. Por favor, ingrese una contraseña válida.')
        return verificar_contrasena()
    for caracter in primera_contrasena:
        if caracter.isupper():
            contrasena_valida = True
            break
    if contrasena_valida == False:
        print('La contraseña no cumple con los requisitos. Por favor, ingrese una contraseña válida.')
        return verificar_contrasena()
    for caracter in primera_contrasena:
        contrasena_valida = False
        if caracter.islower():
            contrasena_valida = True
            break
    if contrasena_valida == False:
        print('La contraseña no cumple con los requisitos. Por favor, ingrese una contraseña válida.')
        return verificar_contrasena()
    for caracter in primera_contrasena:
        contrasena_valida = False
        if caracter.isdigit():
            contrasena_valida = True
            break
    if contrasena_valida == False:
        print('La contraseña no cumple con los requisitos. Por favor, ingrese una contraseña válida.')
        return verificar_contrasena()
    else:
        print('''
    Por favor, confirme su contraseña ingresándola nuevamente.
    ''')
        segunda_contrasena = input('Ingrese nuevamente su contrasena: ')
        if segunda_contrasena != primera_contrasena:
            print('Las contraseñas no coinciden. Por favor, ingrese la contraseña nuevamente.')
            return verificar_contrasena()
        return primera_contrasena

#Creamos la funcion que mostrara los presupuestos a enviar y permitira al usuario eliminar aquellos que ya ha respondido.
def mostrar_pedidos ():
    with open (r'pedidos.json','r',encoding='UTF-8') as file:
        pedidos = json.load(file)
    if len(pedidos) == 0:
        print('No hay pedidos para mostrar.')
        menu_administrador()
    else:
        indice = 1
        for pedido in pedidos:
            marco = ' '*20 +'#'*20
            print(marco)
            print(' '*19,f'#{"Pedido N° "+str(indice):^18s}#')
            print(marco)
            print(f'''
    Nombre de Usuario: {pedido['username']}
    Correo Electronico: {pedido['mail']}''')
            mostrar_carrito(pedido['productos'])
            indice = indice + 1
        print('''
    Si desea eliminar un pedido, presione 's'. Sino, presione cualquier otra tecla.
        ''')
        decision = input('¿Desea eliminar un pedido? S/N: ').lower()
        if decision != 's':
            limpiarPantalla()
            return menu_administrador()
        else:
            eliminar_pedido(indice,pedidos)

#Creamos la funcion recursiva que permitira al usuario eliminar los presupuestos.
def eliminar_pedido(indice,lista):
    print("""  -- Ingrese 'x' para volver al menu anterior -- 
    A continuacion, ingrese el numero de pedido que desea eliminar.""")
    numero_pedido = input('El numero de pedido a eliminar es: ')
    if numero_pedido.lower() == 'x':
        menu_administrador()
    else:
        try:
            numero_pedido = int(numero_pedido)
            if numero_pedido <= 0 or numero_pedido > indice - 1:
                print('Por favor, ingrese una opcion válida.')
                eliminar_pedido(indice,lista)
            else:
                print(f'''
    Se eliminara el pedido {numero_pedido}. Si desea continuar, presione 's'. Sino, presione cualquier otra tecla.
                ''')
                confirmar_decision = input(f'¿Desea eliminar el pedido {numero_pedido}? S/N: ')
                if confirmar_decision.lower() != 's':
                    eliminar_pedido(indice,lista)
                else:
                    del lista[numero_pedido - 1]
                    with open(r'pedidos.json','w',encoding='utf-8') as nuevos_pedidos:
                        nuevos_pedidos.write(json.dumps(lista,indent=4))
                    limpiarPantalla()
                    print('''
        El pedido se ha eliminado satisfactoriamente.
                    ''')
                    menu_administrador()
        except ValueError:
            print('Por favor, ingrese una opcion válida.')
            eliminar_pedido(indice,lista)

menu_principal()
