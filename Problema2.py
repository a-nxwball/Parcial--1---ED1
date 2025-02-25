def insertion_sort(arr):
    """
    Ordena un arreglo de números enteros utilizando el algoritmo de Ordenamiento por Inserción.
    Se utiliza la estructura de datos 'arreglo'.
    
    Args:
        arr (list): Arreglo de números enteros.
        
    Devuelve:
        sorted_arr: Arreglo ordenado.
    """
    n = len(arr)
    # Iterar desde el segundo elemento, considerando el primer elemento como subarreglo ordenado.
    for i in range(1, n):
        key = arr[i]  # Elemento a insertar.
        j = i - 1
        
        # Mover elementos del subarreglo ordenado que sean mayores que 'key' una posición a la derecha.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertar 'key' en la posición correcta.
        arr[j + 1] = key
    
    return arr

def main():
    # Arreglo original
    arr = [12, 11, 13, 5, 6]
    print("Arreglo original:", arr)
    
    # Ordenar el arreglo utilizando el algoritmo de Ordenamiento por Inserción
    sorted_arr = insertion_sort(arr)
    print("Arreglo ordenado:", sorted_arr)

# Ejemplo de uso:
if __name__ == "__main__":
    main()