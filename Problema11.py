class Queue:
    """
    Implementación de una cola utilizando un arreglo dinámico (lista).
    
    Métodos:
        enqueue(x): Agrega un elemento al final de la cola.
        dequeue(): Elimina y devuelve el elemento al frente de la cola.
        front(): Devuelve el elemento al frente sin eliminarlo.
        is_empty(): Verifica si la cola está vacía.
        size(): Devuelve el tamaño actual de la cola.
    """
    def __init__(self):
        self.queue = []  # Lista dinámica para almacenar elementos

    def enqueue(self, x):
        self.queue.append(x)
        print(f"Elemento {x} agregado a la cola.")

    def dequeue(self):
        if self.is_empty():
            print("Error: La cola está vacía, no se puede eliminar un elemento.")
            return None
        removed = self.queue.pop(0)  # Eliminar el primer elemento (frontal)
        print(f"Elemento {removed} eliminado de la cola.")
        return removed

    def front(self):
        if self.is_empty():
            print("Error: La cola está vacía, no hay elemento en el frente.")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def main():
    cola = Queue()

    # Insertar elementos
    cola.enqueue(10)
    cola.enqueue(20)
    cola.enqueue(30)

    # Obtener el elemento al frente sin eliminarlo
    print(f"Elemento al frente: {cola.front()}")

    # Eliminar elementos
    cola.dequeue()
    cola.dequeue()

    # Verificar el nuevo frente
    print(f"Nuevo elemento al frente: {cola.front()}")

    # Verificar tamaño de la cola
    print(f"Tamaño actual de la cola: {cola.size()}")

    # Intentar eliminar el último elemento y otro en una cola vacía
    cola.dequeue()
    cola.dequeue()

if __name__ == "__main__":
    main()