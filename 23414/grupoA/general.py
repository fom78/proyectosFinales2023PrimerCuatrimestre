#modulo general

###############################################################################
###   MODULO DE FUNCIONES GENERALES                                         ###
###############################################################################

#FUNCIONES DEL MODULO: ***COMPLETAR***
#f_ansi(estilo='sin efecto', texto='blanco', fondo='negro') str, str, str
#modo_video(modo='normal') str
#pausa(msg='Presione ENTER para continuar...') str
#mostrar_menu(menu)  [[]] -> str
#carga_datos_json str -> [{}]
#escribe_datos_json [{}], str

#manejo de archivos json
from json import load, dump

#interaccion con el sistema operativo
#uso: system('clear') en GNU/Linux o system('cls') en MS Windows (cualquier comando del shell)
from os import system, name, path, chdir

#manejo de contraseñas (ingreso sin eco en pantalla)
from getpass import getpass  #similar a input, sin mostrar los caracteres ingresados en la terminal

#manejo de fechas
from datetime import date

#manejo de tiempos (futuras ampliaciones con time_ns como semilla para la encriptacion de contraseñas)
from time import sleep, time_ns, gmtime  #sleep(s), time_ns() ns desde 01/01/1970 (origen para time)

#parametros del sistema
ancho_linea=150
sangria=3
intentos_ingreso_max=3

#comandos propios de cada sistema operativo
so               = name
limpiar_pantalla = 'clear' if so=='posix' else 'cls'
listar_carpeta   = 'ls'    if so=='posix' else 'dir'
copiar_archivo   = 'cp'    if so=='posix' else 'copy'
borrar_archivo   = 'rm'    if so=='posix' else 'del'
barra            = '/'     if so=='posix' else '\\'
carpeta_sistema  = path.dirname(__file__)                     #'/home/userpp/stock'        - r'D:\stock'
carpeta_datos    = carpeta_sistema + barra + 'datos' + barra  #'/home/userpp/stock/datos/' - r'D:\stock\datos\'

#archivos
json_usuarios  = 'usuarios.json'  #json_NN = carpeta_sistema + carpeta_datos + 'NN.dat'
json_rubros    = 'rubros.json'
json_articulos = 'articulos.json'
json_stock     = 'stock.json'

###############################################################################
###   FUNCIONES DE FORMATEO DE VIDEO                                        ###
###############################################################################
def f_ansi(estilo='sin efecto', texto='blanco', fondo='negro'):
    #formato ANSI: ESC + '[' + estilo + ';' + color_texto + ';' + color_fondo + 'm'
    #                          0-7            30-37               40-47
    #Estilo    : Código estilo - Color   : Código texto : Código fondo 
    #sin efecto: 0               negro   : 30             40
    #negrita   : 1               rojo    : 31             41
    #debil     : 2               verde   : 32             42
    #cursiva   : 3               amarillo: 33             43
    #subrayado : 4               azul    : 34             44
    #inverso   : 5               morado  : 35             45
    #parpadea  : 6               cian    : 36             46
    #tachado   : 7               blanco  : 37             47
    ESC=chr(27)  #Esc
    estilos = ('sin efecto', 'negrita', 'debil', 'cursiva', 'subrayado', 'inverso', 'parpadea', 'tachado')
    textos = fondos = ('negro', 'rojo', 'verde', 'amarillo', 'azul', 'morado', 'cian', 'blanco')
    est = str(estilos.index(estilo))    if estilo in estilos else  0
    txt = str(30 + textos.index(texto)) if texto  in textos  else 37
    fon = str(40 + fondos.index(fondo)) if fondo  in fondos  else 40
    print(ESC + '[' + est + ';' + txt + ';' + fon + 'm')

def modo_video(modo='normal'):
    if modo=='normal':
        f_ansi('negrita','amarillo','morado')
    elif modo=='alerta':
        f_ansi('negrita','rojo','negro')
    elif modo=='azul':
        f_ansi('negrita','blanco','azul')
    elif modo=='amarillo':
        f_ansi('negrita','amarillo','negro')
    else:
        f_ansi('sin efecto','blanco','negro')

