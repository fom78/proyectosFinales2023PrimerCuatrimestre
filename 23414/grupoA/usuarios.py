#FUNCIONES DEL MODULO: ***COMPLETAR***
#abm_usuarios
#alta_usuarios
#baja_usuarios
#modificacion_usuarios
# ~ #listar_usuarios (usuarios [{}]) lista por pantalla de usuarios (usuario, clave)
#usuario_existente
#alta_clave
#clave_valida

from general import *

###############################################################################
###   USUARIOS                                                              ###
###############################################################################
def listar_usuarios(usuarios):
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', 'Listado de Usuarios Registrados']]
    menu+=[['com_*']]
    menu+=[['com_n']]
    menu+=[['com_<', f"{'Usuario':20}  {'Clave':20}"]]
    menu+=[['com_<', f"{'='*20}  {'='*20}"]]
    for usuario in usuarios:
        menu+=[['com_<', f"{usuario['usuario']:20}  {usuario['clave']:20}"]]
    menu+=[['com_n']]
    mostrar_menu(menu)
    pausa()

#requisitos para contraseñas:
#    - al menos 4 caracteres
#    - sin espacios en blanco
#    - se pueden agregar mas...
def clave_valida(clave):
    tiene_blancos=False
    for caracter in clave:
        if caracter.isspace():
            tiene_blancos=True
    if len(clave)<4 or tiene_blancos:
        print('La contraseña no puede tener espacios en blanco y debe tener al menos 4 caracteres')
        pausa()
        return False
    else:
        return True

#creacion de contraseñas
def alta_clave(usuario, tope):
    intentos_ingreso=0
    while True:
        intentos_ingreso+=1
        nueva_clave=getpass(f'Ingrese una contraseña para {usuario}: ')
        if clave_valida(nueva_clave):
            intentos_ingreso=0
            while True:
                intentos_ingreso+=1
                confirma_clave=getpass('Reingrese la contraseña para su validación: ')
                if nueva_clave==confirma_clave:
                    return nueva_clave
                else:
                    print('Las contraseñas ingresadas no coinciden.')
                    if intentos_ingreso<tope:
                        oportunidad='oportunidad'+'' if tope-intentos_ingreso==1 else 'es'
                        print(f"Tiene {tope-intentos_ingreso} {oportunidad} más para reingresar su contraseña.")
                        pausa()
                        continue
                    else:
                        nueva_clave=''
                        print('El ingreso de la contraseña ha fallado.')
                        pausa()
                        return ''
        else:                
            if intentos_ingreso<tope:
                oportunidad='oportunidad'+'' if tope-intentos_ingreso==1 else 'es'
                print(f"Tiene {tope-intentos_ingreso} {oportunidad} más para ingresar su contraseña.")
                pausa()
                continue
            else:
                print('El ingreso de la contraseña ha fallado.')
                pausa()
                return ''

#devuelve True si el usuario esta registrado
def usuario_existente(usuarios, usuario_buscado):
    for usuario in usuarios:
        if usuario['usuario']==usuario_buscado:
            return True
    return False

#usuarios: {'usuario':str, 'clave':str}
def alta_usuarios(usuarios, tope):
    intentos_ingreso=0
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', 'Alta de Usuarios Registrados']]
    menu+=[['com_*']]
    menu+=[['com_n']]
    menu+=[['com_i', 'Ingrese el nuevo usuario: ']]
    while True:
        intentos_ingreso+=1
        nuevo_usuario=mostrar_menu(menu).strip()
        #sin usuario, reintentar
        if nuevo_usuario=='':
            if intentos_ingreso>=tope:
                print('Falló en el ingreso de un nuevo usuario.')
                pausa()
                break
            else:
                print('Debe ingresar un usuario.')
                oportunidad='oportunidad'+'' if tope-intentos_ingreso==1 else 'es'
                print(f"Tiene {tope-intentos_ingreso} {oportunidad} más para ingresar un usuario.")
                pausa()
                continue
        else:
            #verificar si el nuevo usuario ya existe
            if usuario_existente(usuarios, nuevo_usuario):
                print('El usuario ya existe.')
                pausa()
                break
            #usuario nuevo
            else:
                nueva_clave=alta_clave(nuevo_usuario, tope)
                if nueva_clave=='':
                    print(f'Falló el ingreso de una contraseña valida para {nuevo_usuario}.')
                    pausa()
                else:
                    usuario={'usuario': nuevo_usuario, 'clave': nueva_clave}  #creo el nuevo usuario con los datos ingresados
                    usuarios.append(usuario)  #actualizo en memoria
                    usuarios=sorted(usuarios, key=lambda usuarios: usuarios['usuario'])
                    escribe_datos_json(usuarios, json_usuarios)  #actualizo en disco
                    listar_usuarios(usuarios)
                break

