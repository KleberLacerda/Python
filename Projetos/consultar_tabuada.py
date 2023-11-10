num = int(input('Digite um número para ver sua tabuada: '))
print('-='*10)
for c in range(1, 11):
    soma = num * c
    print('{} x {:2} = {}'.format(num, c, soma))
print('-='*10)
