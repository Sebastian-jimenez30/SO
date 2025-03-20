def best_fit(mem_avail, req, index):

    if not mem_avail or req <= 0:
        return None

    best_index = -1
    min_size = float('inf')

    for i, (base, limit) in enumerate(mem_avail):
        if limit >= req and limit < min_size:
            min_size = limit
            best_index = i

    if best_index == -1:
        return None

    base, limit = mem_avail[best_index]
    new_base = base
    new_limit = req
    remaining_limit = limit - req

    if remaining_limit > 0:
        mem_avail[best_index] = (base + req, remaining_limit)
    else:
        del mem_avail[best_index]

    return mem_avail, new_base, new_limit, best_index
