#login
login = input("Digite o login: ")
senha = int(input("Digite a senha: "))
if login == "admin" and senha == 1234:
    print("Acesso permitido!")
else: 
    print("Acesso negado!")

#3 tentativas
tentativas = 0
max_attempts = 3

def obter_login():
    global tentativas
    login = input("Digite o login: ")
    senha = int(input("Digite a senha: "))

    if login == "admin" and senha == 1234 and tentativas < 3:   
        print("Acesso permitido!")
        return True
    else:
        tentativas += 1
        print("Acesso negado! Tentativas restantes:", max_attempts - tentativas)
        return False


while tentativas <= max_attempts:
    result = obter_login ()
    if result:
        break
    else:
        if tentativas == max_attempts:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")
            break
        else:

            print("Tente novamente.")
