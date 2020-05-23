from math import sqrt
m = int(input('Minimalt antal rutor ? '))
n = int(input('Maximalt antal rutor ? '))
möjliga = [(l, q // l) for q, r in zip(range(m, n+1), (sqrt(q) for q in range(m, n+1))) for l in range(1, int(r+1)) if q % l == 0]
# möjliga = []
# for q, r in zip(range(m, n+1), (sqrt(q) for q in range(m, n+1))):
#     for l in range(1, int(r+1)):
#         if q % l == 0:
#             möjliga.append((l, q // l))
skillnader = [abs(l - b) for l, b in möjliga]
print('Bästa mått:', *möjliga[skillnader.index(min(skillnader))])