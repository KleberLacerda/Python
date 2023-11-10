print('>> Perguntas e Resposta <<')
print()

perguntas = [
    {
    'Pergunta': 'Quanto é 2 + 2?',
    'Opções': ['1', '4', '6', '5'],
    'Resposta': '4',
},
{
    'Pergunta': 'Dia da Consciência Negra?',
    'Opções': ['20/11', '20/10', '20/08', '19/11'],
    'Resposta': '20/11',
},
{
    'Pergunta': 'Quem descobriu o Brasil?',
    'Opções': ['Pedro Álvares Cabral', 'Cristovão Colombo', 'Luíz Inácio Lula da Silva', 'Dom Pedro 1º'],
    'Resposta': 'Pedro Álvares Cabral',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')
    print()

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < len(opcoes):
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        qtd_acertos += 1
        print('Acertou!')
        print('-='*15)
        
    else:
        print('Errou!')
        print('-='*15)


print()

print('Você acertou', qtd_acertos,'\nde', len(perguntas), 'perguntas.') 
print()
    
    