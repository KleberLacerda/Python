print(f'{'ESCOLA PYTHON':^30}')
print('Boletim Escolar -> Turma 3ºC')
print('*'*30)

turma = list()
aluno = dict()
notas = list()

while True:
    aluno.clear()
    aluno['nome'] = str(input('Nome do aluno: '))

    notas.clear()
    for c in range(0, 4):
        notas.append(float(input(f'Digite a {c+1}ª nota: ')))
        
    aluno['notas'] = notas[:]
    aluno['media'] = sum(notas) / 4
    aluno['aprovado'] = 'SIM' if aluno['media'] >= 7 else 'NÃO'
    turma.append(aluno.copy())

    while True:
        resp = str(input('Quer adicionar outro aluno? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('[ERRO] DIGITE APENAS S OU N')
    if resp == 'N':
        break
print()
print('-='*45)
print(f'{'Boletim da Turma 3ºC':^50}')
print('-='*45)
print('cod  ', end='')
for i in aluno.keys():
    print(f'{i:<25}', end='')
print()
print('-'*90)

for k, v in enumerate(turma):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<23} ', end=' ')
    print()
print('-='*45)

# ARRUMAR ESSA PARTE DO ALGORITIMO
'''
situacao = str(input('Digite [A]provado | [R]eprovado\nDIGITE --> ')).upper()[0].strip()
if situacao == 'A':
    if turma['aprovado'] == 'SIM':
        print(f'Alunos Aprovados:\n {turma["nome"]}')
    else:
        print()
elif situacao == 'R':
    if turma['aprovado'] == 'NÃO':
        print(f'Alunos Reprovados:\n {turma["nome"]}')
    else:
        print()
else:
    print('ERRO, digitou algo errado')
'''
while True:
    busca = int(input('Mostrar notas do aluno? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(turma):
        print('ERRO, não exite')
    else:
        print(f' -- LEVANTAMENTO DO ALUNO {turma[busca]["nome"]}:')
        for i, n in enumerate(turma[busca]['notas']):
            print(f'  {i+1}ª Nota {n}')
            
    print('-='*45)




