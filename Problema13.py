class Stack:
    """
    Implementación de una pila utilizando un arreglo dinámico (lista).
    
    Métodos:
        push(x): Agrega un elemento al tope de la pila.
        pop(): Elimina y devuelve el elemento en el tope de la pila.
        top(): Devuelve el elemento en el tope sin eliminarlo.
        is_empty(): Verifica si la pila está vacía.
    """
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

class QueueWithTwoStacks:
    """
    Implementación de una cola utilizando dos pilas (simulación de cola FIFO).
    
    Métodos:
        enqueue(x): Agrega un elemento al final de la cola.
        dequeue(): Elimina y devuelve el primer elemento de la cola.
        front(): Devuelve el primer elemento de la cola sin eliminarlo.
        is_empty(): Verifica si la cola está vacía.
    """
    def __init__(self):
        self.stack1 = Stack()  # Pila para ingresar elementos
        self.stack2 = Stack()  # Pila para remover elementos

    def enqueue(self, x):
        self.stack1.push(x)
        print(f"Elemento {x} agregado a la cola.")

    def dequeue(self):
        if self.is_empty():
            print("Error: La cola está vacía, no se puede eliminar un elemento.")
            return None
        if self.stack2.is_empty():
            # Transferir los elementos de stack1 a stack2
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        removed = self.stack2.pop()
        print(f"Elemento {removed} eliminado de la cola.")
        return removed

    def front(self):
        if self.is_empty():
            print("Error: La cola está vacía, no hay elemento en el frente.")
            return None
        if self.stack2.is_empty():
            # Transferir los elementos de stack1 a stack2 si stack2 está vacía
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.top()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

def main():
    queue = QueueWithTwoStacks()

    # Insertar elementos en la cola
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Ver el primer elemento en la cola
    print(f"Elemento en el frente de la cola: {queue.front()}")

    # Eliminar elementos de la cola
    queue.dequeue()
    queue.dequeue()

    # Verificar el nuevo frente de la cola
    print(f"Nuevo elemento en el frente de la cola: {queue.front()}")

    # Verificar si la cola está vacía
    print(f"¿Está vacía la cola? {'Sí' if queue.is_empty() else 'No'}")

    # Eliminar el último elemento
    queue.dequeue()

    # Verificar si la cola está vacía
    print(f"¿Está vacía la cola? {'Sí' if queue.is_empty() else 'No'}")

if __name__ == "__main__":
    main()