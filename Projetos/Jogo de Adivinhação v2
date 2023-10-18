from random import randint

print('Olá, sou seu computador. E quero te desafiar!')
pc = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    j = int(input('Entre 0 e 10, qual número estou pensando? '))
    palpite += 1
    if j == pc:
        acertou = True
    else:
        if j < pc:
            print('Mais... Tente denovo!')
        else:
            print('Menos... Tente denovo!')
print('Acertou, com {} palpite. \nO número que estava pensando era {} '.format(palpite, pc))