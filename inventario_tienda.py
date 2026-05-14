print("==== CONTROL DE INVENTARIO DE TIENDA ====")
print("")

stock = [] 
codigo = [] 
precio = [] 
categoria = [] 
nombre = []

def agregarProducto():
    numProductos = int(input("Digita la cantidad de productos a ingresar: "))

    for i in range(numProductos):
        print(f"--- Registro del Producto #{i+1} ---")

        nom = input("Escribe el nombre del producto: ")
        nombre.append(nom)

        while True:
            entrada = input("Escribe el codigo del producto (solo numeros): ")

            if entrada.isdigit():
                codigo.append(int(entrada))
                break
            else:
                print("Error, no puedes ingresar letras, vuelve a intentarlo.")

        cat = input("Ingresa la categoria del producto: ")
        categoria.append(cat)

        while True:
            prc = input("Ingresa el precio del producto: ")

            if prc.isdigit():
                precio.append(int(prc))
                break
            else:
                print("Error, no puedes ingresar letras, vuelve a intentarlo.")
        
        while True:
            stk = input("Ingresa el stock del producto: ")

            if stk.isdigit():
                stock.append(int(stk))
                break
            else:
                print("Error, no puedes ingresar letras, vuelve a intentarlo.")

def buscarProducto():
    if not codigo:
        print("El inventario esta vacio")
        print("")
        return

    cod = int(input("Ingresa el codigo del producto: "))

    if cod in codigo:
        indice = codigo.index(cod)

        print("\n---Producto encontrado---")
        print("Nombre:", nombre[indice])
        print("Categoria:", categoria[indice])
        print("Precio:", precio[indice],"$")
        print("Codigo:", codigo[indice])
        print("Stock:", stock[indice])
        print("")
    else:
        print("Codigo no encontrado")
        print("")





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
            agregarProducto()
        case 2:
            buscarProducto()

        case 5:
            print("Saliendo del sistema...")
            break

        case _:
            print("Opcion no valida, vuelve a intentarlo")
            print("")
