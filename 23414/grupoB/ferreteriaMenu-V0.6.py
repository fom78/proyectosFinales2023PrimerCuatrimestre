import json
from mod_ferreteria.f_esteticas import *
from mod_ferreteria.f_gestion import *
from mod_ferreteria.f_mostrar import *

dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)

file = open("stockFerreteria.json","r") 
productos = json.load(file) 
file.close()
######################################################################
#GENERACION DE MENU Y BUCLE PARA EL MANEJO DE LAS FUNCIONES###########
######################################################################
borrarpantalla()
def menu_gestion():
    borrarpantalla()
    titulo("menú gestión")
    while True:
            
        print("[1]- Insertar un producto")
        print("[2]- Borrar un Producto")
        print("[3]- Editar Producto")
        print("[0]- Salir")
        print("")
        varOpcion=int(input("Ingrese una Opcion: "))
        if varOpcion==1:
            borrarpantalla()
            altaProducto(productos)
        elif varOpcion==2:
            borrarpantalla()
            varBorrarProductos= int(input("Ingrese el codigo del Producto a eliminar: "))
            borrarProductos(productos, varBorrarProductos)
        elif varOpcion==6:
            borrarpantalla()
            varEditarProductos= int(input("Ingrese el codigo del Producto a Editar: "))
            borrarpantalla()
            for item in productos:
                if item['codigo']==varEditarProductos:
                    modificarProductos(productos,item['codigo'])#EDITAR PRODUCTOS CON MENU
                    #editarProducto(productos,item)#EDITAR PRODUCTOS SIN MENU
                    break
            else:
                borrarpantalla()
                print("EL CODIGO DE PRODUCTO NO EXISTE")
                pausa_con_respuesta()
                borrarpantalla()

        elif  varOpcion==0:
            borrarpantalla()
            break
            
        else:
            print("Valor Incorrecto")
               
def menu_reportes():
    borrarpantalla()
    while True:  
        titulo("menú de reportes")
        
        print("[1]- Listar los Productos")
        print("[2]- Busqueda por Descripcion Producto")     
        print("[3]- Valorizar Stock")     
        print("[4]- Generar archivo .TXT")
        print("[0]- Salir")
        print("")
        varOpcion=int(input("Ingrese una Opcion: "))
        if varOpcion==1:
            borrarpantalla()
            listarProductos(productos)
        elif varOpcion==2:
            borrarpantalla()
            varCriterioBusq=input("Ingrese la Busqueda por Descripcion de Producto: ")
            borrarpantalla()
            busquedaProductos(productos,varCriterioBusq)
        elif varOpcion==3:
            borrarpantalla()
            valorizarStock(productos)
        elif varOpcion==4:
            generareportetxt(productos,"listastock.txt")
        elif  varOpcion==0:
            borrarpantalla()
            break
            
        else:
            print("Valor Incorrecto")

while True:
    titulo("python frereteria")
    print("[1]- Menú de gestión")
    print("[2]- Menú de reportes")
    print("[0]- SALIR ")

    varOpcion=int(input("Ingrese una Opcion: "))
    if varOpcion==1:
        borrarpantalla()
        menu_gestion()
    elif varOpcion==2:
        borrarpantalla()
        menu_reportes()
    elif  varOpcion==0:
           titulo("hasta pronto!")
           break 
    else:
        print("Valor Incorrecto")
    ###########################################################################


        