# Escribe un programa que tenga un menú para gestionar un inventario de productos:
'''
a) Agregar Producto
b) Mostrar Inventario
c) Buscar Producto
d) Eliminar Producto
e) Salir
'''
inventario = {}

# def agregar_producto():
def agregar_producto():
    print("Agregando Productos...")
    print("------------------")
    producto = input("Ingrese el primer producto (o 'salir' para terminar): ")
    cantidad = input(f"Ingrese la cantidad de {producto}: ")
    while True:
        producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if producto.lower() == 'salir':
            break #romper el bucle
        print(producto)
        cantidad = input(f"Ingrese la cantidad de {producto}: ")
        inventario[producto.lower()] = inventario.get(producto.lower(), 0) + int(cantidad)
        print(f"Producto {producto} agregado con cantidad {cantidad}.")

# función mostrar inventario.
def mostrar_inventario():
    print("Mostrando Inventario...")
    if inventario:
        print("Inventario actual:")
        print("------------------")               
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad}")
            
        waiting = input("Presione Enter para continuar...")
        return True  
    else:
        print("El inventario está vacío.")
        waiting = input("Presione Enter para continuar...")
        print("------------------")
        print("\n")
        return False  

# mostrar_inventario()

agregar_producto()
mostrar_inventario()
