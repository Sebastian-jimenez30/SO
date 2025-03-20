def first_fit(mem_avail, req, index):

    if not mem_avail or req <= 0:
        return None

    for i, (base, limit) in enumerate(mem_avail):
        if limit >= req:
            new_base = base
            new_limit = req
            remaining_limit = limit - req

            if remaining_limit > 0:
                mem_avail[i] = (base + req, remaining_limit)
            else:
                del mem_avail[i]

            return mem_avail, new_base, new_limit, i

    return None
