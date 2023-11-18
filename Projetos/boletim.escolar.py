print('NOME DA ESCOLA: TANTAS \nSALA: A \nPROFESSOR: KLEBER\n')
print(f'{'BOLETIM ESCOLAR ANO 2023':^40}')
print('*' * 40)

aluno = {}

while True:
    aluno['nome'] = str(input('Nome do Aluno: '))
    aluno['nota_1'] = float(input('Digite a 1º nota: '))
    aluno['nota_2'] = float(input('Digite a 2º nota: '))
    aluno['media'] = (aluno['nota_1'] + aluno['nota_2']) / 2
    
    
    decisao = str(input('Quer continuar? [S/N]: ')).upper()
    print()
    if decisao == 'N':
        break

'''
print('='*40)
print(f'{'Nº':<5}{'NOME':<10}{'MÉDIA':>8}')
print('-'*30)
for k, v in aluno.items():
    print(f'{k:.<4}{v['nome']:<10}{v['media']:>8.1f}')
'''


if aluno['media'] >= 7:
    print(f'{aluno['nome'], 'APROVADO!'}')
else:
    print(f'{aluno['nome'], 'REPROVADO!'}')

'''
ver_notas = str(input('Quer ver as notas? [S|N]: ')).upper()
if ver_notas == 'S':
    while True:
        print('='*40)
        opc = int(input('Mostrar notas de qual aluno? (999 interompe): '))
        if opc == 999:
            break
        if opc <= len(aluno) - 1:
            print(f' Notas do {aluno[opc][0]} são {aluno[opc][1]}')'''
  

print('='*40)
print('OBRIGADO POR UTILIZAR NOSSO SISTEMA!')

