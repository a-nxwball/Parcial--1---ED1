class Node:
    """
    Estructura de un nodo en una lista enlazada.
    
    Atributos:
        data (int): Valor almacenado en el nodo.
        next (Node): Referencia al siguiente nodo en la lista.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Implementación de una lista enlazada.
    
    Métodos:
        insert_at_beginning(data): Inserta un nodo al inicio de la lista.
        insert_at_end(data): Inserta un nodo al final de la lista.
        search(value): Busca un nodo por su valor y retorna si existe o no.
        delete(value): Elimina un nodo por su valor si existe.
        display(): Muestra los elementos de la lista enlazada.
    """
    def __init__(self):
        self.head = None  # La lista inicia vacía

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Nodo con valor {data} insertado al inicio.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Nodo con valor {data} insertado al final.")

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return f"Nodo con valor {value} encontrado en la lista."
            current = current.next
        return f"Nodo con valor {value} no encontrado en la lista."

    def delete(self, value):
        current = self.head
        previous = None
        
        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Nodo con valor {value} eliminado de la lista.")
                return
            previous = current
            current = current.next
        
        print(f"Nodo con valor {value} no encontrado en la lista.")

    def display(self):
        if not self.head:
            print("La lista está vacía.")
        else:
            current = self.head
            print("Lista enlazada:", end=" ")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

def main():
    linked_list = LinkedList()

    # Insertar nodos
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)

    # Mostrar la lista
    linked_list.display()

    # Buscar un nodo
    print(linked_list.search(20))  
    print(linked_list.search(40))  

    # Eliminar un nodo
    linked_list.delete(10)
    linked_list.display()

    linked_list.delete(40)  # Intento de eliminar un nodo inexistente

if __name__ == "__main__":
    main()