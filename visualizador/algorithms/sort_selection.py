# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0         # índice actual donde pondremos el mínimo
j = 0         # cursor que recorre para encontrar el mínimo
min_index = 0 # posición del mínimo encontrado

def init(vals):
    global items, n, i, j, min_index
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_index = i

def step():
    global items, n, i, j, min_index

    # Caso terminado
    if i >= n - 1:
        return {"done": True}

    # Fase de búsqueda del mínimo
    if j < n:
        a = min_index
        b = j
        swap = False

        # Si encontramos un valor menor, actualizamos el mínimo
        if items[j] < items[min_index]:
            min_index = j

        # Avanzamos j
        j += 1

        return {"a": a, "b": b, "swap": swap, "done": False}

    # Cuando j ya recorrió toda la lista → hacemos el swap final
    else:
        a = i
        b = min_index
        swap = False

        # Hacemos swap solo si corresponde
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
            swap = True

        # Preparamos para la siguiente pasada
        i += 1
        min_index = i
        j = i + 1

        return {"a": a, "b": b, "swap": swap, "done": False}

    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
   
