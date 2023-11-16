from random import choice
from time import sleep
import os

print('Sorteio do Produto XXXXX')
print('='*20)
print('Escreva o nome dos participantes')
lista = []
while True:
    nome = str(input('Nome: '))
    lista.append(nome)
    encerrar = str(input('Acresentar mais alguém [S/N]: ')).upper()
    os.system('cls')
    
    if encerrar == 'N':
        ('Vamos fazer o SORTEIO!!!')
        break
   
sorteado = choice(lista)
print('Nome SORTEADO foi -> ', end=''), sleep(3), print(f'{sorteado:>20}')
print()