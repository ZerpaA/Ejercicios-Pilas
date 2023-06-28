# Se define la clase Pila
class Pila:
    # El método __init__ se ejecuta al crear una instancia de la clase Pila
    def __init__(self):
        # Se inicializa una lista vacía para almacenar los elementos de la pila
        self.items = []

    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        # Devuelve True si la longitud de la lista de elementos es cero, es decir, si está vacía
        return len(self.items) == 0

    # Método para apilar un elemento en la pila
    def apilar(self, elemento):
        # Se agrega el elemento al final de la lista de elementos
        self.items.append(elemento)

    # Método para desapilar un elemento de la pila
    def desapilar(self):
        # Si la pila está vacía, devuelve None
        if self.esta_vacia():
            return None
        # Si no está vacía, se elimina y devuelve el último elemento de la lista de elementos
        return self.items.pop()

# Se crea una instancia de la clase Pila llamada pila_nombres
pila_nombres = Pila()

# Función para imprimir el contenido de la pila
def imprimir_pila():
    # Si la pila está vacía, se imprime un mensaje indicándolo
    if pila_nombres.esta_vacia():
        print("La pila está vacía")
    else:
        # Si no está vacía, se imprime el contenido de la pila en orden inverso (el último elemento apilado es el primero en imprimirse)
        print("Estado de la pila:")
        for nombre in reversed(pila_nombres.items):
            print(nombre)

# Función para contar la cantidad de nombres iguales en la pila
def contar_nombres_iguales():
    # Si la pila está vacía, se imprime un mensaje indicándolo
    if pila_nombres.esta_vacia():
        print("La pila está vacía")
    else:
        # Si no está vacía, se crea un diccionario para almacenar el conteo de cada nombre
        contador_rep = {}
        for elemento in pila_nombres.items:
            if elemento in contador_rep:
                contador_rep[elemento] += 1

            else:
                contador_rep[elemento] = 1
        # Se imprime el diccionario con el conteo de cada nombre
        print(contador_rep)

# Función para contar la cantidad de nombres que comienzan con la letra "L"
def contar_nombres_con_l():
    # Si la pila está vacía, se imprime un mensaje indicándolo
    if pila_nombres.esta_vacia():
        print("La pila está vacía")
    else:
        
        cantidad = sum(1  for nombre in pila_nombres.items if nombre.startswith("l")) + sum(1  for nombre in pila_nombres.items if nombre.startswith("L"))
        print(f"Cantidad de nombres que comienzan con L: {cantidad}")

# Bucle infinito para mostrar el menú principal y permitir al usuario interactuar con el programa
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

    # Se solicita al usuario que ingrese una opción del menú
    opcion = input("Selecciona una opción: ")

    # Se verifica qué opción eligió el usuario y se ejecuta el código correspondiente a esa opción
    if opcion == "1":
        nombre = input("Ingresa un nombre: ")
        nombre.lower()
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
