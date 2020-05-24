from itertools import combinations
rad = list(input('Rad ? '))
n = len(rad)
max_avs = int(input('Maxavstånd ? '))
possible_swaps = [{i, i + swap_len} for swap_len in range(1, max_avs + 1) for i in range(n - swap_len)]
max_par = sum(map(lambda a, b: a == b, rad[:-1], rad[1:])) # number of pairs in the beginning
for n_swaps in range(1, n//2 + 1):
    for swaps in combinations(possible_swaps, r=n_swaps):
        if len(set.union(*swaps)) == sum(len(s) for s in swaps): # no duplicate positions in swaps
            result = rad.copy()
            for i, j in swaps:
                result[i], result[j] = result[j], result[i]
            n_pairs = sum(map(lambda a, b: a == b, result[:-1], result[1:]))
            max_par = max(n_pairs, max_par)
print('Max antal par:', max_par)