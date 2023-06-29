# ------ Variables, librerias y estados iniciales globales ------ #
import os
import json
import loginModulo
import deco
import abm
import reportesMod

# ----- lista de Productos ----- #
productos = open("ProductosAlmacen.json", "r")
listaProductos = json.load(productos)
productos.close()
 
# ----- PROGRAMA ----- #
loginModulo.altaLogin()
while True:
    deco.decorarConCuadrado("LISTA DE PRODUCTOS DEL GRUPO B")
    print()
    print(" [1] Gestión de Productos \n [2] Reportes \n [3] Acerca de... \n [0] Salir. \n ")

    opcionMenuGeneral = int(input("Seleccione una de las opciones anteriores: "))
    print()
    if opcionMenuGeneral == 0:
        os.system("cls")
        break

    elif opcionMenuGeneral == 1:
       
        while True:
            os.system("cls")
            deco.decorarConCuadrado("Gestión de Producto")
            print()
            print(" [1] Nuevo Producto \n [2] Modificar Producto \n [3] Eliminar producto \n [0] Volver al Menú Principal  \n ")
            opcionGestionProducto = int(input("Seleccione una de las opciones anteriores: "))
            if opcionGestionProducto == 0:
                os.system("cls")
                break
            elif opcionGestionProducto == 1:
                os.system("cls")
                deco.decorarConCuadrado("Nuevo Producto")
                abm.agregarProducto(listaProductos) 
            elif opcionGestionProducto == 2:
                os.system("cls")
                deco.decorarConCuadrado("Modificar Producto")
                deco.tablaProductos(listaProductos)
                abm.ModificarProducto(listaProductos)                
            elif opcionGestionProducto == 3:
                os.system("cls")
                deco.decorarConCuadrado("Eliminar Producto")
                abm.EliminarProducto(listaProductos)
        
    elif opcionMenuGeneral == 2:
       
        while True:
            os.system("cls")
            deco.decorarConCuadrado("Reportes")
            print()
            print(" [1] Productos por Código \n [2] Productos por Categoría \n [3] Producto por Cantidad \n [4] Productos por Nombre \n [0] Volver al Menú Principal \n ")
            
            opcionReporteProd = int(input("Seleccione una opción: "))

            if opcionReporteProd == 0:
                os.system("cls")
                break
            elif opcionReporteProd == 1:
                print("Productos por código")
                reportesMod.productoPorCodigo()
            elif opcionReporteProd == 2:
                print("Productos por Categoría")
                reportesMod.productoPorCategoria()
            elif opcionReporteProd == 3:
                print("Productos por Cantidad")
                reportesMod.productoPorCantidad()
            elif opcionReporteProd == 4:
                print("Productos por Nombre")
                reportesMod.productoPorNombre()
    elif opcionMenuGeneral == 3:
        os.system("cls")
        reportesMod.staff()
            
    else: print("Introduzca una opción válida.")

print("¡GRACIAS POR USAR NUESTRO PROGRAMA!")
print("\nFIN  DEL PROGRAMA - Gestión de Productos by Grupo B\n")