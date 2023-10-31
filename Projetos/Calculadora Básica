from time import sleep
print(' -=-=-\033[4;39m Calculadora Básica\033[m -=-=-')
while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    op = input('Digite o operador [+|-|/|*]: ')

    numeros_validos = None
    try:  
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        print('Tente novamente.')
        print('-='*20)
        continue

    OPERADORES_PERMITIDOS = '+-/*'

    if op not in OPERADORES_PERMITIDOS:
        print('Operador inválido.')
        print('Tente novamente.')
        print('-='*20)
        continue

    if len(op) > 1:
        print('Digite apenas um operador.')
        print('-='*20)
        continue
    
    if op == '+':
        print(f'Resultado = {num_1_float + num_2_float:.2f}')
    elif op == '-':
        print(f'Resultado = {num_1_float - num_2_float:.2f}')
    elif op == '/':
        print(f'Resultado = {num_1_float / num_2_float:.2f}')
    else:
        print(f'Resultado = {num_1_float * num_2_float:.2f}')


    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print('-='*20)

    if sair is True:
        break

print('Finalizando...')
sleep(1)
print('Programa Encerrado.')
