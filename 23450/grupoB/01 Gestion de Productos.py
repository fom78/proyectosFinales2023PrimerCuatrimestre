

print("-----------------------------------")
print("- LISTA DE PRODUCTOS  DEL GRUPO B - ")
print("-----------------------------------")
print()

while True:
    print(" 1. Gestion de Productos \n 2. Reporte \n 3. Hacer pedido \n 0. Salir. \n ")

    opcion = int(input("Seleccione una de las opciones anteriores: "))
    print()
    
    if opcion == 1:
       print()
       print("Gestion de Producto")
       print()
       print(" 1. Nuevo Producto \n 2. Modificar Producto \n 3. Elilinar prodcuto \n 4. Volver al Menu Principal  \n ")
       break
    elif opcion == 2:
       print()
       print("Reportes")
       print()
       print(" 1. Productos \n 2. Pedidos. \n 3. Volver al Menu Principal  \n ")
              
       reportesOpcion = int(input("Selccione una Opcion: "))
       if reportesOpcion == 1:
           print()
           print("Productos")
           print()
           print(" 1. Productos por Codigo \n 2. Productos por Categoria. \n 3. Producto por Cantindad \n 4. Producto por noombre \n 5. Volver a Reportes. \n ")
           break
       elif reportesOpcion ==2:
           print()
           print("Pedidos")
           print()
           print(" 1. Pedidos Entregados. \n 2. Pedidos por Entregar. \n 3. Pedidos segun Categoria  \n ")
           break
       elif reportesOpcion == 3:
           print("debe volver al menu Principal")
           break

    elif opcion == 3:
       print()
       print("Hacer pedido")
       print()
       print(" 1. Nuevo Pedido. \n 2. Mis Pedidos.  \n 3. Cancelar Pedido \n 4. Volver al Menu Principal  \n ")
       
       pedidoOpcion = int(input("Seleccione Opcion: "))
       if pedidoOpcion == 1:
           print("nuevo pedido aca")
       elif pedidoOpcion == 2:
           print("Mis Pedidos")
       elif pedidoOpcion == 3:
           print("Cancelar Pedido")
       elif pedidoOpcion == 4:
           print("Volver al Menu Principal")
           break
        
    elif opcion == 0:
        break
    else: print("Introduce una opcion valida.")