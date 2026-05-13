print("==== CONTROL DE INVENTARIO DE TIENDA ====")
print("")

numProductos = int(input("Digita la cantidad de productos a ingresar: "))

stock = [numProductos] 
codigo = [numProductos] 
precio = [numProductos] 
categoria = [numProductos] 
nombre = [numProductos]

while True:
    print("---MENU DE INVENTARIO---")
    print("1. Agregar nuevo producto")
    print("2. Buscar producto")
    print("3. Actualizar stock")
    print("4. Vender producto")
    print("5. Salir")
    opcion = int(input("Ingresa una opcion: "))

    match (opcion):
        case 1:
            for i in range(1):
                nombre = str(input("Ingresa el nombre del producto: "))
    
