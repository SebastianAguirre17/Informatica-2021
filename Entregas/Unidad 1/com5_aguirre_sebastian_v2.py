def showInfo(dinero, sombreros, precio):
    print(f"\nStock de Sombreros: {sombreros}")
    print(f"Dinero en caja: ${dinero}")
    print(f"Precio por unidad: ${precio}\n")

def mostrarVenta(cant_venta, precio, stock, dinero):
    print(f"Se vendieron {cant_venta} sobreros a un precio de ${precio}")
    print(f"Total de la venta: ${cant_venta * precio}")
    print(f"Dinero en caja: ${dinero}")
    print(f"Stock de Sombreros: {stock}\n")

def main():
    dinero = 1000

    sombreros = int(input("Ingrese la cantidad inicial de sombreros: "))
    precio = int(input("Ingrese el precio de cada sombrero: $"))
    showInfo(dinero, sombreros, precio)

    print("Vendo 1 tercio del stock.\n")
    cant_venta = sombreros // 3
    dinero += cant_venta * precio
    sombreros -= cant_venta
    mostrarVenta(cant_venta, precio, sombreros, dinero)

    print("Vendo la mitad del stock.\n")
    cant_venta = sombreros // 2
    dinero += cant_venta * precio
    sombreros -= cant_venta
    mostrarVenta(cant_venta, precio,sombreros, dinero)

# Ejecuto main    
main()

