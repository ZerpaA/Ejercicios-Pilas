# Se define la clase Pila
class Pila:
    # El método __init__ se ejecuta al crear una nueva instancia de la clase
    def __init__(self):
        # Se inicializa una lista vacía para almacenar los elementos de la pila
        self.items = []

    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        # Devuelve True si la longitud de la lista items es igual a 0, lo que significa que la pila está vacía
        return len(self.items) == 0

    # Método para agregar un elemento a la pila
    def apilar(self, elemento):
        # Se agrega el elemento al final de la lista items
        self.items.append(elemento)

    # Método para eliminar el último elemento de la pila y devolverlo
    def desapilar(self):
        # Si la pila está vacía, devuelve None
        if self.esta_vacia():
            return None
        # De lo contrario, utiliza el método pop de la lista para eliminar y devolver el último elemento de la lista items
        return self.items.pop()

# Se crea una nueva instancia de la clase Pila llamada pila_numeros
pila_numeros = Pila()

# Función para imprimir los elementos actuales de la pila
def imprimir_pila():
    # Si la pila está vacía, imprime un mensaje indicando que está vacía
    if pila_numeros.esta_vacia():
        print("La pila está vacía")
    else:
        # De lo contrario, imprime cada elemento de la lista items en orden inverso utilizando un bucle for y la función reversed
        print("Elementos actuales de la pila:")
        for numeros in reversed(pila_numeros.items):
            print(numeros)

# Bucle infinito para mostrar el menú al usuario
while True:
    print("\n===============")
    print("  MENÚ PRINCIPAL")
    print("===============")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Imprimir pila")
    print("4. Salir")

    # El usuario puede seleccionar una opción ingresando su número correspondiente
    opcion = input("Selecciona una opción: ")

    # Si el usuario selecciona la opción 1, se le pedirá que ingrese un número y se agregará a la pila utilizando el método apilar
    if opcion == "1":
        numero = input("Ingresa un numero: ")
        pila_numeros.apilar(numero)
        print(f"Numero {numero} agregado a la pila.")
    # Si el usuario selecciona la opción 2, se eliminará el último elemento de la pila utilizando el método desapilar
    elif opcion == "2":
        numero_eliminado = pila_numeros.desapilar()
        if numero_eliminado is None:
            print("La pila está vacía")
        else:
            print(f"Numero {numero_eliminado} eliminado de la pila.")
    # Si el usuario selecciona la opción 3, se llamará a la función imprimir_pila
    elif opcion == "3":
        imprimir_pila()
    # Si el usuario selecciona la opción 4, se romperá el bucle y se saldrá del programa
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    # Si el usuario ingresa una opción no válida, se mostrará un mensaje indicando que la opción no es válida y se le pedirá que intente de nuevo.
    else:
        print("Opción no válida. Inténtalo de nuevo.")
