items = []
n = 0
i = 0
j = None

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    global items, n, i, j

    # 1) Si ya procesamos todos: terminar
    if i >= n:
        return {"done": True}

    # 2) Si j es None, iniciamos el desplazamiento
    if j is None:
        j = i
        return {"a": None, "b": None, "swap": False, "done": False}


    # 3) Si todavía podemos desplazar (comparar j-1 con j)
    if j > 0 and items[j-1] > items[j]:
        # Hacemos un swap
        items[j-1], items[j] = items[j], items[j-1]
        a, b = j-1, j   # índices de los que se intercambiaron
        j -= 1         # seguimos desplazando hacia la izquierda
        return {"a": a, "b": b, "swap": True, "done": False}

    # 4) No hay más desplazamientos → avanzar i
    i += 1
    j = None
    return {"a": None, "b": None, "swap": False, "done": False}

    # TODO:
    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
