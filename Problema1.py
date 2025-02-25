def max_subarray_sum(arr):
    """
    Encuentra la suma del subarreglo contiguo de mayor suma 
    Se utilizan la estructura de datos 'arreglo' y el algoritmo de Kadane.
    
    Args:
        arr (list): Arreglo de números enteros.
    
    Devuelve:
        int: La suma máxima encontrada.
    """
    # Verificar que el arreglo no esté vacío.
    if not arr:
        return 0  # Se retorna 0 si el arreglo está vacío.
    
    # Inicializamos current_sum y max_sum con el primer elemento del arreglo.
    current_sum = max_sum = arr[0]
    
    # Recorremos el arreglo a partir del segundo elemento.
    for i in range(1, len(arr)):
        # Se decide si se suma el elemento actual o se inicia un nuevo subarreglo.
        current_sum = max(arr[i], current_sum + arr[i])
        # Se actualiza max_sum si current_sum es mayor.
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def main():
    # Arreglo original
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Arreglo original:", arr)
    
    # Calcular la suma del subarreglo contiguo de mayor suma
    max_sum = max_subarray_sum(arr)
    print("Suma del subarreglo contiguo de mayor suma:", max_sum)

# Ejemplo de uso:
if __name__ == "__main__":
    main()
