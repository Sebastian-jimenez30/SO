def worst_fit(mem_avail, req, index):

    if not mem_avail or req <= 0:
        return None

    max_index = -1
    max_size = -1

    for i, (base, limit) in enumerate(mem_avail):
        if limit >= req and limit > max_size:
            max_size = limit
            max_index = i

    if max_index == -1:
        return None

    base, limit = mem_avail[max_index]
    new_base = base
    new_limit = req
    remaining_limit = limit - req

    if remaining_limit > 0:
        mem_avail[max_index] = (base + req, remaining_limit)
    else:
        del mem_avail[max_index]

    return mem_avail, new_base, new_limit, max_index
