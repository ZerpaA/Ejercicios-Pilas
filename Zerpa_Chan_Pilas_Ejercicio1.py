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

pila_numeros = Pila()

def imprimir_pila():
    if pila_numeros.esta_vacia():
        print("La pila está vacía")
    else:
        print("Elementos actuales de la pila:")
        for numeros in reversed(pila_numeros.items):
            print(numeros)

while True:
    print("\n===============")
    print("  MENÚ PRINCIPAL")
    print("===============")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Imprimir pila")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        numero = input("Ingresa un numero: ")
        pila_numeros.apilar(numero)
        print(f"Numero {numero} agregado a la pila.")
    elif opcion == "2":
        numero_eliminado = pila_numeros.desapilar()
        if numero_eliminado is None:
            print("La pila está vacía")
        else:
            print(f"Numero {numero_eliminado} eliminado de la pila.")
    elif opcion == "3":
        imprimir_pila()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")