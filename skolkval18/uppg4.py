def swap(brickor, i, d):
    temp = inverted([brickor.pop(i) for _ in range(2)])
    return brickor + temp if d else temp + brickor
def unswap(brickor, i, d):
    for b in reversed(inverted([brickor.pop(p if d else 0) for p in range(-2, 0)])):
        brickor.insert(i, b)
    return brickor
def inverted(r):
    return ['S' if b == 'V' else 'V' for b in r]
def solve(brickor, depth, history):
    if brickor in history['state']:
        i = history['state'].index(brickor)
        if depth >= history['depth'][i]:
            return brickor
        history['depth'][i] = depth
    else:
        history['state'].append(brickor.copy())
        history['depth'].append(depth)
    for a, (i, j) in enumerate(zip(brickor[:-1], brickor[1:])):
        if 'S' in (i, j):
            for direction in (0, 1):
                brickor = swap(brickor, a, direction)
                depth += 1
                brickor = solve(brickor, depth, history)
                depth -= 1
                brickor = unswap(brickor, a, direction)
    return brickor    
brickor = list(input('Brickor ? '))
history = {'state': [], 'depth': []}
solve(brickor, 0, history)
print('Minsta antal drag:', history['depth'][history['state'].index(sorted(history['state'])[-1])])