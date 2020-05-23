n = int(input('Behöver antal? '))
m = int(input('Har antal? '))
behöver = list(sorted((int(input('Behöver längd ? ')) for _ in range(n)), reverse=True))
har = list(sorted((int(input('Har längd ? ')) for _ in range(m)), reverse=True))
köp = []
for i in behöver:
    if har:
        if i <= har[0]:
            har.pop(0)
            continue
    köp.append(i)
print('Antal:', len(köp))
print('Längder:', *reversed(köp))