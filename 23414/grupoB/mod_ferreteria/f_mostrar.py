from mod_ferreteria.f_esteticas import *
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)

def listarProductos(listado):
    print("LISTADO DE PRODUCTOS")
    encabezado()
    for item in listado:
        cuerpo(item)
    pie()
    pausa_con_respuesta()
    borrarpantalla()
######################################################################
#BUSUEDA DE PRODUCTOS#################################################
def busquedaProductos(listado,caracteres):
    print("RESULTADO DE BUSQUEDA")
    encabezado()
    for item in listado:
        if caracteres in item["descripcion"]:
            cuerpo(item)
    pie()
    pausa_con_respuesta()
    borrarpantalla()
    
    ########################################################################################    
##GENERACION DE REPORTE .TXT############################################################

def generareportetxt(listado, txt_file_path):
    with open(txt_file_path, 'w') as txtArchivo:
        for productos in listado:
            values = productos.values()
            txtArchivo.write(' '.join(map(str, values)) + '\n')
            