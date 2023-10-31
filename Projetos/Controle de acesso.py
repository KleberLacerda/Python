senha_salva = '123456'
login_salvo = 'kleber.lacerda'
login_digitado = ' '
senha_digitada = ' '
repeticoes = 0

while (senha_salva != senha_digitada) or (login_salvo != login_digitado):
    print(f'{repeticoes+1}º Tentativa')
    login_digitado = input('Login: ')
    senha_digitada = input('Senha: ')
    print('xxx'*10)
    repeticoes += 1

    if senha_salva == senha_digitada and login_salvo == login_digitado:
        print('Acesso Liberado')
        

    elif senha_salva == senha_digitada or login_salvo == login_digitado:
        print('Login ou senha inválido')
        print('xxx'*10)
        
        
    elif repeticoes > 2:
        print('Acesso bloqueado')
        print('Após 3 tentativas')
        break
        
    
