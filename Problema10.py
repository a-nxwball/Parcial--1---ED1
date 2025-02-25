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
        self.stack = []  # Lista dinámica para almacenar elementos

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

def is_balanced(expression):
    """
    Verifica si una expresión matemática con paréntesis, corchetes y llaves está balanceada.
    
    Args:
        expression (str): La expresión a verificar.
    
    Returns:
        bool: True si la expresión está balanceada, False en caso contrario.
    """
    stack = Stack()
    matching_brackets = {')': '(', '}': '{', ']': '['}  # Mapear cierre a apertura

    for char in expression:
        if char in '({[':  # Si es un símbolo de apertura
            stack.push(char)
        elif char in ')}]':  # Si es un símbolo de cierre
            top = stack.pop()
            if top != matching_brackets[char]:  # Verificar si es el que corresponde
                return False

    return stack.is_empty()  # Si la pila está vacía, los paréntesis están balanceados

def main():
    expressions = [
        "(a + b) * [c - d] {e + f}",
        "(a + b) * [c - d} {e + f}",
        "{[a + b] * (c + d)}",
        "((a + b)"
    ]

    for expr in expressions:
        if is_balanced(expr):
            print(f"La expresión '{expr}' está balanceada.")
        else:
            print(f"La expresión '{expr}' no está balanceada.")

if __name__ == "__main__":
    main()