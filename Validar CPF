import re
print('Validar CPF')
cpf = re.sub(r'[^0-9]','',input('Digite o CPF: '))
print('*'*20)
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito = ((resultado_digito_1 * 10) % 11)
digito = digito if digito <= 9 else 0



dez_digitos = nove_digitos + str(digito)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_gerado = f'{nove_digitos}{digito}{digito_2}'
if cpf == cpf_gerado:
    print(f'{cpf} Válido')
else:
    print(f'{cpf} Inválido')