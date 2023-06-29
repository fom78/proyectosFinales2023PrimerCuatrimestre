
'''BIENVENIDO PODRA INGRESAR CON EL 
USUARIO=JUAN
CONTRASEÑA=1234'''


import gestion
import os

dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)

#Para invocar Menú de Usuario   
     
def menu_Usuario():
 while True:
  gestion.decorar(2)
  print("""

            :::Menú:::
          ::::Usuario::::

        [1] - Gestión de Productos 
        [2] - Reportes 
        [0] - Salir
         """)
  opcionUsuario=gestion.inputEntero("Ingrese una opción: ")
  if opcionUsuario==1:
    menuGestion()
  elif opcionUsuario==2:
    menuReportes()  
  elif opcionUsuario==0:
    gestion.decorar(2)
    print("¡Gracias por utilizar la app del Grupo A!!-PS D:\CodoACodo> Grupo A")
    exit()   
  else:
    gestion.decorar(2)
    print("Opción inválida. Intente de nuevo")
    

def menuGestion():
    while True:
      print("""

              :::Menú:::
            ::::Gestión::::

        [1] - Ingresar nuevo producto 
        [2] - Modificar un producto 
        [3] - Eliminar un producto   
        [4] - Ver inventario
        [0] - Volver al menú principal
        """)
      opcionGestion=gestion.inputEntero("Ingrese una opción: ")
      if opcionGestion==1:
        gestion.decorar(2)
        print("A G R E G A R  P R O D U C T O".center(40,))
        gestion.ingresarNuevoProducto()
        gestion.decorar(2)
      elif opcionGestion==2:
        gestion.decorar(2)
        print("M O D I F I C A R   P R O D U C T O".center(40,))
        gestion.modificarProducto()
        gestion.decorar(2)
      elif opcionGestion==3:
        gestion.decorar(2)
        print("E L I M I N A R  P R O D U C T O".center(40,))
        gestion.eliminarProducto()
        gestion.decorar(2)
      elif opcionGestion==4:
        gestion.decorar(2)
        print("V E R  I N V E N T A R I O".center(40,))
        gestion.verInventario()
        gestion.decorar(2)
      elif opcionGestion==0:    
         break
      else:
        print("Ingresá una opción válida![0-5]")
        gestion.decorar(2)


def menuCategorias():
  while True:
    print("""
          CATEGORIAS:
          [1]  Accesorios para el Hogar
          [2]  Contruccion
          [3]  Cerradura y Seguridad
          [4]  Ferreteria y jardin
          [5]  Electricidad
          [6]  Fontaneria
          [7]  Pintura y Accesorios
          [8]  Material de fijacion
          [9]  Equipos de Seguridad
          [10] Herramientas Electricas
          [11] Herramientas Manuales
          [0] Salir
          """)
    entero=gestion.inputEntero("Ingrese la categoria que desea buscar: ")
    if entero ==0:
      break
    elif entero >=1 and entero <=11:
      catBuscada=gestion.categoriasXNro(entero)
      gestion.verProductoPor("categoria",catBuscada)
    else:
      print("Ingrese una opción válida")


def menuReportes():
  while True:
    gestion.decorar(2)
    print("""

               :::Menú:::
            ::::Reportes::::
           
            [1] Mostrar productos nacionales
            [2] Mostrar productos importados
            [3] Mostrar productos con stock limitado
            [4] Mostrar productos sin stock
            [5] Mostrar productos por categoria
            [0] Volver al menú principal
            """)
    opcionReportes=gestion.inputEntero("Ingrese una opción: ")
    if opcionReportes==0:
      break
    elif opcionReportes==1:
      gestion.verProductoPor("nacional",True)
    elif opcionReportes==2:
      gestion.verProductoPor("nacional",False)
    elif opcionReportes==3:
      gestion.stockLim()
    elif opcionReportes==4:
      gestion.verProductoPor("cantidad",0)
    elif opcionReportes==5:
      menuCategorias()
    else:
      print("Ingrese una opción válida [0-5]")
      gestion.decorar(2)
      

