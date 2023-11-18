print('*'* 60,'\n')
print(f'{'GERADOR  DE PALPITES MEGA SENA':^60}')
print('\n','*'* 60)

from random import randint
from time import sleep
lista = []
jogos = []
palpites = int(input('Quantos palpites quer gerar? '))
total_palpites = 1
while total_palpites <= palpites:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_palpites += 1
print('\n', '*' * 5, f' SORTEANDO {palpites} JOGOS', '*' * 5, '\n')

for i, l in enumerate(jogos):
    print(f'Jogo {i+ 1}: {l}')
    sleep(1)
print('Boa Sorte!')
