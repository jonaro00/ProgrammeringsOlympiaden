from math import ceil
ettor, tvåor, treor, fyror = (int(input(f'Hur många {n}-grupper ? ')) for n in range(1, 5))
ettor -= min(ettor, treor)
if tvåor % 2:
    ettor -= min(2, ettor)
print('Behövs:', fyror + treor + ceil(tvåor / 2) + ceil(ettor / 4))