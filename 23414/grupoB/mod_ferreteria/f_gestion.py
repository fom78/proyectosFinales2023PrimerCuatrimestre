import json
from mod_ferreteria.f_esteticas import *
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)
######################################################################
#FUNCION DE CODIGO####################################################
def  ingresoCodigo(listado):
    while True:
        while True:
            try: 
                codigoAlta=int(input("Ingrese el codigo del Producto: "))
                break
            except:
                print("El codigo debe ser un numer entero")
        for item in listado:
            if item["codigo"]==codigoAlta:
                print("el codigo ya existe")
                break 
        else:
                varCodigo=codigoAlta
                break

######################################################################
#ALTA DE PRODUCTOS####################################################
def  altaProducto(listado):
    titulo("Alta de Producto")
    print()
    while True:
        while True:
            try: 
                borrarpantalla()
                print("Alta de Producto")
                print()
                codigoAlta=int(input("Ingrese el codigo del Producto: "))
                break
            except:
                print("El codigo debe ser un numer entero")
        for item in listado:
            if item["codigo"]==codigoAlta:
                print()
                print("el codigo ya existe")
                print()
                pausa_con_respuesta()
                borrarpantalla()
                break 
        else:
                varCodigo=codigoAlta
                break
    #varCodigo=ingresoCodigo()
    varCategoria=control_categoria()
    varDescripcion=input("Ingrese la Descripcion del Producto: ")
    while True: 
      try:
        varCantidad=int(input("Ingrese la cantidad del Producto: "))
        break
      except:
          print("La codigo debe ser un entero.")
    while True: 
      try:      
        varPrecioUnit=float(input("Ingrese el Precio del Producto: "))
        break
      except:
        print("El precio debe ser un numero")
    while True: 
      try:      
        varPrecioVPublico=float(input("Ingrese el Precio Venta al Publico: "))
        break
      except:
        print("El precio debe ser un numero")
    item = {
        "cantidad": varCantidad,
        "categoria": varCategoria,
        "codigo": varCodigo,
        "descripcion": varDescripcion,
        "precioUnit": varPrecioUnit,
        "precioVPublico": varPrecioVPublico
    }
    borrarpantalla()
    print()
    print("NUEVO ITEM INGRESADO")
    encabezado()
    cuerpo(item)
    pie()
    listado.append(item)
    arch = open("stockFerreteria.json","w")
    json.dump(listado,arch, indent=2)  
    arch.close()
    pausa_con_respuesta()
    borrarpantalla()
##############################################################
#LISTAR PRODUCTOS#############################################

######################################################################
#BORRAR PRODUCTOS#####################################################
def borrarProductos(listado,caracteres):
    titulo("PRODUCTO ELIMINADO")
    encabezado()
    for item in listado:
        if caracteres == item ["codigo"]:
            cuerpo(item)
            listado.remove(item)
            arch = open("stockFerreteria.json","w")
            json.dump(listado,arch, indent=2)  
            arch.close()
    pie()
    pausa_con_respuesta()
######################################################################
#VALORIZAR STOCK######################################################
def valorizarStock(listado):
    titulo("valor del stock")
    valorTotalStock=0
    for item in listado:
        valorItemStock=item["cantidad"]*item["precioUnit"]
        valorTotalStock=valorTotalStock+valorItemStock
    print()
    print(f"EL VALOR TOTAL DEL STOCK ES DE: ${valorTotalStock:.2f}")
    print()
    pausa_con_respuesta()
    borrarpantalla()
######################################################################
#EDITAR PRODUCTO CON MENU#############################################   

def modificarProductos(listado, codigo_mod):
    titulo("modificar producto")
    
    for producto in listado:       
        if producto['codigo'] == codigo_mod:
            encabezado()
            cuerpo(producto)
            pie()
            modificar = input (f""" 
            ¿Que deseas modificar?
            
            [1] CODIGO: {producto['codigo']}
            [2] CATEGORIA: {producto['categoria']}
            [3] CCANTIDAD: {producto['cantidad']} 
            [4] DESCRIPCION: {producto['descripcion']}
            [5] PRECIO: {producto['precioUnit']}
            [6] PVP: {producto['precioVPublico']}
            [ ] Otro para salir  
            
            >>> """)
            print()
            match modificar:
                case "1": 
                    producto['codigo'] = int(input("Ingrese el Nuevo Codigo de producto: "))
                    borrarpantalla()  
                case "2":
                    producto['categoria'] = control_categoria() 
                    borrarpantalla()
                case "3":
                    producto['cantidad'] = int(input("Ingrese la cantidad del Producto: ")) 
                    borrarpantalla()
                case "4":
                    producto['descripcion'] = input("Nueva descripcion: ") 
                    borrarpantalla()
                case "5":
                    producto['precioUnit'] = float(input("Ingrese el Precio del Producto: "))
                    borrarpantalla() 
                case "6":
                    producto['precioVPublico'] = float(input("Ingrese el Precio Venta al Publico: "))
                    borrarpantalla()
                case _:
                    borrarpantalla()
                    break
            encabezado()
            cuerpo(producto)
            #print (f"|{producto['codigo']:6}  | {producto['categoria']:<12} | {producto['cantidad']:7} | {producto['descripcion']:<40} |  {producto['precioUnit']:10.2f} | {producto['precioVPublico']:10.2f}|")
            pie()
            pausa_con_respuesta()
    arch = open("stockFerreteria.json","w")
    json.dump(listado,arch,indent= 2) 
    arch.close() 
    
######################################################################
#EDITAR PRODUCTO SIN MENU#############################################

def editarProducto(listado, producto):
    titulo("EDITAR PRODUCTO")
    print()
    varCodigo=int(input(f"Ingrese el nuevo codigo({producto['codigo']}) o 0 para no modificar:"))
    if varCodigo!=0:
        producto['codigo']=varCodigo
    varCategoria=input(f"ingrese la nueva categoria del Producto({producto['categoria']}): ")
    if varCategoria !="":
        producto['categoria']=varCategoria
    else:
        producto['categoria']=producto['categoria']
    varDescripcion=input("Ingrese la Descripcion del Producto: ")
    if varDescripcion != "":
        producto['descripcion']=varDescripcion
    else :
        producto['descripcion']=producto['descripcion']
    varPrecioUnit=float(input(f"Ingrese el Nuevo Precio({producto['precioUnit']:.2f}) o 0 para no modificar: "))
    if varPrecioUnit!=0:
        producto['precioUnit']=varPrecioUnit
    varPrecioVPublico=float(input(f"Ingrese el Nuevo PVP({producto['precioVPublico']:.2f}) o 0 para no modificar: "))
    if varPrecioVPublico!=0:
        producto['precioVPublico']=varPrecioVPublico
    
    arch = open("stockFerreteria.json","w")
    json.dump(listado,arch, indent=2)  
    arch.close()
    borrarpantalla()
    print()
    encabezado()
    cuerpo(producto)
    pie()
    print()
    pausa_con_respuesta()
    borrarpantalla()
    
