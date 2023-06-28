class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()


pila_nombres = Pila()

def imprimir_pila():
    if pila_nombres.esta_vacia():
        print("La pila está vacía")
    else:
        print("Estado de la pila:")
        for nombre in reversed(pila_nombres.items):
            print(nombre)

def contar_nombres_iguales():
    if pila_nombres.esta_vacia():
        print("La pila está vacía")
    else:
        contador_rep = {}
        for elemento in pila_nombres.items:
            if elemento in contador_rep:
                contador_rep[elemento] += 1

            else:
                contador_rep[elemento] = 1
        print(contador_rep)

def contar_nombres_con_l():
    if pila_nombres.esta_vacia():
        print("La pila está vacía")
    else:
        
        cantidad = sum(1  for nombre in pila_nombres.items if nombre.startswith("l")) + sum(1  for nombre in pila_nombres.items if nombre.startswith("L"))
        print(f"Cantidad de nombres que comienzan con L: {cantidad}")


while True:
    print("\n===============")
    print("  MENÚ PRINCIPAL")
    print("===============")
    print("1. Agregar nombre")
    print("2. Eliminar nombre")
    print("3. Imprimir pila")
    print("4. Cantidad de nombres iguales")
    print("5. Cantidad de nombres que comienzan con L")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Ingresa un nombre: ")
        nombre.lower
        pila_nombres.apilar(nombre)
        print(f"Nombre {nombre} agregado a la pila.")
    elif opcion == "2":
        nombre_eliminado = pila_nombres.desapilar()
        if nombre_eliminado is None:
            print("La pila está vacía")
        else:
            print(f"Nombre {nombre_eliminado} eliminado de la pila.")
    elif opcion == "3":
        imprimir_pila()
    elif opcion == "4":
        contar_nombres_iguales()
    elif opcion == "5":
        contar_nombres_con_l()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")