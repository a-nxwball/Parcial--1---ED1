class Node:
    """
    Estructura de un nodo en una lista doblemente enlazada.
    
    Atributos:
        data (int): Valor almacenado en el nodo.
        prev (Node): Referencia al nodo anterior.
        next (Node): Referencia al siguiente nodo.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """
    Implementación de una lista doblemente enlazada.
    
    Métodos:
        insert_at_end(data): Inserta un nodo al final de la lista.
        display(): Muestra los elementos de la lista en orden normal.
        reverse(): Invierte la lista doblemente enlazada.
        display_reverse(): Muestra la lista en orden inverso.
    """
    def __init__(self):
        self.head = None  # La lista inicia vacía

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        print(f"Nodo con valor {data} insertado al final.")

    def display(self):
        if not self.head:
            print("La lista está vacía.")
        else:
            current = self.head
            print("Lista en orden normal:", end=" ")
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

    def reverse(self):
        if not self.head:
            return
        
        current = self.head
        prev_node = None

        # Intercambiar prev y next para cada nodo
        while current:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node
            current = current.prev  # Moverse al siguiente nodo en la nueva dirección

        # Actualizar la cabeza de la lista
        if prev_node:
            self.head = prev_node.prev

        print("Lista invertida correctamente.")

    def display_reverse(self):
        if not self.head:
            print("La lista está vacía.")
            return
        
        # Ir al último nodo
        current = self.head
        while current.next:
            current = current.next

        # Imprimir en orden inverso
        print("Lista en orden inverso:", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

def main():
    dll = DoublyLinkedList()

    # Insertar nodos
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)

    # Mostrar lista original
    dll.display()

    # Invertir la lista
    dll.reverse()

    # Mostrar lista invertida
    dll.display()

    # Mostrar lista en orden inverso desde el final
    dll.display_reverse()

if __name__ == "__main__":
    main()