print('\033[4;36;49m Calculadora de IMC \033[m')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('Seu IMC {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')