###############################################################################
###   FUNCION DE PAUSA CON MENSAJE                                          ###
###############################################################################
def pausa(msg='Presione ENTER para continuar...'):
    input('\n'+msg)

###############################################################################
###   FUNCION GENERAL DE MENU                                               ###
###############################################################################
def mostrar_menu(menu):
    system(limpiar_pantalla)
    # ~ sangria=3
    opcion=''
    for item in menu:
        if item[0]=='com_n':    #salto de línea
            print()
        elif item[0]=='com_*':  #línea de asteriscos                                : ****************************************
            print(f'{"*"*ancho_linea}')
        elif item[0]=='com_^':  #textos centrados (títulos)                         : *                Título                *
            print(f'* {item[1].upper():^{ancho_linea-4}} *')
        elif item[0]=='com_<':  #textos alineados a la izquierda                    : *Texto descriptivo                     *
            print(f'{item[1]}')
        elif item[0]=='com_+':  #textos con sangría (opciones con texto descriptivo): *   Para hacer x presione y            *
            print(f'{" "*sangria}{item[1]}')
        elif item[0]=='com_i':  #ingreso de datos con texto descriptivo             : *Ingrese su opción:                    *
            opcion=input('\n'+item[1])
        elif item[0]=='com_p':  #ingreso de contraseñas con texto descriptivo       : *Ingrese su contraseña:                *
            opcion=getpass('\n'+item[1])
        else:                   #opciones con un número o letra asignados           : *    1) Opción 1                       *
            print(f'{" "*sangria}{item[0]:>2}) {item[1]}')  #                       : *   AA) Opción AA                      *
    return opcion

###############################################################################
###   MANEJO DE ARCHIVOS JSON                                               ###
###############################################################################
def carga_datos_json(arch):
    try:
        f=open(arch, 'r')
        lista_dic=load(f)
        f.close()
    except:
        f=open(arch, 'w')
        f.close()
        lista_dic=[]
    return lista_dic

def escribe_datos_json(lista_dic, arch):
    #en dump:
    #  - indent=2 
    #    agrega una indentacion de 2 espacios y facilita la lectura del archivo json
    #  - ensure_ascii=False
    #    permite escribir bien las vocales acentuadas
    f=open(arch, 'w')
    dump(lista_dic, f, indent=2, ensure_ascii=False)
    f.close()

###############################################################################
###   MANEJO DE FECHAS Y TIEMPOS                                            ###
###############################################################################
def literal_dia(dia):
    if dia==0:
        return 'lunes'
    elif dia==1:
        return 'martes'
    elif dia==2:
        return 'miercoles'
    elif dia==3:
        return 'jueves'
    elif dia==4:
        return 'viernes'
    elif dia==5:
        return 'sabado'
    elif dia==6:
        return 'domingo'

def codigo_ejemplo_de_fechas():
    #ejemplo de manejo de fechas con datetime.date
    hoy  = date.today()
    venc = date(2023, 8, 18)
    #ejemplo para el calculo de vencimientos (la diferencia de fecha retorna un objeto timedelta)
    print(f'''
    Fechas desde datetime.date:
    Hoy es {hoy.day}/{hoy.month}/{hoy.year} - {hoy}
    Vencimiento: {venc.day}/{venc.month}/{venc.year} (ejemplo para el calculo)
    Dias hasta el vencimiento: {abs(venc-hoy).days}
    ''')

    #tiempos y fechas con time (time_ns y gmtime)
    t_ns = time_ns()  #puedo usarlo de semilla para encriptar
    t = gmtime()  #t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, t.tm_wday (0: lunes), tm_yday (dias desde el 1/1)
    print(f'''
    Tiempos con time.time_ns:
    Desde el 01/01/1970 pasaron {t_ns}ns, o sea {abs(t_ns/1000000000/86400/365)} años.

    Tiempos y fechas con time.gmtime:
    Hoy es {literal_dia(t.tm_wday)}, {t.tm_mday}/{t.tm_mon}/{t.tm_year}, y son las {t.tm_hour}:{t.tm_min}:{t.tm_sec} (UTC).
    Pasaron {t.tm_yday} días desde el 01/01/{t.tm_year}.
    ''')
