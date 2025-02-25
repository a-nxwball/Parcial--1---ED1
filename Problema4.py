def is_subset(set1, set2):
    """
    Función para determinar si uno de los conjuntos es subconjunto del otro.
    
    Argumentos:
        set1 (set): Primer conjunto.
        set2 (set): Segundo conjunto.
        
    Devuelve:
        str: Mensaje indicando cuál conjunto es subconjunto o si no lo son.
    """
    if set1.issubset(set2):
        return f"El conjunto {set1} es un subconjunto de {set2}."
    elif set2.issubset(set1):
        return f"El conjunto {set2} es un subconjunto de {set1}."
    else:
        return "Ninguno de los conjuntos es subconjunto del otro."

def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3}
    print(is_subset(set1, set2))

if __name__ == "__main__":
    main()