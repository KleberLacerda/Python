times = ('Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Flamengo',
        'Athletico-PR', 'Fluminense', 'Cuiabá', 'São Paulo', 'Corinthians', 'Fortaleza', 
        'Internacional', 'Santos', 'Vasco', 'Bahia', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG',)

print(f'Times do Brasileirão 2023: {times}')
print('='*140)
print()
print(f'Classificados para Copa Libertadores: {times[:4]}')
print('='*140)
print()
print(f'Zona do Rebaixamento Z-4: {times[-4:]}')
print('='*140)
print()
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*140)
print()
print(f'Qual posição do São Paulo? {times.index('São Paulo')+1}ª')
print()
