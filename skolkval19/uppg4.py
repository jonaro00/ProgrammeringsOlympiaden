from itertools import product
start = input('Start ? ')
mål   = input('Mål   ? ')
multationer = ('A', 'B', 'C', 'AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC', 'AAA', 'AAB', 'AAC', 'ABA', 'ABB', 'ABC', 'ACA', 'ACB', 'ACC', 'BAA', 'BAB', 'BAC', 'BBA', 'BBB', 'BBC', 'BCA', 'BCB', 'BCC', 'CAA', 'CAB', 'CAC', 'CBA', 'CBB', 'CBC', 'CCA', 'CCB', 'CCC')
lösningar = set()
for c1, c2, c3 in product('ABC', repeat=3):
    for m1, m2, m3 in product(multationer, repeat=3):
        z = start
        swaps = [(c1, m1), (c2, m2), (c3, m3)]
        for swap in swaps[:]:
            if swap[0] == swap[1] or swap[0] not in z:
                swaps.remove(swap)
                continue
            z = z.replace(swap[0], swap[1])
        if z == mål:
            lösningar.add(tuple(swaps))
lösningar = tuple(lösningar)
längder = tuple(map(len, lösningar))
bäst = lösningar[längder.index(min(längder))]
for i, s in enumerate(bäst, start=1):
    print(f'Multation {i}:  {s[0]} -> {s[1]}')