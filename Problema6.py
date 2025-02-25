class Product:
    """
    Estructura para representar un producto en el inventario.
    
    Atributos:
        product_id (int): ID del producto.
        name (str): Nombre del producto.
        quantity (int): Cantidad disponible en el inventario.
        price (float): Precio del producto.
    """
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    """
    Estructura para manejar el inventario de productos utilizando un arreglo.
    
    Métodos:
        add_product(product): Agrega un nuevo producto al inventario.
        update_product(product_id, quantity, price): Modifica la cantidad y precio de un producto.
        remove_product(product_id): Elimina un producto del inventario.
        show_inventory(): Muestra todos los productos en el inventario.
    """
    def __init__(self):
        self.products = []  # Arreglo para almacenar los productos

    def add_product(self, product):
        self.products.append(product)
        print(f"Producto '{product.name}' agregado correctamente.")

    def update_product(self, product_id, quantity, price):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = quantity
                product.price = price
                print(f"Producto '{product.name}' actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def remove_product(self, product_id):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                del self.products[i]
                print(f"Producto '{product.name}' eliminado correctamente.")
                return
        print("Producto no encontrado.")

    def show_inventory(self):
        if not self.products:
            print("El inventario está vacío.")
        else:
            print("Inventario de productos:")
            for product in self.products:
                print(f"ID: {product.product_id}, Nombre: {product.name}, Cantidad: {product.quantity}, Precio: ${product.price:.2f}")

def main():
    inventory = Inventory()

    # Agregar productos al inventario
    inventory.add_product(Product(1, "Laptop", 10, 1200.50))
    inventory.add_product(Product(2, "Mouse", 50, 25.99))
    inventory.add_product(Product(3, "Teclado", 30, 45.75))

    # Mostrar el inventario
    inventory.show_inventory()

    # Modificar un producto
    inventory.update_product(2, 45, 27.99)

    # Eliminar un producto
    inventory.remove_product(3)

    # Mostrar el inventario después de modificaciones
    inventory.show_inventory()

if __name__ == "__main__":
    main()