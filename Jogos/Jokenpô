from random import randint
from time import sleep

jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('{:=^40}'.format(' VAMOS JOGAR '))
print('''QUAL SUA ESCOLHA:
[ 0 ] - PAPEL
[ 1 ] - PEDRA
[ 2 ] - TESOURA''')
player = int(input('JOGADA: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('>=<' * 10)
print('\033[1;35;40m COMPUTADOR jogou {}\033[m'.format(jogadas[pc]))
print('\033[1;36;40m VOCÊ jogou {} \033[m'.format(jogadas[player]))
print('>=<' * 10)
if pc == 0: # PEDRA
    if player == 0:
        print('{:=^20}'.format('\033[4;39;40m EMPATOU\033[m'))
    elif player == 1:
        print('{:=^20}'.format('\033[1;32;49m VOCÊ GANHOU\033[m'))
    elif player == 2:
        print('{:=^20}'.format('\033[1;32;49m COMPUTADOR GANHOU\033[m'))
    else:
        print('{:=^20}'.format('\033[4;31;49m JOGADA INVÁLIDA\033[m'))
elif pc == 1: # PAPEL
    if player == 0:
        print('{:=^20}'.format('\033[1;32;49m COMPUTADOR GANHOU \033[m'))
    elif player == 1:
        print('{:=^20}'.format('\033[4;39;40m EMPATOU \033[m'))
    elif player == 2:
        print('{:=^20}'.format('\033[1;32;49m VOCÊ GANHOU \033[m'))
    else:
        print('{:=^20}'.format('\033[4;31;49m JOGADA INVÁLIDA \033[m'))
elif pc == 2: # TESOURA
    if player == 0:
        print('{:=^20}'.format('\033[1;32;49m VOCÊ GANHOU \033[m'))
    elif player == 1:
        print('{:=^20}'.format('\033[1;32;49m COMPUTADOR GANHOU\033[m'))
    elif player == 2:
        print('{:=^20}'.format('\033[4;39;40m EMPATOU \033[m'))
    else:
        print('{:=^20}'.format('\033[4;31;49m JOGADA INVÁLIDA \033[m'))