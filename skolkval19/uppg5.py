n = int(input('Storlek ? '))
rows_max = [int(input(f'Rad {i}, högsta stapeln ? ')) for i in range(1,n+1)]
cols_max = [int(input(f'Kolumn {i}, högsta stapeln ? ')) for i in range(1,n+1)]
max_grid = [[min(i, j) for j in cols_max] for i in rows_max]
min_grid = [[j for j in i] for i in max_grid]
for lap in range(2):
    for i, (this_row, rm) in enumerate(zip(min_grid, rows_max)):
        for j, (c, cm) in enumerate(zip(this_row, cols_max)):
            if lap == 0:
                if j == i:
                    break
            elif j < i:
                continue
            this_max = min(rm, cm)
            if this_max == 1:
                continue
            x = this_row[:]
            x.remove(c)
            y = [r[j] for r in min_grid]
            y.remove(c)
            if max(x) >= this_max and max(y) >= this_max:
                this_row[j] = 1
print('Min:', sum(sum(r) for r in min_grid))
print('Max:', sum(sum(r) for r in max_grid))