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
    
print("Bienvenido")
print("A continuación se le presentará un menú para gestionar su inventario de productos.")
print("Por favor, elija una opción del menú a continuación:")

while True:
    opcion = input("Opciones: " \
    "\n----------------------" \
    "\na - Agregar Producto " 
    "\nb - Mostrar Inventario" \
    "\nc - Buscar Producto" \
    "\nd - Eliminar Producto" \
    "\ne - Salir " \
    "\n----------------------" \
    "\n Ingrese su elección: ")
    print("------------------")

    match opcion:
        case "a":
            print("Agregando Productos...")
            while True:
                producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
                if producto.lower() == 'salir':
                    break
                cantidad = input(f"Ingrese la cantidad de {producto}: ")
                inventario[producto.lower()] = inventario.get(producto.lower(), 0) + int(cantidad)
                print(f"Producto {producto} agregado con cantidad {cantidad}.")

        case "b":
            print("Mostrando Inventario...")
            if inventario:
                print("Inventario actual:")
                print("------------------")               
                for producto, cantidad in inventario.items():
                    print(f"{producto}: {cantidad}")
                
                waiting = input("Presione Enter para continuar...")
                continue  
            else:
                print("El inventario está vacío.")
                waiting = input("Presione Enter para continuar...")
                print("------------------")
                print("\n")
                continue

        case "c":
            print("Buscador Productos")
            print("------------------")
            if inventario == {}:
                print("El inventario está vacío.")
                print("------------------")
                print("\n")
                waiting = input("Presione Enter para continuar...")
                continue                    
            else:
                print("Buscando Productos...")
                print("------------------")
                while True:
                    producto = input("Ingrese el nombre del producto a buscar (o 'salir' para terminar): ")
                    if producto.lower() == 'salir':
                        break
                    if producto.lower() in inventario:
                        print(f"Producto {producto} encontrado con cantidad {inventario[producto.lower()]}.")
                        print("------------------")
                    else:
                        print(f"Producto {producto.lower()} no encontrado en el inventario.")
                        print("------------------")
                    print("\n")
            print("------------------")
            print("\n")

        case "d":
            print("Buscando Productos A Eliminar...")
            print("------------------")
            if inventario == {}:
                print("El inventario está vacío.")                
                waiting = input("Presione Enter para continuar...")
                print("------------------")
                print("\n")
                continue
            else:
                while True:
                    producto = input("Ingrese el nombre del producto a eliminar (o 'salir' para terminar): ")   
                    if producto.lower() == 'salir':
                        break
                    if producto.lower() in inventario:
                        del inventario[producto.lower()]
                        print(f"Producto {producto} eliminado del inventario.")
                        print("------------------")
                    else:
                        print(f"Producto {producto} no encontrado en el inventario.")
                        print("------------------")

        case "e":
            salir = input("¿Está seguro que desea salir? (S/N): ")
            if salir.lower() == 's':
                print("Saliendo del programa...")
                print("Gracias por visitarnos. Esperamos que vuelva pronto.")
                print("------------------")
                break
            else:
                print("Regresando al menú principal...")
                
            exit() # Termina el programa

        case _:
            print("Opción no válida, intente nuevamente.")
        
