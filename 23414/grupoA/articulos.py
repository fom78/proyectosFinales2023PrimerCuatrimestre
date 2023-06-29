#FUNCIONES DEL MODULO: ***COMPLETAR***
#abm_articulos
#alta_articulos(articulos, rubros)
#baja_articulos
#modificacion_articulos
#listar_articulos(articulos)
#buscar_articulo(articulos, articulo_buscado='', titulo='Búsqueda de Artículos')

from general import *
from rubros import listar_rubros, actualiza_rubros

###############################################################################
###   ARTICULOS                                                             ###
###############################################################################
#cd_articulo,articulo,marca,presentacion,peso,unidad,bulto,precio,cantidad,origen,vencimiento
def buscar_articulo(articulos, articulo_buscado='', titulo='Búsqueda de Artículos'):
    encontrado=[]
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', titulo]]
    menu+=[['com_*']]
    menu+=[['com_n']]
    menu+=[['com_<', f"{'Código':<7}  {'Artículo':<25}  {'Marca':<25}  {'Presentación':<20}  {'Peso/Unidad':<11}  {'Precio':<8}  {'Origen':<9}"]]
    menu+=[['com_<', f"{'='*7}  {'='*25}  {'='*25}  {'='*20}  {'='*11}  {'='*8}  {'='*9}"]]
    if articulo_buscado=='':
        articulo_buscado=input('Ingrese el artículo a buscar: ')
    for articulo in articulos:
        if articulo_buscado=='*' or articulo_buscado.lower() in articulo['articulo'].lower():
            encontrado+=articulo
            presentacion=' ' if articulo['presentacion']=='' else articulo['presentacion']
            origen='Importado' if articulo['origen']=='I' else 'Nacional'
            menu+=[['com_<', f"{articulo['cd_articulo']:<7}  {articulo['articulo']:<25}  {articulo['marca']:<25}  {presentacion:<20}  {articulo['peso']:9.2f}{articulo['unidad']:<2}  ${articulo['precio']:7.2f}  {origen:<9}"]]
    mostrar_menu(menu)
    pausa()
    return encontrado

def listar_articulos(articulos):
    buscar_articulo(articulos, '*', 'Listado de Artículos')

#articulo: cd_articulo, articulo, marca, presentacion, peso, unidad, precio, stock_minimo, origen
def alta_articulos(articulos, rubros):
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', 'Alta de Artículos']]
    menu+=[['com_*']]
    menu+=[['com_n']]
    menu+=[['com_<', 'Ingrese los datos del nuevo artículo.']]
    menu+=[['com_n']]
    mostrar_menu(menu)
    print('\nIngrese un rubro para el artículo de los rubros registrados en el sistema:\n')
    listar_rubros(rubros, pausar='N', titulo='Alta de Artículos')
    while True:
        print()
        #ingreso primero el rubro del articulo para formar su codigo
        n_rubro                   =input('Ingrese el código de rubro: ').upper()
        #el codigo de rubro ingresado es valido?
        if len(n_rubro)!=3 or not n_rubro.isalpha():
            print('El código de rubro debe estar formado por tres letras.\n')
            pausa()
            continue
        #existe ese codigo de rubro?
        existe=False
        for rubro in rubros:
            if rubro['cd_rubro']==n_rubro:
                existe=True
                break
        #busco el ultimo codigo de ese rubro
        if existe:
            max_cd=0
            for articulo in articulos:
                if articulo['cd_articulo'][:3]==n_rubro:
                    if int(articulo['cd_articulo'][3:])>max_cd:
                        max_cd=int(articulo['cd_articulo'][3:])
            #el nuevo cd_articulo esta formado por el cd_rubro + max + 1 (con ceros a la izquierda con formato 0000)
            n_cd_articulo         =n_rubro+f'{max_cd+1:0>4}'
            n_articulo            =input('Nombre (ENTER para salir): ').capitalize()
            if n_articulo=='':
                break
            n_marca               =input('Marca                    : ').capitalize()
            n_presentacion        =input('Presentación             : ').capitalize()
            while True:
                try:
                    n_peso        =input('Peso o volumen           : ')
                    n_peso        =float(n_peso)
                    break
                except:
                    print('Ingrese un número...')
            n_unidad              =input('Unidad (KG/G/L/ML/U)     : ').upper()
            existe=False
            for articulo in articulos:
                if articulo['articulo']    ==n_articulo     and \
                   articulo['marca']       ==n_marca        and \
                   articulo['presentacion']==n_presentacion and \
                   articulo['peso']        ==n_peso         and \
                   articulo['unidad']      ==n_unidad:
                    existe=True
                    break
            if existe:
                print('El artículo ya existe...')
                pausa()
                break
            else:
                while True:
                    try:
                        n_precio      =input('Precio               : ')
                        n_precio      =float(n_precio)
                        break
                    except:
                        print('Ingrese un número...')
                while True:
                    try:
                        n_stock_minimo=input('Stock mínimo         : ')
                        n_stock_minimo=float(n_stock_minimo)
                        break
                    except:
                        print('Ingrese un número...')
                n_origen              =input('Origen (Nac/Imp)     : ').lower()
                n_origen='N' if n_origen!='I' else 'I'
                articulo={'cd_articulo' : n_cd_articulo, \
                          'articulo'    : n_articulo, \
                          'marca'       : n_marca, \
                          'presentacion': n_presentacion, \
                          'peso'        : n_peso, \
                          'unidad'      : n_unidad, \
                          'precio'      : n_precio, \
                          'stock_minimo': n_stock_minimo, \
                          'origen'      : n_origen}
                articulos.append(articulo)
                articulos=sorted(articulos, key=lambda articulos: articulos['articulo']+articulos['marca']+articulos['presentacion']+str(articulos['peso'])+articulos['unidad'])
                escribe_datos_json(articulos, json_articulos)
                break
        else:
            print('Ese código de rubro no existe...')
            pausa()
            break

