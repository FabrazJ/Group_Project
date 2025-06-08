# main.py

from product import Product
from Cart import Cart

def mostrar_menu():
    print("\n🛒 MINI MARKET")
    print("1. Agregar producto al carrito")
    print("2. Ver total")
    print("3. Vaciar carrito")
    print("4. Salir")

def main():
    carrito = Cart()

    # Catálogo fijo
    catalogo = {
        "1": Product("Manzana", 0.5),
        "2": Product("Banana", 1.0),
        "3": Product("Agua", 0.75)
    }

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nProductos disponibles:")
            for codigo, prod in catalogo.items():
                print(f"{codigo}. {prod.name} - ${prod.price}")
            codigo = input("Selecciona el número del producto: ")

            if codigo in catalogo:
                cantidad = int(input("¿Cantidad? "))
                carrito.add(catalogo[codigo], cantidad)
                print(f"✅ Agregado: {cantidad} x {catalogo[codigo].name}")
            else:
                print("❌ Producto no válido.")

        elif opcion == "2":
            print(f"\n🧾 Total a pagar: ${carrito.total():.2f}")

        elif opcion == "3":
            carrito.clear()
            print("🧹 Carrito vaciado.")

        elif opcion == "4":
            print("👋 ¡Gracias por visitar el Mini Market!")
            break

        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
