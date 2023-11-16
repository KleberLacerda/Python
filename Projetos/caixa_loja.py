print('='*40)
print(f'{'Lojas Teste':^40}')
print('='*40)
total = cont = 0
nota = ''
lista = []
while True:
    produto = str(input('Nome do produto: '))
    preco_produto = float(input('Preço: R$ '))
    total += preco_produto
    cont += 1
    lista.append(produto)
   
    encerrar = input('Quer adicionar mais produtos? [S/N]: ').upper()[0]

    if encerrar == 'N':
        print(f'{'FIM DA COMPRA':-^40}')
        print()
        
        break
    elif encerrar == 'S':
        continue
    else:
        print('ERROR!')

desconto = str(input('Vai dar desconto? [S/N]: ')).upper()
if desconto == 'S':
    valor_desconto = float(input('Qual o valor do desconto? '))
    valor_compra = total - (total * valor_desconto/ 100)
    
    print()
    print(f'{'Nota da Compra':^23}')
    for i, produto in enumerate(lista):
        print(f'{i + 1:.<20}', end='') 
        print(produto)

    print()
    print('='*20)   
    print(f'O total da compra foi R$ {valor_compra:.2f}')
    print()  

else:
    print()
    print(f'{'Nota da Compra':^23}')
    for i, produto in enumerate(lista):
        print(f'{i + 1:.<20}', end='') 
        print(produto)

    print()
    print('='*20)  
    print(f'O total da compra foi R$ {total:.2f}')
    print()  