#articulo: cd_articulo, articulo, marca, presentacion, peso, unidad, precio, stock_minimo, origen
def baja_articulos(articulos, stock):
    stock=sorted(stock, key=lambda stock: stock['cd_articulo']+stock['vencimiento'])
    while True:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Baja de Artículos']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['1', 'Baja de cantidad de artículos (venta/vencimiento)']]
        menu+=[['2', 'Eliminación de artículos']]
        menu+=[['com_n']]
        menu+=[['0', 'Salir']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su consulta y luego presione ENTER: ']]
        opcion=mostrar_menu(menu)
        if opcion=='0':
            break
        b_articulo=input('Ingrese el código del artículo a actualizar su cantidad: ').upper()
        if len(b_articulo)!=7:
            print('El código está formado por tres letras y cuatro dígitos...')
            pausa()
            continue
        encontrado=False
        for articulo in articulos:
            if articulo['cd_articulo']==b_articulo:
                encontrado=True
                print(f"Artículo: ({articulo['cd_articulo']}) {articulo['articulo']} {articulo['marca']}")
                print(f"Artículo: ({articulo['presentacion']}) {articulo['peso']}{articulo['unidad']}")
                cant_dep=0
                cant_gon=0
                for item in stock:
                    if item['cd_articulo']==b_articulo:
                        cant_dep+=item['cant_dep']
                        cant_gon+=item['cant_gon']
                print(f"Stock en depósito: {cant_dep}")
                print(f"Stock en góndola : {cant_gon}")
                print()
        if not encontrado:
            print(f"No se encontró el artículo {b_articulo}.")
            pausa()
            continue
        if opcion=='1':
            print('Ingrese la cantidad a descontar (si es mayor al stock, este quedara en cero).')
            while True:
                try:
                    cantidad=int(input('Cantidad a descontar del stock: '))
                    break
                except:
                    print('Ingrese un número...')
            print(f'Ingrese de dónde desea descontar los {cantidad} artículos.')
            deposito=input('Ingrese depósito o góndola (D/G): ').upper()
            for item in stock:
                if item['cd_articulo']==b_articulo:
                    if deposito=='D':
                        if cantidad>item['cant_dep']:
                            cantidad-=item['cant_dep']
                            item['cant_dep']=0
                        else:
                            item['cant_dep']-=cantidad
                            cantidad=0
                            break
                    else:
                        if cantidad>item['cant_gon']:
                            cantidad-=item['cant_gon']
                            item['cant_gon']=0
                        else:
                            item['cant_gon']-=cantidad
                            cantidad=0
                            break
        elif opcion=='2':
            confirma=input(f"Está seguro de eliminar el artículo {b_articulo} (S/N): ").upper()
            if confirma:
                indice_articulo=-1
                for articulo in articulos:
                    indice_articulo+=1
                    if articulo['cd_articulo']==b_articulo:
                        articulos.pop(indice_articulo)
                        indice_stock=-1
                        for item in stock:
                            indice_stock+=1
                            if item['cd_articulo']==b_articulo:
                                stock.pop(indice_stock)
                actualiza_rubros(rubros, articulos)
        elif opcion=='0':
            break
        articulos=sorted(articulos, key=lambda articulos: articulos['articulo']+articulos['marca']+articulos['presentacion']+str(articulos['peso'])+articulos['unidad'])
        escribe_datos_json(articulos, json_articulos)

#articulo: cd_articulo, articulo, marca, presentacion, peso, unidad, precio, stock_minimo, origen
def modificacion_articulos(articulos, rubros, stock):
    stock=sorted(stock, key=lambda stock: stock['cd_articulo']+stock['vencimiento'])
    while True:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Modificación de Artículos']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['com_<', 'Ingrese los datos del artículo a modificar: ']]
        menu+=[['com_n']]
        mostrar_menu(menu)
        print('Ingrese el código del artículo a actualizar su cantidad, o ENTER para salir.')
        m_cd_articulo=input('Código del artículo: ').upper()
        if m_cd_articulo=='':
            break
        if len(m_cd_articulo)!=7:
            print('El código está formado por tres letras y cuatro dígitos...')
            pausa()
            if not buscar_articulo(articulos):
                print('No se encontraron coincidencias...')
                pausa()
            continue
        encontrado=False
        for articulo in articulos:
            if articulo['cd_articulo']==m_cd_articulo:
                encontrado=True
                m_articulo=articulo['articulo']
                m_marca=articulo['marca']
                m_presentacion=articulo['presentacion']
                m_peso=articulo['peso']
                m_unidad=articulo['unidad']
                m_precio=articulo['precio']
                m_stock_minimo=articulo['stock_minimo']
                m_origen=articulo['origen']
                m_cant_dep=0
                m_cant_gon=0
                for item in stock:
                    if item['cd_articulo']==m_cd_articulo:
                        m_cant_dep+=item['cant_dep']
                        m_cant_gon+=item['cant_gon']
                break
        if not encontrado:
            print(f"No se encontró el artículo {m_cd_articulo}.")
            pausa()
            continue
        # ~ listar_rubros(rubros, pausar='N', titulo='Modificación de Artículos')
        print()
        print(f"Artículo: ({m_cd_articulo}) {m_articulo} - Marca: {m_marca}")
        print(f"Presentación: {m_presentacion} - Peso: {m_peso} - Unidad: {m_unidad} - Precio: ${m_precio}")
        print(f"Stock en depósito: {m_cant_dep}")
        print(f"Stock en góndola : {m_cant_gon}")
        print()
        print('Ingrese las modificaciones necesarias, o enter para conservarlas como están.')
        print()
        n_articulo=input('Artículo: ').capitalize()
        if n_articulo!='':
            m_articulo=n_articulo
        n_marca=input('Marca: ').capitalize()
        if n_marca!='':
            m_marca=n_marca
        n_presentacion=input('Presentación: ').capitalize()
        if n_presentacion!='':
            m_presentacion=n_presentacion
        while True:
            try:
                n_peso=input('Peso o volumen: ')
                if n_peso!='':
                    n_peso=float(n_peso)
                    m_peso=n_peso
                break
            except:
                print('Ingrese un número...')
        n_unidad=input('Unidad (KG/G/L/ML/U): ').upper()
        if n_unidad!='':
            m_unidad=n_unidad
        while True:
            try:
                n_precio=input('Precio: ')
                if n_precio!='':
                    n_precio=float(n_precio)
                    m_precio=n_precio
                break
            except:
                print('Ingrese un número...')
        while True:
            try:
                n_stock_minimo=input('Stock mínimo: ')
                if n_stock_minimo!='':
                    n_stock_minimo=float(n_stock_minimo)
                    m_stock_minimo=n_stock_minimo
                break
            except:
                print('Ingrese un número...')
        n_origen=input('Origen (Nac/Imp): ').lower()
        if n_origen!='':
            if n_origen!='I':
                n_origen='N'
            m_origen=n_origen
        n_articulo={'cd_articulo' : m_cd_articulo, \
                    'articulo'    : m_articulo, \
                    'marca'       : m_marca, \
                    'presentacion': m_presentacion, \
                    'peso'        : m_peso, \
                    'unidad'      : m_unidad, \
                    'precio'      : m_precio, \
                    'stock_minimo': m_stock_minimo, \
                    'origen'      : m_origen}
        for articulo in articulos:
            if articulo['cd_articulo']==m_cd_articulo:
                articulos.pop(articulos.index(articulo))
                articulos.append(n_articulo)
                articulos=sorted(articulos, key=lambda articulos: articulos['articulo']+articulos['marca']+articulos['presentacion']+str(articulos['peso'])+articulos['unidad'])
                escribe_datos_json(articulos, json_articulos)
                break

#articulo: cd_articulo 'RRRNNNN', articulo str, marca str, presentacion str, peso float, unidad str, precio float, stock_minimo int, origen 'I'/'N'
def abm_articulos(articulos, rubros, stock):  #gestion de articulos
    while True:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de gestión de Stock']]
        menu+=[['com_^', 'Gestion de Artículos']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['1', 'Listado de artículos']]
        menu+=[['2', 'Alta de artículos']]
        menu+=[['3', 'Baja de artículos']]
        menu+=[['4', 'Modificación de artículos']]
        menu+=[['com_n']]
        menu+=[['0', 'Salir']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su consulta y luego presione ENTER: ']]
        opcion=mostrar_menu(menu)
        if opcion=='1':
            listar_articulos(articulos)
        elif opcion=='2':
            alta_articulos(articulos, rubros)
        elif opcion=='3':
            baja_articulos(articulos, stock)
        elif opcion=='4':
            modificacion_articulos(articulos, rubros, stock)
        elif opcion=='0':
            break
        articulos=sorted(articulos, key=lambda articulos: articulos['articulo']+articulos['marca']+articulos['presentacion']+str(articulos['peso'])+articulos['unidad'])
