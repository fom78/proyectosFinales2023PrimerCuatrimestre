#!/usr/bin/python3
#Sistema de gestion de stock
#todos los archivos deben estar en la misma carpeta, tanto codigo (.py), como datos (.dat, .json, o .sqlite3).

from general import *  #carga_datos, pausa, mostrar_menu (COMPLETAR)
from usuarios import *
from articulos import *
from rubros import *
from reportes import *

###############################################################################
###   INGRESO DE USUARIOS REGISTRADOS                                       ###
###############################################################################
def ingresar(usuarios, rubros, articulos, stock, tope):
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', 'Ingreso de Usuarios Registrados']]
    menu+=[['com_*']]
    menu+=[['com_n']]
    salir=False
    login_ok=False
    intentos_ingreso=0
    while not login_ok and intentos_ingreso<tope:
        intentos_ingreso+=1
        menu+=[['com_i', 'Ingrese su usuario y luego presione ENTER: ']]
        usuario_ingresado=mostrar_menu(menu)
        menu.pop()
        menu+=[['com_p', 'Ingrese su contraseña y luego presione ENTER: ']]
        clave_ingresada=mostrar_menu(menu)
        menu.pop()
        for usuario in usuarios:
            if usuario_ingresado==usuario['usuario'] and clave_ingresada==usuario['clave']:
                login_ok=True
                menu =[['com_*']]
                menu+=[['com_<', f'*{" "*(ancho_linea-2)}*']]
                menu+=[['com_^', f'Bienvenido {usuario_ingresado}!!!']]
                menu+=[['com_<', f'*{" "*(ancho_linea-2)}*']]
                menu+=[['com_*']]
                menu+=[['com_n']]
                mostrar_menu(menu)
                pausa()
                #devuelve True si un usuario registrado quiere salir del sistema
                salir=sistema_para_usuarios(usuarios, rubros, articulos, stock)
                break
        if not login_ok:  #recorrio usuarios y no coincide ningun par usuario, contraseña
                print('Usuario o contraseña inválidos.')
                print(f'Tiene {intentos_ingreso_max - intentos_ingreso} intentos para ingresar.')
                pausa()
    if intentos_ingreso>=tope:
        print('Ingreso no autorizado.')
        pausa()
    return salir  #si devuelve True desde sistema_para_usuarios, sale del sistema

###############################################################################
###   MENU DE USUARIOS REGISTRADOS                                          ###
###############################################################################
def sistema_para_usuarios(usuarios, rubros, articulos, stock):
    while True:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Menú de Usuarios Registrados']]
        menu+=[['com_*']]
        menu+=[['1', 'Gestión de artículos']]
        menu+=[['2', 'Gestión de rubros']]
        menu+=[['3', 'Reportes']]
        menu+=[['4', 'Gestión de usuarios']]
        menu+=[['com_n']]
        menu+=[['0', 'Salir al menú de clientes']]
        menu+=[['00', 'Salir del sistema']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su opción y luego presione ENTER: ']]
        opcion=mostrar_menu(menu)
        if opcion=='1':
            abm_articulos(articulos)  #gestion de articulos
        elif opcion=='2':
            abm_rubros(rubros)  #gestion de rubros
        elif opcion=='3':
            reportes(articulos, stock)  #reportes
        elif opcion=='4':
            modo_video('alerta')
            abm_usuarios(usuarios, intentos_ingreso_max)  #gestion de usuarios
            modo_video('normal')
        elif opcion=='0':
            #salir a menu de clientes
            return False
        elif opcion=='00':
            #salir del sistema
            return True

###############################################################################
###   MENU PRINCIPAL (INGRESO AL SISTEMA Y VISTA DE CLIENTES)               ###
###############################################################################
def menu_principal():
    while True:
        #ver en menu.py como trabaja la funcion mostrar_menu()
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock', '']]
        menu+=[['com_^', 'Consulta de Stock y Precios', '']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['com_<', 'Ingrese:']]
        menu+=[['com_n']]
        menu+=[['com_+', '(artículo) para consultar su stock y precio']]  #cualquier ingreso != de R o U lo buscara como un articulo
        menu+=[['com_+', '(R)        para buscar un artículo por su rubro']]
        menu+=[['com_+', '(U)        para ingresar al sistema como un usuario registrado']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su consulta y luego presione ENTER: ', '']]
        opcion=mostrar_menu(menu)
        if opcion.lower()=='u':  #ingresar al sistema
            #ingresar devuelve True si se selecciona salir del sistema en el menu de usuarios
            #esto evita que un cliente pueda salir del sistema, solo un usuario registrado puede salir
            salir=ingresar(usuarios, rubros, articulos, stock, intentos_ingreso_max)
            if salir:
                break
        elif opcion.lower()=='r':  #listar rubros
            listar_rubros(rubros, 'clientes')
        elif opcion=='':  #si no se ingreso nada, no hace nada y vuelve a mostrar el menú
            pass
        else:  #buscar articulo
            buscar_articulo(articulos, opcion)

###############################################################################
###   INICIO DEL CODIGO                                                     ###
###############################################################################
usuarios =carga_datos_json(json_usuarios)
rubros   =carga_datos_json(json_rubros)
articulos=carga_datos_json(json_articulos)
stock    =carga_datos_json(json_stock)

#usuarios ordenado por nombre de usuario
usuarios=sorted(usuarios, key=lambda usuarios: usuarios['usuario'])

#rubros ordenado por rubro
rubros=sorted(rubros, key=lambda rubros: rubros['rubro'])

#articulos ordenado por articulo y marca
articulos=sorted(articulos, key=lambda articulos: articulos['articulo']+articulos['marca']+articulos['presentacion']+str(articulos['peso'])+articulos['unidad'])

# ~ #articulos ordenado por codigo
# ~ articulos=sorted(articulos, key=lambda articulos: articulos['cd_articulo'])

# ~ #articulos ordenado por rubro y articulo
# ~ articulos=sorted(articulos, key=lambda articulos: articulos['cd_articulo'][:3]+articulos['articulo'])

modo_video('normal')

menu_principal()