def menu_Cliente(): 
  import random
  while True:
    gestion.decorar(2)
    print('''

              :::Menú:::
          :::::Clientes:::::

      [1] - Ver producto y stock
      [2] - Generar una compra
      [0] - Salir''')
    opcion=gestion.inputEntero("Ingrese una opción: ")
    if opcion==0:
      break
    elif opcion==1:
      print("Ver que puedo comprar")
      repuesto=input("ingrese el nombre del producto que necesita: ")
      print("Contamos con stock continue para realizar su compra")
      print("por favor proceda a consultar las diferentes formas de pago!!")
    elif opcion==2:
      mercaderia=input("ingrese el nombre de el producto que necesita: ")
      cantidad=input("ingrese cantidad de producto que necesita: ")
      valor=random.randint(3000,12000)
      valor=round(valor)
      print("su compra de ",cantidad,mercaderia," tiene un  valor total de" ,valor," pesos, a continuación le brindaremos las diferentes formas de pagos. ")
      while True:
        gestion.decorar(2)
        print("""

                  :::METODOS:::
                 ::::DE PAGO::::

              [1] - EFECTIVO
              [2] - 3 CUOTAS SIN INTERES 
              [3] - 12 CUOTAS CON 10% DE INTERES
              [0] - SALIR
          """)
        opcion=gestion.inputEntero("Ingrese una opción: ")
        if opcion==0:
          break
        elif opcion==1:
          descuentoAzar=random.randint(15,25)
          descuento=valor*(descuentoAzar/100)
          precioFinal=round(valor-descuento)
          print("Descuento del dia del", descuentoAzar,"% , Ud debe abonar ",precioFinal,"pesos ")
          print("Si desea realizar la compra por favor comuniquese al 12345666 con el área de compras")
          print("Gracias por elegirnos!!")
          break
        elif opcion==2:
          cuotas=round( valor/3)
          print("El valor de cada cuota es" ,cuotas, "pesos")
          print("Si desea realizar la compra por favor comuniquese al 12345666 con el área de compras")
          print("Gracias por elegirnos!!")
          break
        elif opcion==3:
          cuotasConInteres=round((valor*1.10)/12)
          print("Ud debera pagar 12 cuotas de", cuotasConInteres," pesos")
          print("Si desea realizar la compra por favor comuniquese al 12345666 con el área de compras")
          print("Gracias por elegirnos!!")
          break
     
#inicio    
while True:
  gestion.decorar(1)
  print("Bienvenido al programa de gestión de stock del grupo A".center(60,))
  print('''

            :::Menú:::
          ::::Inicial::::

        [1] Crear usuario
        [2] Iniciar sesión
        [0] Salir''')
  gestion.decorar(2)
  opcion=gestion.inputEntero("Ingrese una opción: ")
  if opcion==0:
    print("¡Gracias por utilizar nuestra app!PS D:\CodoACodo>Grupo A")
    break
  elif opcion==1:
    gestion.decorar(2)
    print("Crear Usuario")
        
    logins=[]
    usuario=input("Ingrese nombre de usuario: ")
    contrasena=input("Ingrese contraseña: ")

    logins={
    "usuario":usuario,
    "contraseña":contrasena,}
    print("Hola", usuario, "tu contraseña sera", contrasena, "por favor recorda anotar los datos para no olvidarte") 
    gestion.decorar(3)   

  elif opcion==2:
    gestion.decorar(2)
    print("Iniciar sesión")
    usuario="juan"
    contraseña="1234"
    
    from getpass import getpass
    
    nombre=input("Ingrese su usuario: ")
    nombre=nombre.strip()
    print("Para mantener de forma segura su contraseña su ingreso no se mostrara por pantalla,luego de digitarla ingrese con la tecla 'enter' ")
    password=getpass("Ingrese su contraseña: ")
    if password==contraseña and nombre==usuario:
      print("Bienvenido a la empresa")
      gestion.decorar(2)
      print("Hola",usuario, "bienvenid@ al menú de la empresa")
      gestion.decorar(2)
      menu_Usuario()
    else:
      print("Hola",nombre,"usted es un cliente por lo tanto podra ver los productos que tenemos y el stock con el que cuenta para realizar su compra")
      menu_Cliente()

        
        
        
        
        
        
        
        
 
              

     
         

  

    









        

    

