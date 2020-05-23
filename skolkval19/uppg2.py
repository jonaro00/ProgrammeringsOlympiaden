n = int(input('Antal rader ? '))
m = int(input('Antal kolumner ? '))
text = list(input('Krypterad text ? '))
grid = [['']*m for n in range(n)]
path = []
x = 0
y = 0
dx = 1
dy = 1
for i, c in enumerate(text):
    if (y, x) not in path:
        path.append((y, x))
    if i == len(text) - 1:
        break
    while (y, x) in path:
        if x + dx not in range(m):
            dx *= -1
        if y + dy not in range(n):
            dy *= -1
        x += dx
        y += dy
for i in range(n):
    for j in range(m):
        if (i, j) in path:
            grid[i][j] = text.pop(0)
final_message = ''
for i, j in path:
    final_message += grid[i][j]
print('Meddelande:', final_message)