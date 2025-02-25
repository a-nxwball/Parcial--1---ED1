class Node:
    """
    Nodo para la lista enlazada. Cada nodo tiene un valor y una referencia al siguiente nodo.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Implementación de una lista enlazada.
    
    Métodos:
        append(value): Agrega un nuevo nodo al final de la lista.
        detect_cycle(): Detecta si hay un ciclo en la lista utilizando el algoritmo de Floyd.
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def detect_cycle(self):
        """
        Algoritmo de Floyd (tortuga y liebre) para detectar ciclos en una lista enlazada.
        Utiliza dos punteros, uno avanza de dos en dos (liebre) y el otro de uno en uno (tortuga).
        Si se encuentran, hay un ciclo. Si la liebre llega al final (None), no hay ciclo.
        """
        slow = self.head  # Tortuga: avanza una posición a la vez
        fast = self.head  # Liebre: avanza dos posiciones a la vez

        while fast and fast.next:
            slow = slow.next         # Tortuga avanza 1 paso
            fast = fast.next.next    # Liebre avanza 2 pasos

            if slow == fast:         # Si tortuga y liebre se encuentran, hay un ciclo
                return True

        return False  # Si la liebre llega al final sin encontrar a la tortuga, no hay ciclo

def main():
    # Crear la lista enlazada
    linked_list = LinkedList()

    # Agregar elementos a la lista
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    # Crear un ciclo en la lista / Comentar para probar sin ciclo
    # linked_list.head.next.next.next.next.next = linked_list.head.next.next

    # Detectar si la lista tiene ciclo
    if linked_list.detect_cycle():
        print("La lista tiene un ciclo.")
    else:
        print("La lista no tiene un ciclo.")

if __name__ == "__main__":
    main()
