def custom_combs(iterable, r):
    n = len(iterable)
    indices = list(range(r))
    yield tuple(iterable[i] for i in indices)
    while 1:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        
        yield tuple(iterable[i] for i in indices)

def custom_product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)



from itertools import combinations, product
def n_pairs(s):
    p = 0
    for a, b in zip(s[:-1], s[1:]):
        if a == b:
            p += 1
    return p
rad = list(input('Rad ? '))
n = len(rad)
max_avs = int(input('Maxavstånd ? '))

possible_swaps = [{i, i + swap_len} for swap_len in range(1, max_avs + 1) for i in range(n - swap_len)]
max_par = 0
# for n_swaps in range(1, n//2 + 1):
#     for swaps in combinations(possible_swaps, n_swaps):
#         if len(set.union(*swaps)) == n_swaps * 2:
#             result = rad[:]
#             for i, j in swaps:
#                 result[i], result[j] = result[j], result[i]
#             max_par = max(max_par, n_pairs(result))
flag = ()
optimal_rad = rad[:]
for n_swaps in range(1, n//2 + 1):
    for swaps in product(possible_swaps, repeat=n_swaps):
        if n_swaps is not 1:
            if flag:
                if swaps[flag[0]] is flag[1]:
                    continue
                flag = ()
            holder = swaps[0]
            for i, swap in enumerate(swaps[1:], start=2):
                holder = set.union(holder, swap)
                if len(holder) != i * 2:
                    flag = (i-1, swap)
                    break
            if flag:
                continue
        result = rad[:]
        for i, j in swaps:
            result[i], result[j] = result[j], result[i]
        if n_pairs(result) > max_par:
            max_par = n_pairs(result)
            optimal_rad = ''.join(result)
print(f'Max antal par: {max_par} ({optimal_rad})')