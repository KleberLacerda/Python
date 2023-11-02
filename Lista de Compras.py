from time import sleep
import os

print('Lista de Compras')

lista = []

while True:
    print('*'*18)
    opcao = input('[I] inserir \n[E] excluir \n[L] listar \n[S] sair \n\nDigite uma opção -> ').upper()

    if opcao == 'I':
        os.system('cls')
        
        item = input('Digite o item: ')
        lista.append(item)

    elif opcao == 'E':
        os.system('cls')

        for i, item in enumerate(lista):
            print(i, item)
        print('*'*15)

        excluir = input('Deseja excluir qual item: ')
        apagar = int(excluir)

        del lista[apagar]

    elif opcao == 'L':
        os.system('cls')

        if len(lista) == 0:
            print('Nada na lista \n')

        for i, item in enumerate(lista):
            print(i, item)

    elif opcao == 'S':
        break

    else:
        print('\nOpção Inválida \n')
        

os.system('cls')
print('Saindo...\n')
sleep(1)
print('Programa Encerrado.')