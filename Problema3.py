def union_conjuntos(conjunto_a, conjunto_b):
    """
    Función para obtener la unión de dos conjuntos.
    
    Args:
        conjunto_a (set): Primer conjunto.
        conjunto_b (set): Segundo conjunto.
    
    Devuelve:
        set: Unión de los dos conjuntos.
    """
    # Utilizamos el operador '|' para la unión
    return conjunto_a | conjunto_b

def interseccion_conjuntos(conjunto_a, conjunto_b):
    """
    Función para obtener la intersección de dos conjuntos.
    
    Args:
        conjunto_a (set): Primer conjunto.
        conjunto_b (set): Segundo conjunto.
    
    Devuelve:
        set: Intersección de los dos conjuntos.
    """
    # Utilizamos el operador '&' para la intersección
    return conjunto_a & conjunto_b

def diferencia_simetrica_conjuntos(conjunto_a, conjunto_b):
    """
    Función para obtener la diferencia simétrica de dos conjuntos.
    La diferencia simétrica contiene los elementos que están en 
    uno de los conjuntos, pero no en ambos.
    
    Args:
        conjunto_a (set): Primer conjunto.
        conjunto_b (set): Segundo conjunto.
    
    Devuelve:
        set: Diferencia simétrica de los dos conjuntos.
    """
    # Utilizamos el operador '^' para la diferencia simétrica
    return conjunto_a ^ conjunto_b

def main():
    # Definir dos conjuntos
    conjunto_a = {1, 2, 3, 4, 5}
    conjunto_b = {4, 5, 6, 7, 8}
    
    # Unión de los conjuntos
    union = union_conjuntos(conjunto_a, conjunto_b)
    print("Unión de los conjuntos:", union)
    
    # Intersección de los conjuntos
    interseccion = interseccion_conjuntos(conjunto_a, conjunto_b)
    print("Intersección de los conjuntos:", interseccion)
    
    # Diferencia simétrica de los conjuntos
    diferencia_simetrica = diferencia_simetrica_conjuntos(conjunto_a, conjunto_b)
    print("Diferencia simétrica de los conjuntos:", diferencia_simetrica)

# Ejemplo de uso:
if __name__ == "__main__":
    main()