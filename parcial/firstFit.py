def worst_fit(memory, req):

    
    # Encuentra el bloque más grande que pueda acomodar la solicitud
    max_size = -1
    index = -1
    for i, (base, limit) in enumerate(memory):
        size = limit - base
        if size >= req and size > max_size:
            max_size = size
            index = i

    # Si no se encontró un bloque adecuado
    if index == -1:
        return None  

    # Si se encontró un bloque adecuado, realiza la asignación
    base, limit = memory[index]
    
    # Calculamos el nuevo inicio y fin del bloque
    new_base = base
    new_limit = base + req
    new_start = base + req

    # Actualiza la memoria
    if new_limit < limit:
        memory[index] = (new_limit, limit)
    else:
        memory.pop(index)
    
    return memory, new_base, new_limit, new_start


memory = [(0, 100), (200, 300), (400, 600)]
req = 50
new_memory, new_base, new_limit, new_start = worst_fit(memory, req)

print("Nueva memoria:", new_memory)
print("Nueva base:", new_base)
print("Nuevo límite:", new_limit)
print("Nuevo inicio:", new_start)
