import os
import json
# ------ Ingreso de Usuario y validacion ----------- #
def altaLogin():
    ingreso = False
    intento = 1
    print("INGRESO AL SISTEMA")
    while not ingreso:
        if intento < 4:
            usuario = input("\nIngrese USUARIO o escriba: 'NUEVO' para generar uno: ").upper()
            if usuario == "NUEVO":
                users = open("users.json", "r")
                listaUsers = json.load(users)
                os.system("cls")
                print("╔"+"═"*17+"╗")
                print("# ALTA DE USUARIO #")
                print("╚"+"═"*17+"╝")
                alta = False
                while not alta:
                    nuevoUsuario = input("Escriba usuario nuevo: ").upper()
                    for dic in listaUsers:
                        if nuevoUsuario == dic['usuario']:
                            print("¡ATENCIÓN! Usuario no disponible\n")
                            break
                    else:
                        pswd = False
                        while not pswd:
                            nuevaContrasenia = input("Escriba la contraseña: ")
                            os.system("cls")
                            if nuevaContrasenia == nuevoUsuario.lower():
                                print("¡ATENCIÓN! La contraseña no puede ser igual al usuario\n")
                            else:
                                print("¡USUARIO GENERADO CORRECTAMENTE!\nAHORA INGRESE AL SISTEMA.")
                                pswd = True
                                alta = True
                #se crea diccionario para usurio
                usuarioNuevo = {
                    "usuario": nuevoUsuario,
                    "contrasenia": nuevaContrasenia
                }
                listaUsers.append(usuarioNuevo)
                users = open("users.json", "w")
                json.dump(listaUsers, users, indent=2)
            else:
                contrasenia = input("Escriba la contraseña: ")
                valid=[{
                    "usuario": usuario,
                    "contrasenia": contrasenia
                }]
                # validación
                users = open("users.json", "r")
                listaUsers = json.load(users)
                for linea in valid:
                    if linea in listaUsers:
                        os.system("cls")
                        print(f"¡INGRESO CORRECTO! BIENVENIDO/A {usuario}.")
                        ingreso = True
                        break
                    else:
                        os.system("cls")
                        print(f"NO PUDIMOS RECONOCERLO/A. INTENTOS RESTANTES > {3 - intento}")
                        intento += 1
        else:
            print("#"*19)
            print("# ACCESO DENEGADO #")
            print("#"*19)
            exit()
    users.close()