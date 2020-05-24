from itertools import combinations
n = int(input('Antal videor ? '))
all_vids = [(int(input(f'Video {i}, längd      ? ')), set(input(f'Video {i}, kategorier ? '))) for i in range(1, n+1)]
all_categs = set.union(*(v[1] for v in all_vids))
tider = [sum(v[0] for v in vids) for n_vids in range(1, n+1) for vids in combinations(all_vids, r=n_vids) if set.union(*(v[1] for v in vids)) == all_categs]
# tider = []
# for n_vids in range(1, n+1):
#     for vids in combinations(all_vids, r=n_vids):
#         if set.union(*(v[1] for v in vids)) == all_categs:
#             tider.append(sum(v[0] for v in vids))
print('Svar:', min(tider))