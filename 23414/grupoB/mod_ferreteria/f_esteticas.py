import os
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)
#TITULOS###########################
def titulo(texto):
    texto = texto.upper()
    print("-"*50)
    print(texto.center(50,":"))
    print("-"*50)
    print ("")

#PAUSA CON RESPUESTA DE ENTER#############################################
def pausa_con_respuesta():
    input("Presiona Enter para continuar...")
    print("Continuando después de la pausa.")

#BOORADO DE PANTALLA#####################################################
def borrarpantalla():
    # El siguiente código funciona en Windows, macOS y Linux
    os.system('cls' if os.name == 'nt' else 'clear')

#FORMATO DE TABLAS DE EN PANTALLA####################################
def encabezado():
    print()
    print("-"*104)
    print (f"| CODIGO |  CATEGORIA   | CANTIDAD|                DESCRIPCION               |  PREC.UNIT. |     PVP   |")
    print("-"*104)
    
def cuerpo(item):
    print (f"|{item['codigo']:6}  | {item['categoria']:<12} | {item['cantidad']:7} | {item['descripcion']:<40} |  {item['precioUnit']:10.2f} | {item['precioVPublico']:10.2f}|")   

def pie():
    print("-"*104)
    print()


#CONTROL DE CATEGORIA###########################################################################
def control_categoria():
    print ("Selecciona a que categora pertenece el nuevo producto:")
    print ("""
    [1] FERRETERIA
    [2] BULONERIA Y FIJACIONES
    [3] HERRAMIENTAS DE MEDICION
    [4] ADHESIVOS    
    [0] OTRO""")
    var=input(">>>> ")
    match var:
        case "1":
            var = "FERRETERIA"
        case "2":
            var = "BULONERIA"
        case "3":
            var = "MEDICION"
        case "4":
            var = "ADHESIVOS"
        case "0":
            var = "Otro"
        case _:
            var = "Otro"

            
    return str(var)