#usuarios: {'usuario':str, 'clave':str}
def baja_usuarios(usuarios):
    menu =[['com_*']]
    menu+=[['com_^', 'Sistema de Gestión de Stock']]
    menu+=[['com_^', 'Baja de Usuarios Registrados']]
    menu+=[['com_*']]
    menu+=[['com_n']]
    menu+=[['com_+', 'Ingrese el usuario a eliminar y luego presione ENTER, o solamente ENTER para salir.']]
    menu+=[['com_n']]
    menu+=[['com_i', 'Usuario a eliminar: ']]
    usuario_a_eliminar=mostrar_menu(menu)
    if usuario_a_eliminar=='admin':
        print('No es posible eliminar al usuario "admin".')
    elif usuario_existente(usuarios, usuario_a_eliminar):
        confirmar=input(f'ESTA SEGURO QUE QUIERE ELIMINAR AL USUARIO "{usuario_a_eliminar}"? (S/N): ').lower()
        if confirmar=='s':
            for usuario in usuarios:
                if usuario['usuario']==usuario_a_eliminar:
                    usuarios.remove(usuario)
            escribe_datos_json(usuarios, json_usuarios)
    listar_usuarios(usuarios)

#usuarios: {'usuario':str, 'clave':str}
def modificacion_usuarios(usuarios, tope):
    while True:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Modificación de Usuarios Registrados']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['com_i', 'Ingrese el usuario a modificar y luego presione ENTER: ']]
        usuario_a_editar=mostrar_menu(menu)
        nuevo_nombre=''
        if not usuario_existente(usuarios, usuario_a_editar):
            print(f'El usuario ingresado "{usuario_a_editar}" no esta registrado.')
            print('Use la opción "Alta de usuarios" si desea crear un nuevo usuario.')
            break
        elif usuario_a_editar=='admin':  #para el usuario admin solo se puede cambiar su contraseña
            nuevo_nombre=usuario_a_editar
            nueva_clave=alta_clave(nuevo_nombre, tope)
            if nueva_clave=='':
                print(f'Falló la actualización de contraseña para el usuario "{nuevo_nombre}".')
                break
        else:  #cambiar solamente contraseña o tambien el nombre del usuario
            print(f'Ingrese un nuevo nombre de usuario para "{usuario_a_editar}, ')
            print('o ENTER si solo desea actualizar su contraseña.')
            nuevo_nombre=input('Nuevo nombre de usuario: ')
            if nuevo_nombre=='':
                nuevo_nombre=usuario_a_editar
            #si se ingresa el nombre de otro usuario:
            elif usuario_existente(usuarios, nuevo_nombre):
                print(f'El usuario "{nuevo_nombre}" ya existe.')
                break
            nueva_clave=alta_clave(nuevo_nombre, tope)
            if nueva_clave=='':
                if nuevo_nombre!=usuario_a_editar:
                    print(f'Falló el cambio de nombre del usuario "{usuario_a_editar}" a "{nuevo_nombre}".')
                print(f'Falló la actualización de contraseña para el usuario "{nuevo_nombre}".')
                break
        for usuario in usuarios:
            if usuario['usuario']==usuario_a_editar:
                usuario['usuario']=nuevo_nombre
                usuario['clave']=nueva_clave
        usuarios=sorted(usuarios, key=lambda usuarios: usuarios['usuario'])
        escribe_datos_json(usuarios, json_usuarios)
        break
    listar_usuarios(usuarios)
    pausa()

#gestion de usuarios
def abm_usuarios(usuarios, intentos_ingreso_max):
    #usuarios: {'usuario':str, 'clave':str}
    clave_admin=''
    for usuario in usuarios:
        if usuario['usuario']=='admin':
            clave_admin=usuario['clave']
    if clave_admin=='':
        print('ERROR: NO EXISTE UN ADMINISTRADOR.')
        pausa()
    else:
        menu =[['com_*']]
        menu+=[['com_^', 'Sistema de Gestión de Stock']]
        menu+=[['com_^', 'Gestion de Usuarios Registrados']]
        menu+=[['com_*']]
        menu+=[['com_n']]
        menu+=[['com_p', 'Ingrese la contraseña de administrador: ']]
        clave_ingresada=mostrar_menu(menu)
        if clave_ingresada!=clave_admin:
            print('La gestion de usuarios está reservada al administrador.')
            pausa()
        else:
            menu.pop()
            menu+=[['1', 'Listado de usuarios']]
            menu+=[['2', 'Alta de usuarios']]
            menu+=[['3', 'Baja de usuarios']]
            menu+=[['4', 'Modificación de usuarios']]
            menu+=[['com_n']]
            menu+=[['0', 'Salir']]
            menu+=[['com_n']]
            menu+=[['com_i', 'Ingrese su consulta y luego presione ENTER: ']]
            while True:
                opcion=mostrar_menu(menu)
                if opcion=='1':
                    listar_usuarios(usuarios)
                elif opcion=='2':
                    alta_usuarios(usuarios, intentos_ingreso_max)
                elif opcion=='3':
                    baja_usuarios(usuarios)
                elif opcion=='4':
                    modificacion_usuarios(usuarios, intentos_ingreso_max)
                elif opcion=='0':
                    break

