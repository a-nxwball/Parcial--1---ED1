class Queue:
    """
    Implementación de una cola utilizando un arreglo dinámico (lista).
    
    Métodos:
        enqueue(x): Agrega un cliente al final de la cola.
        dequeue(): Elimina y devuelve el cliente al frente de la cola.
        front(): Devuelve el cliente al frente sin eliminarlo.
        is_empty(): Verifica si la cola está vacía.
    """
    def __init__(self):
        self.queue = []  # Lista dinámica para almacenar clientes

    def enqueue(self, x):
        self.queue.append(x)
        print(f"Cliente {x} agregado a la fila.")

    def dequeue(self):
        if self.is_empty():
            print("Error: La fila está vacía, no hay clientes para atender.")
            return None
        customer = self.queue.pop(0)  # Eliminar al cliente al frente
        print(f"Cliente {customer} atendido y salido de la fila.")
        return customer

    def front(self):
        if self.is_empty():
            print("Error: La fila está vacía, no hay clientes al frente.")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def main():
    # Simulación de clientes que llegan a la tienda
    store_queue = Queue()

    # Clientes llegan a la tienda
    store_queue.enqueue("Cliente A")
    store_queue.enqueue("Cliente B")
    store_queue.enqueue("Cliente C")

    # Ver el cliente al frente
    print(f"Cliente al frente de la fila: {store_queue.front()}")

    # Atender clientes
    store_queue.dequeue()  # Atendemos al primero
    store_queue.dequeue()  # Atendemos al siguiente

    # Ver el nuevo cliente al frente
    print(f"Nuevo cliente al frente de la fila: {store_queue.front()}")

    # Verificar el tamaño de la fila
    print(f"Tamaño actual de la fila: {store_queue.size()}")

    # Intentar atender más clientes en una fila vacía
    store_queue.dequeue()
    store_queue.dequeue()

if __name__ == "__main__":
    main()
