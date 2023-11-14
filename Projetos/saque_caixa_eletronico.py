from time import sleep 

print('='*50)
print(f'{'* Simulação Saque Caixa Eletrônico *':^50}')
print('='*50)

saldo = 1000
cedula = 0
total_cedula = 0

while True:
    saque = int(input('Qual valor será sacado: R$ '))
    print()

    if saque > saldo:
        print(f'Saldo Indisponível -> Disponível R$ {saldo}')
        print('Tente Novamente.')
        print('='*50)
    else:
        saldo_atual = saldo - saque
        print(f'Saldo Atual: R${saldo_atual}')
        print('='*50)
        encerrar = str(input('Quer realizar outro saque?[S/N]: ')).upper()[0]

        while encerrar == 'S':
            saque = int(input('Qual valor será sacado: R$ '))
            print()

            if saque > saldo_atual:
                print(f'Saldo Indisponível -> Disponível R$ {saldo_atual}')
                print('Tente Novamente.')
                print('='*50)
            else:
                saldo_atual -= saque
                print(f'Saldo Atual: R${saldo_atual}')
                print('='*50)
            encerrar = str(input('Quer realizar outro saque?[S/N]: ')).upper()[0]

       
        print('='*50)
        print(f'\nSaldo R${saldo_atual}\n')  
        break

sleep(1)
print('Obrigado pela preferência')
print('='*50)
    
















