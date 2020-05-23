antal = int(input('Antal staplar ? '))
staplar = [int(input(f'Stapel {i} ? ')) for i in range(1, antal+1)]
behöver = 0
väghöjd = 0
for a in reversed(staplar):
    väghöjd += behöver
    behöver = max(0, väghöjd - a)
    if a >= väghöjd:
        väghöjd = a
print('Extra kartonger:', väghöjd - staplar[0])