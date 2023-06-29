def tablaProductos(lista):
    print()
    print("┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ CÓDIGO ┃                  PRODUCTO                   ┃")
    print("┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
    for producto in lista:
        print(f"│{producto['codigo']:^8}│ {(producto['producto']).title():<44}│")
        print("├────────┼─────────────────────────────────────────────┤")

def decorarConCuadrado(titulo):
    print("╔══" + "═" * len(titulo) + "══╗")
    print("║  " + " " * len(titulo) + "  ║")
    print(f"║  {titulo}  ║")
    print("║  " + " " * len(titulo) + "  ║")
    print("╚══" + "═" * len(titulo) + "══╝")

def decorarConCuadradoCh(titulo):
    print("┌──" + "─" * len(titulo) + "──┐")
    print(f"│  {titulo}  │")
    print("└──" + "─" * len(titulo) + "──┘")

def tablaCompleta():
    print()
    print("┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┓")
    print("┃ CÓDIGO ┃                  PRODUCTO                   ┃     CATEGORÍA     ┃ CANTIDAD ┃   PRECIO   ┃")
    print("┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━┩")

def tablaCantidad():
    print()
    print("┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ CANTIDAD ┃                  PRODUCTO                   ┃")
    print("┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")

def tablaCategoria():
    print()
    print("┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃     CATEGORÍA     ┃                  PRODUCTO                   ┃")
    print("┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")