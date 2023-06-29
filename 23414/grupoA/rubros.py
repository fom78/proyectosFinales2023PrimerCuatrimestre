#FUNCIONES DEL MODULO: ***COMPLETAR***
#abm_rubros
#alta_rubros
#baja_rubros
#modificacion_rubros
#listar_rubros
#literal_frio

from general import *

###############################################################################
###   RUBROS                                                                ###
###############################################################################
#actualiza la cantidad de articulos de cada rubro
def actualiza_rubros(rubros, articulos):
    for rubro in rubros:
        cant_articulos=0
        for articulo in articulos:
            if articulo['cd_articulo'][:3]==rubro['cd_rubro']:
                cant_articulos+=1
        rubro['cant_articulos']=cant_articulos
    escribe_datos_json(rubros, json_rubros)

#devuelve una cadena descriptiva segun el codigo de frio que recibe como argumento
def literal_frio(frio):
    if frio==0:
        return 'No requiere'
    elif frio==1:
        return 'Puede refrigerarse'
    elif frio==2:
        return 'Requiere refrigeración'
    elif frio==3:
        return 'Requiere congelación'
    else:
        return '---'  #no deberia pasar nunca por el else

#listado de rubros diferenciado para usuarios registrados y clientes
def listar_rubros(rubros, usuario='usuario registrado', pausar='S', titulo='Listado de Rubros'):
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', titulo]]
    menu+=[['com_*']]
    menu+=[['com_n']]
    if usuario=='clientes':
        menu+=[['com_<', f"{'Código':<6} {'Rubro':<20}"]]
        menu+=[['com_<', f"{'='*6:<6} {'='*20:<20}"]]
        for rubro in rubros:
            menu+=[['com_<', f"{rubro['cd_rubro']:<6} {rubro['rubro']:<20}"]]
    else:
        menu+=[['com_<', f"{'Código':<6} {'Rubro':<20} {'Frío':<22} {'Artículos':<9}"]]
        menu+=[['com_<', f"{'='*6:<6} {'='*20:<20} {'='*22:<22} {'='*9:<9}"]]
        for rubro in rubros:
            refrigeracion=literal_frio(int(rubro['frio']))
            menu+=[['com_<', f"{rubro['cd_rubro']:<6} {rubro['rubro']:<20} {refrigeracion:<22} {str(rubro['cant_articulos']):>9}"]]
    menu+=[['com_n']]
    mostrar_menu(menu)
    if pausar=='S':
        pausa()

#rubros: {'cd_rubro':str, 'rubro':str, 'frio':int(0,3), 'cant_articulos':int}
def alta_rubros(rubros):
    while True:  #alta de nuevos rubros hasta salir ingresando 0 como codigo
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Alta de Rubros']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        mostrar_menu(menu)
        nuevo_cd_rubro=input('Ingrese el código del nuevo rubro (RRR), 0 para terminar: ').upper()
        if nuevo_cd_rubro=='0':  #salir
            break  #sale del while de alta de nuevos rubros
        elif len(nuevo_cd_rubro)!=3 or not nuevo_cd_rubro.isalpha():  #el codigo ingresado no es valido
            print('El código de rubro debe estar formado por tres letras.\n')
            pausa()
            continue
        for rubro in rubros:  #no quiero salir y el codigo es valido, verifico si ya existe
            if nuevo_cd_rubro==rubro['cd_rubro']:
                print(f'Ese código ya existe: {rubro["cd_rubro"]}: {rubro["rubro"]}.\n')
                pausa()
                break  #salgo del for de verificacion de codigos existentes
        if nuevo_cd_rubro==rubro['cd_rubro']:
            continue  #codigo repetido, vuelvo a pedir los datos
        #es un codigo valido y no existe previamente, ingreso el nombre del nuevo rubro
        while True:
            nuevo_rubro=input('Ingrese el nombre del nuevo rubro: ').capitalize()
            if nuevo_rubro:  #si nuevo_rubro=='' vuelve a pedir el ingreso
                break
        while True:  #ingreso la necesidad de refrigeracion de los articulos de este nuevo rubro
            menu =[['com_n']]
            menu+=[['com_+', 'Necesidad de refrigeración:']]
            menu+=[['com_<', '='*27]]
            for i in range(4):
                menu+=[[str(i), literal_frio(i)]]
            menu+=[['com_n']]
            menu+=[['com_i', 'Ingrese la necesidad de refrigeración: ']]
            nuevo_frio=mostrar_menu(menu)
            if nuevo_frio in ('0', '1', '2', '3'):  #el codigo es valido, salgo del while de frio
                break
        #creo el nuevo rubro con los datos ingresados y le asigno 0 a su cantidad de articulos
        rubro={'cd_rubro': nuevo_cd_rubro, 'rubro': nuevo_rubro, 'frio': int(nuevo_frio), 'cant_articulos': 0}
        rubros.append(rubro)  #actualizo en memoria
        escribe_datos_json(rubros, json_rubros)  #actualizo en disco
        listar_rubros(rubros)

