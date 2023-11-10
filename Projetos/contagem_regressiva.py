print('\033[1;36;49m <> CONTAGEM REGRESSIVA PARA ANO NOVO! <>\033[m')

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('🎆 \033[4;39;49m Feliz Ano Novo!\033[m 🎆 ')