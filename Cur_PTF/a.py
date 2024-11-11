arr = [11, 21, 7, 14, 3, 6, 7]

def indice_mayor_a_menor_en_array(arr):
    # Ordenar el array en orden descendente y guardar los índices originales
    sorted_indices = sorted(range(len(arr)), key=lambda i: arr[i], reverse=True)
    
    # Crear un array para almacenar los índices ordenados
    result = [0] * len(arr)
    
    # Diccionario para rastrear los índices ya asignados
    value_to_rank = {}
    rank = 1
    
    for idx in sorted_indices:
        value = arr[idx]
        if value not in value_to_rank:
            value_to_rank[value] = rank
            rank += 1
        result[idx] = value_to_rank[value]
    
    return result

print(indice_mayor_a_menor_en_array(arr))