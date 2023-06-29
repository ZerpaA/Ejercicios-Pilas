from datetime import date

class Producto:
    # Constructor de la clase Producto
    def __init__(self, codigo, descripcion, precio_unitario, fecha_ingreso):
         # Asignamos los valores de los argumentos a las variables de instancia
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.fecha_ingreso = fecha_ingreso

class Venta:

    def __init__(self, producto, cantidad, fecha_venta):
        self.producto = producto
        self.cantidad = cantidad
        self.fecha_venta = fecha_venta
        self.precio_total = producto.precio_unitario * cantidad

class Inventario:
    def __init__(self):
         # Inicializamos dos listas vacías:una para almacenar los productos del inventario y otra para las ventas
        self.productos = []
        self.ventas = []

    # Función para registrar un producto en el inventario
    def registrar_producto(self, producto):
        self.productos.append(producto)

     # Función para registrar una venta en el sistema
    def registrar_venta(self, codigo, cantidad, fecha_venta):
        # Buscamos el producto con el código especificado en la lista de productos del inventario
        for producto in reversed(self.productos):
            if producto.codigo == codigo:
                 # Creamos una instancia de la clase Venta con los datos ingresados y el producto encontrado
                venta = Venta(producto, cantidad, fecha_venta)
                # Agregamos la venta a la lista de ventas del sistema
                self.ventas.append(venta)
                return venta
        return None

    # Función para generar un reporte de ventas por fecha
    def ventas_por_fecha(self, fecha):
        # Creamos una lista vacía para almacenar las ventas encontradas
        ventas = []
        for venta in self.ventas:
            if venta.fecha_venta == fecha:
                ventas.append(venta)
        return ventas
    # Función para generar un reporte de ventas por producto
    def ventas_por_producto(self, codigo):
        ventas = []
        for venta in self.ventas:
            if venta.producto.codigo == codigo:
                ventas.append(venta)
        return ventas
        
    # Función para generar un reporte de productos que exceden un precio determinado
    def productos_exceden_precio(self, precio):
        productos = []
        for producto in self.productos:
            if producto.precio_unitario > precio:
                productos.append(producto)
        return productos

def menu():
    inventario = Inventario()
    # Bucle infinito para mostrar el menú principal y permitir al usuario interactuar con el programa
    while True:
        print("1. Registrar producto")
        print("2. Registrar venta")
        print("3. Generar reporte de ventas por fecha")
        print("4. Generar reporte de ventas por producto")
        print("5. Generar reporte de productos que exceden un precio")
        print("6. Salir")
        # Se solicita al usuario que ingrese una opción del menú
        opcion = input("Elige una opción: ")
        # Se verifica qué opción eligió el usuario y se ejecuta el código correspondiente a esa opción
        if opcion == "1":
            codigo = input("Ingresa el código del producto: ")
            descripcion = input("Ingresa la descripción del producto: ")
            precio_unitario = float(input("Ingresa el precio unitario del producto: "))
            fecha_ingreso = input("Ingresa la fecha de ingreso del producto (dd/mm/aaaa): ")
            dia, mes, anio = map(int, fecha_ingreso.split("/"))#divide la fecha con / y almacena cada elemento en una variable
            fecha_ingreso = date(anio, mes, dia)#reordena la fecha
            producto = Producto(codigo, descripcion, precio_unitario, fecha_ingreso)
            inventario.registrar_producto(producto)
            print("Producto registrado con éxito")
        elif opcion == "2":
            codigo = input("Ingresa el código del producto: ")
            cantidad = int(input("Ingresa la cantidad vendida: "))
            fecha_venta = input("Ingresa la fecha de venta (dd/mm/aaaa): ")
            dia, mes, anio = map(int, fecha_venta.split("/"))
            fecha_venta = date(anio, mes, dia)
            inventario.registrar_venta(codigo, cantidad, fecha_venta)
            print("Venta registrada con éxito")
        elif opcion == "3":
            fecha = input("Ingresa la fecha (dd/mm/aaaa): ")
            dia, mes, anio = map(int, fecha.split("/"))
            fecha = date(anio, mes, dia)
            ventas = inventario.ventas_por_fecha(fecha)
            print(f"Ventas por fecha {fecha}:")
            for venta in ventas:#recorre la pila para mostrar los resultados
                print(f"Código: {venta.producto.codigo}, Descripción: {venta.producto.descripcion}, Cantidad: {venta.cantidad}, Precio total: {venta.precio_total}")
        elif opcion == "4":
            codigo = input("Ingresa el código del producto: ")
            ventas = inventario.ventas_por_producto(codigo)
            print(f"Ventas por producto {codigo}:")
            for venta in ventas:
                print(f"Código: {venta.producto.codigo}, Descripción: {venta.producto.descripcion}, Cantidad: {venta.cantidad}, Precio total: {venta.precio_total}")
        elif opcion == "5":
            precio = float(input("Ingresa el precio: "))
            productos = inventario.productos_exceden_precio(precio)
            print(f"Productos que exceden el precio {precio}:")
            for producto in productos:
                print(f"Código: {producto.codigo}, Descripción: {producto.descripcion}, Precio unitario: {producto.precio_unitario}")
        elif opcion == "6":
            break

if __name__ == "__main__":
    menu()