from datetime import date

class Producto:
    # Constructor de la clase Producto
    def __init__(self, codigo, descripcion, precio_unitario, fecha_ingreso):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.fecha_ingreso = fecha_ingreso

class Inventario:
    # Constructor de la clase Inventario
    def __init__(self):
        self.productos = []

    # Función para registrar un producto en el inventario
    def registrar_producto(self, producto):
        self.productos.append(producto)

    # Función para registrar una orden de salida de un producto del inventario
    def orden_salida(self, codigo):
        for producto in reversed(self.productos):
            if producto.codigo == codigo:
                self.productos.remove(producto)
                return producto
        return None

    # Función para generar un reporte de ventas por fecha
    def ventas_por_fecha(self, fecha):
        ventas = []
        for producto in self.productos:
            if producto.fecha_ingreso == fecha:
                ventas.append(producto)
        return ventas

    # Función para generar un reporte de ventas por producto
    def ventas_por_producto(self, codigo):
        ventas = []
        for producto in self.productos:
            if producto.codigo == codigo:
                ventas.append(producto)
        return ventas

    # Función para generar un reporte de productos que exceden un precio determinado
    def productos_exceden_precio(self, precio):
        productos = []
        for producto in self.productos:
            if producto.precio_unitario > precio:
                productos.append(producto)
        return productos

# Función para mostrar un menú al usuario y permitirle interactuar con el sistema
def menu():
    inventario = Inventario()
    while True:
        print("1. Registrar producto")
        print("2. Registrar orden de salida")
        print("3. Generar reporte de ventas por fecha")
        print("4. Generar reporte de ventas por producto")
        print("5. Generar reporte de productos que exceden un precio")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            codigo = input("Ingresa el código del producto: ")
            descripcion = input("Ingresa la descripción del producto: ")
            precio_unitario = float(input("Ingresa el precio unitario del producto: "))
            fecha_ingreso = input("Ingresa la fecha de ingreso del producto (dd/mm/aaaa): ")
            dia, mes, anio = map(int, fecha_ingreso.split("/"))
            fecha_ingreso = date(anio, mes, dia)
            producto = Producto(codigo, descripcion, precio_unitario, fecha_ingreso)
            inventario.registrar_producto(producto)
            print("Producto registrado con éxito")
        elif opcion == "2":
            codigo = input("Ingresa el código del producto: ")
            inventario.orden_salida(codigo)
            print("Orden de salida registrada con éxito")
        elif opcion == "3":
            fecha = input("Ingresa la fecha (dd/mm/aaaa): ")
            dia, mes, anio = map(int, fecha.split("/"))
            fecha = date(anio, mes, dia)
            ventas = inventario.ventas_por_fecha(fecha)
            print(f"Ventas por fecha {fecha}:")
            for venta in ventas:
                print(f"Código: {venta.codigo}, Descripción: {venta.descripcion}, Precio unitario: {venta.precio_unitario}")
        elif opcion == "4":
            codigo = input("Ingresa el código del producto: ")
            ventas = inventario.ventas_por_producto(codigo)
            print(f"Ventas por producto {codigo}:")
            for venta in ventas:
                print(f"Código: {venta.codigo}, Descripción: {venta.descripcion}, Precio unitario: {venta.precio_unitario}")
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