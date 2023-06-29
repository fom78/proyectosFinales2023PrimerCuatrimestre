import Funciones as f

productos= []

while True:
    f.menuInicioA()
    opcion = f.opcion_numero()
    empleados = f.datos_empleados()
  
    if opcion == 1:
      f.alta(empleados)

    elif opcion == 2:
      if f.sesion(empleados) == True:
         productos = f.datos_productos()
         f.menuDelPrograma()
         
    elif opcion == 0: 
      break
    
    else:
        print("Ingresa una opcion Valida")