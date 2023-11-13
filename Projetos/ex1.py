print(f'{'Caixa - Loja KL':-^40}')
total = cont = 0
lista = []
while True:
    produto = str(input('Nome do produto: '))
    preco_produto = float(input('Preço: R$ '))
    total += preco_produto
    cont += 1
    lista.append(produto)
   
    encerrar = input('Quer adicionar mais produtos? [S/N]: ').upper()[0]

    if encerrar == 'N':
        print(f'{'FIM DO PROGRAMA':-^40}')
        break
    elif encerrar == 'S':
        continue
    else:
        print('ERROR!')

lista = tuple(lista)


print(f'O total da compra foi R$ {total:.2f}')
print(f'Lista de compra: {lista}')