from random import randint

print('Vamos jogar Par ou Ímpar')
print("-"*15)
v = 0
while True:
    j = int(input('Digite um número: '))
    pc = randint(0,10)
    s = j + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: ')).upper().strip()[0]
        print(f'Você: [{j}] \nPC: [{pc}] \nTotal: [{s}] ->', end=' ')
        print('DEU PAR' if s % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if s % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if s % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
print('-='*15)
print('GAME OVER')
print('-='*15)
print(f'Total de Vitórias {v}')