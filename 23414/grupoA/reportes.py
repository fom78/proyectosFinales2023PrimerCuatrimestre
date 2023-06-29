#FUNCIONES DEL MODULO: ***COMPLETAR***
#reportes
#reporte_stock
#reporte_reposicion
#Listar_vencidos
#reporte_vencimientos
#reporte_origen

from general import *
#from time import sleep, time_ns  #sleep(s), time_ns() ns desde 01/01/1970
from datetime import date#, time

###############################################################################
###   REPORTES                                                              ###
###############################################################################

def reporte_stock(articulos, rubros, stock):
    while True:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Reportes - Stock general']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['1', 'Stock completo']]
        menu+=[['2', 'Stock por rubro']]
        menu+=[['3', 'Stock completo valorizado']]
        menu+=[['4', 'Stock por rubro valorizado']]
        menu+=[['com_n']]
        menu+=[['0', 'Salir']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su consulta y luego presione ENTER: ']]
        opcion=mostrar_menu(menu)
        if opcion=='0':
            break
        #filtrados por rubro
        if opcion=='2' or opcion=='4':
            while True:
                cd_rubro=input('Ingrese el código de rubro: ').upper()
                #el codigo de rubro ingresado es valido?
                if len(cd_rubro)!=3 or not cd_rubro.isalpha():
                    print('El código de rubro debe estar formado por tres letras.\n')
                    pausa()
                    continue
                #existe ese codigo de rubro?
                existe=False
                for rubro in rubros:
                    if rubro['cd_rubro']==cd_rubro:
                        nm_rubro=rubro['rubro']
                        existe=True
                        break
                #busco el ultimo codigo de ese rubro
                if not existe:
                    print("No existe ese código de rubro...")
                    pausa()
                break
        else:
            cd_rubro='*'
        valorizado= opcion=='3' or opcion=='4'
        #valorizado True/False - cd_rubro '*'/'RRR' según esté o no filtrado por rubro
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        if opcion=='1':
            menu+=[['com_^', 'Stock completo']]
        elif opcion=='2':
            menu+=[['com_^', 'Stock por rubro']]
            menu+=[['com_^', f'Rubro: {nm_rubro}']]
        elif opcion=='3':
            menu+=[['com_^', 'Stock completo valorizado']]
        elif opcion=='4':
            menu+=[['com_^', 'Stock por rubro valorizado']]
            menu+=[['com_^', f'Rubro: {nm_rubro}']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['com_<', f"{'Código':<7} {'Artículo':<25} {'Marca':<25} {'Presentación':<20} {'Peso/Unidad':<11} {'Precio':<10} {'Origen':<11} {'Minimo':<8} {'Depósito':<8} {'Góndola':<8} {'Vencimiento':<11} {'Importe' if valorizado else ''}"]]
        menu+=[['com_<', f"{'='*7} {'='*25} {'='*25} {'='*20} {'='*11} {'='*10} {'='*11} {'='*8} {'='*8} {'='*8} {'='*11} {'='*12 if valorizado else ''}"]]
        for articulo in articulos:
            #si no hay filtro o el articulo pertenece al rubro del filtro muestro el articulo:
            if cd_rubro=='*' or articulo['cd_articulo'][:3]==cd_rubro:
                origen='Importado' if articulo['origen']=='I' else 'Nacional'
                menu+=[['com_<', f"{articulo['cd_articulo']:<7} {articulo['articulo']:<25} {articulo['marca']:<25} {articulo['presentacion']:<20} {articulo['peso']:9.2f}{articulo['unidad']:<2} ${articulo['precio']:>9.2f} {origen:<11}"]]
                for item in stock:
                    if articulo['cd_articulo']==item['cd_articulo']:
                        monto=''
                        if valorizado:
                            monto=articulo['precio']*(item['cant_dep']+item['cant_gon'])
                            monto=f"$ {monto:>10.2f}"
                        menu+=[['com_<', f"{' '*115} {articulo['stock_minimo']:>8} {item['cant_dep']:>8} {item['cant_gon']:>8} {item['vencimiento']:>11} {monto:>12}"]]
        menu+=[['com_n']]
        mostrar_menu(menu)
        pausa()

def reporte_reposicion(articulos, stock):
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', 'Reportes - Artículos para reponer']]
    menu+=[['com_*']]
    menu+=[['com_n']]
    mostrar_menu(menu)
    #titulos
    print(f"{'Código':<7}  {'Artículo':<25}  {'Marca':<25}  {'Presentación':<20}  {'Peso/Unidad':<11}  {'Minimo':<8}  {'Depósito':<8}  {'Góndola':<8}  {'Total':<8}  {'Faltante':<8}")
    print(f"{'='*7}  {'='*25}  {'='*25}  {'='*20}  {'='*11}  {'='*8}  {'='*8}  {'='*8}  {'='*8}  {'='*8}")
    #por cada articulo:
    for articulo in articulos:
        cant_dep=0
        cant_gon=0
        cant_total=0
        #recorro el stock
        for item in stock:
            #si hay una entada para ese articulo acumulo las cantidades:
            if item['cd_articulo']==articulo['cd_articulo']:
                cant_dep=item['cant_dep']
                cant_gon=item['cant_gon']
                cant_total=cant_dep+cant_gon
        #si el acumulado es menor al stock minimo del articulo lo muestro
        if cant_total<articulo['stock_minimo']:
            presentacion=' ' if articulo['presentacion']=='' else articulo['presentacion']
            print(f"{articulo['cd_articulo']:<7}  {articulo['articulo']:<25}  {articulo['marca']:<25}  {presentacion:<20}  {articulo['peso']:9.2f}{articulo['unidad']:<2}  {articulo['stock_minimo']:8.0f}  {cant_dep:8d}  {cant_gon:8d}  {cant_total:8d}  {articulo['stock_minimo']-cant_total:8.0f}")
    pausa()

def listar_vencidos(articulos, stock, margen=0, valorizado=False):
    hoy=date.today()
    vencidos=list()
    for articulo in articulos:
        for item in stock:
            dia_venc=int(item['vencimiento'][:2])  #dd/mm/aaaa
            mes_venc=int(item['vencimiento'][3:5])
            anio_venc=int(item['vencimiento'][6:])
            fc_venc=date(anio_venc, mes_venc, dia_venc)
            dias_venc=(hoy-fc_venc).days
            if articulo['cd_articulo']==item['cd_articulo'] and dias_venc>=-margen:
                vencido={}
                vencido.update(articulo)
                vencido.update(item)
                vencido.update({'dias_venc': dias_venc})
                if valorizado:
                    vencido.update({'monto': articulo['precio']*(item['cant_dep']+item['cant_gon'])})
                vencidos.append(vencido)
    vencidos=sorted(vencidos, key=lambda vencidos: str(-vencidos['dias_venc'])+vencidos['articulo']+vencidos['marca'])
    #titulos
    print(f"{'Código':<7} {'Artículo':<25} {'Marca':<25} {'Presentación':<20} {'Peso/Unidad':<11} {'Precio':<8} {'Origen':<9} {'Depósito':<8} {'Góndola':<8} {'Vencimiento':<11} {'Días vencido':<12} {'Importe' if valorizado else ''}")
    print(f"{'='*7} {'='*25} {'='*25} {'='*20} {'='*11} {'='*8} {'='*9} {'='*8} {'='*8} {'='*11} {'='*12} {'='*12 if valorizado else ''}")
    for vencido in vencidos:
        presentacion=' ' if vencido['presentacion']=='' else vencido['presentacion']
        origen='Importado' if vencido['origen']=='I' else 'Nacional'
        monto=f"{vencido['monto']:9.2f}" if valorizado else ''
        print(f"{vencido['cd_articulo']:<7} {vencido['articulo']:<25} {vencido['marca']:<25} {presentacion:<20} {articulo['peso']:9.2f}{articulo['unidad']:<2} ${vencido['precio']:7.2f} {origen:<9} {vencido['cant_dep']:8d} {vencido['cant_gon']:8d} {vencido['vencimiento']:<11} {vencido['dias_venc']:12d} {monto:>12}")
    pausa()

def reporte_vencimientos(articulos, stock):
    while True:
        vencidos=[]
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Reportes - Artículos vencidos y con vencimiento próximo']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['1', 'Listado de artículos vencidos']]
        menu+=[['2', 'Listado de artículos con vencimiento próximo']]
        menu+=[['3', 'Listado de artículos vencidos valorizado']]
        menu+=[['4', 'Listado de artículos con vencimiento próximo valorizado']]
        menu+=[['com_n']]
        menu+=[['0', 'Salir']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su consulta y luego presione ENTER: ']]
        opcion=mostrar_menu(menu)
        print()
        if opcion=='0':
            break
        else:
            dias_a_venc=0
            if opcion=='2' or opcion=='4':
                while True:
                    try:
                        dias_a_venc=int(input('Ingrese la cantidad de días previos al vencimiento: '))
                    except:
                        print('Ingrese un número entero...')
                        continue
                    break
            valorizado=opcion=='3' or opcion=='4'
            listar_vencidos(articulos, stock, dias_a_venc, valorizado)    

def reporte_origen(articulos):
    importados=[]
    nacionales=[]
    for articulo in articulos:
        if articulo['origen']=='I':
            importados+=[['com_<', f"{articulo['cd_articulo']:<7} {articulo['articulo']:<25} ${articulo['precio']:10.2f}"]]
        else:
            nacionales+=[['com_<', f"{articulo['cd_articulo']:<7} {articulo['articulo']:<25} ${articulo['precio']:10.2f}"]]
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', 'Listado de artículos segun su origen']]
    menu+=[['com_*']]
    menu+=[['com_n']]
    menu+=[['com_*']]
    menu+=[['com_^', 'IMPORTADOS']]
    menu+=[['com_*']]
    menu+=[['com_<', f"{'Código':<7} {'Artículo':<25}  {'Precio':<10}"]]
    menu+=[['com_<', f"{'='*6:<7} {'='*20:<25}  {'='*10:<10}"]]
    menu+=importados
    menu+=[['com_n']]
    menu+=[['com_*']]
    menu+=[['com_^', 'NACIONALES']]
    menu+=[['com_*']]
    menu+=[['com_<', f"{'Código':<7} {'Artículo':<25}  {'Precio':<10}"]]
    menu+=[['com_<', f"{'='*6:<7} {'='*20:<25}  {'='*10:<10}"]]
    menu+=nacionales
    menu+=[['com_n']]
    mostrar_menu(menu)
    pausa()

def reportes(articulos, rubros, stock):  #reportes
    while True:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Reportes']]
        menu+=[['com_*']]
        menu+=[['1', 'Stock general y valorizado']]
        menu+=[['2', 'Artículos para reponer']]
        menu+=[['3', 'Artículos vencidos y con vencimiento próximo']]
        menu+=[['4', 'Artículos por su origen (Importados/Nacionales)']]
        menu+=[['com_n']]
        menu+=[['0', 'Salir']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su consulta y luego presione ENTER: ']]
        opcion=mostrar_menu(menu)
        if opcion=='1':
            reporte_stock(articulos, rubros, stock)
        elif opcion=='2':
            reporte_reposicion(articulos, stock)
        elif opcion=='3':
            reporte_vencimientos(articulos, stock)
        elif opcion=='4':
            reporte_origen(articulos)
        elif opcion=='0':
            break
    if opcion!='0':
        pausa()