def baja_rubros(rubros, articulos):
    while True:
        encontrado=False
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Baja de Rubros']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['C', 'Ingrese (C) para buscar el rubro a eliminar por su código']]
        menu+=[['R', 'Ingrese (R) para buscar el rubro a eliminar por su nombre']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su opcion, o ENTER para ver una lista de rubros: ']]
        opcion=mostrar_menu(menu).upper()
        if opcion=='':
            listar_rubros(rubros, titulo='Baja de Rubros')
            continue
        elif opcion != 'C'and opcion != 'R':
            continue
        elif opcion=='C':
            item_a_eliminar=input('Ingrese el código del rubro a eliminar: ').upper()
            for rubro in rubros:
                if item_a_eliminar==rubro['cd_rubro']:
                    encontrado=True
                    rubro_a_eliminar=rubro
        elif opcion=='R':
            item_a_eliminar=input('Ingrese el nombre del rubro a eliminar: ').capitalize()
            for rubro in rubros:
                if item_a_eliminar==rubro['rubro']:
                    encontrado=True
                    rubro_a_eliminar=rubro
        if encontrado:
            cd_rubro_a_eliminar=rubro_a_eliminar['cd_rubro']
            tiene_articulos=False
            for articulo in articulos:
                if articulo['cd_articulo'][:3]==cd_rubro_a_eliminar:
                    tiene_articulos=True
                    break
            if tiene_articulos:
                print(f"El rubro {rubro_a_eliminar['cd_rubro']} {rubro_a_eliminar['rubro']} tiene artículos asociados, para eliminarlo antes debe asignarles otro rubro o eliminarlos.")
                pausa()
            else:
                confirma=input(f"Está seguro de eliminar al rubro {rubro_a_eliminar['cd_rubro']} {rubro_a_eliminar['rubro']} (S/N): ").upper()
                if confirma=='S':
                    rubros.remove(rubro_a_eliminar)
                    escribe_datos_json(rubros, json_rubros)
                    listar_rubros(rubros)
        else:
            print(f"No se encontró el {'código' if opcion=='C' else 'rubro'} ingresado ({item_a_eliminar}).")
            pausa()
        break

#rubros: {'cd_rubro':str, 'rubro':str, 'frio':int(0,3), 'cant_articulos':int}
def modificacion_rubros(rubros):
    while True:
        encontrado=False
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Modificación de Rubros']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['C', 'Ingrese (C) para buscar el rubro a modificar por su código']]
        menu+=[['R', 'Ingrese (R) para buscar el rubro a modificar por su nombre']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su opcion, o ENTER para ver una lista de rubros: ']]
        opcion=mostrar_menu(menu).upper()
        if opcion=='':
            listar_rubros(rubros, titulo='Modificación de Rubros')
            continue
        elif opcion != 'C'and opcion != 'R':
            continue
        elif opcion=='C':
            item_a_modificar=input('Ingrese el código del rubro a modificar: ').upper()
            for rubro in rubros:
                if item_a_modificar==rubro['cd_rubro']:
                    encontrado=True
                    rubro_a_modificar=rubro
        elif opcion=='R':
            item_a_modificar=input('Ingrese el nombre del rubro a modificar: ').capitalize()
            for rubro in rubros:
                if item_a_modificar==rubro['rubro']:
                    encontrado=True
                    rubro_a_modificar=rubro
        if encontrado:
            print(f"Ingrese un nuevo nombre para el rubro {rubro_a_modificar['rubro']}, o ENTER para continuar.")
            n_rubro=input('Nuevo nombre de rubro: ').capitalize()
            while True:  #ingreso la necesidad de refrigeracion de los articulos de este nuevo rubro
                menu =[['com_n']]
                menu+=[['com_+', 'Necesidad de refrigeración:']]
                menu+=[['com_<', '='*27]]
                for i in range(4):
                    menu+=[[str(i), literal_frio(i)]]
                menu+=[['com_n']]
                menu+=[['com_i', 'Ingrese la necesidad de refrigeración: ']]
                n_frio=mostrar_menu(menu)
                if n_frio in ('0', '1', '2', '3'):  #el codigo es valido, salgo del while de frio
                    break
            for rubro in rubros:
                if rubro_a_modificar['cd_rubro']==rubro['cd_rubro']:
                    if n_rubro!='':
                        rubro_a_modificar['rubro']=n_rubro
                    rubro['frio']=n_frio
                    break
            rubros=sorted(rubros, key=lambda rubros: rubros['rubro'])
            escribe_datos_json(rubros, json_rubros)  #actualizo en disco
            listar_rubros(rubros)
        else:
            print(f"No se encontró el {'código' if opcion=='C' else 'rubro'} ingresado ({item_a_modificar}).")
            pausa()
        break

#rubros: {'cd_rubro':str, 'rubro':str, 'frio':int(0,3), 'cant_articulos':int}
def abm_rubros(rubros, articulos):  #gestion de rubros
    while True:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Gestión de Rubros']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['1', 'Listado de rubros']]
        menu+=[['2', 'Alta de rubros']]
        menu+=[['3', 'Baja de rubros']]
        menu+=[['4', 'Modificación de rubros']]
        menu+=[['com_n']]
        menu+=[['0', 'Salir']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese su consulta y luego presione ENTER: ']]
        opcion=mostrar_menu(menu)
        if opcion=='1':
            listar_rubros(rubros)
        elif opcion=='2':
            alta_rubros(rubros)
        elif opcion=='3':
            baja_rubros(rubros, articulos)
        elif opcion=='4':
            modificacion_rubros(rubros)
        elif opcion=='0':
            break

