class Stack:
    """
    Implementación de una pila utilizando un arreglo dinámico (lista).
    
    Métodos:
        push(x): Agrega un elemento al tope de la pila.
        pop(): Elimina y devuelve el elemento en el tope de la pila.
        top(): Devuelve el elemento en el tope sin eliminarlo.
        is_empty(): Verifica si la pila está vacía.
        size(): Devuelve el tamaño actual de la pila.
    """
    def __init__(self):
        self.stack = []  # Lista dinámica para almacenar elementos

    def push(self, x):
        self.stack.append(x)
        print(f"Elemento {x} agregado a la pila.")

    def pop(self):
        if self.is_empty():
            print("Error: La pila está vacía, no se puede eliminar un elemento.")
            return None
        removed = self.stack.pop()
        print(f"Elemento {removed} eliminado de la pila.")
        return removed

    def top(self):
        if self.is_empty():
            print("Error: La pila está vacía, no hay elemento en el tope.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def main():
    pila = Stack()

    # Insertar elementos
    pila.push(10)
    pila.push(20)
    pila.push(30)

    # Obtener el elemento en el tope sin eliminarlo
    print(f"Elemento en el tope: {pila.top()}")

    # Eliminar elementos
    pila.pop()
    pila.pop()

    # Verificar el nuevo tope
    print(f"Nuevo elemento en el tope: {pila.top()}")

    # Verificar tamaño de la pila
    print(f"Tamaño actual de la pila: {pila.size()}")

    # Intentar eliminar el último elemento y otro en una pila vacía
    pila.pop()
    pila.pop()

if __name__ == "__main__":
    main()