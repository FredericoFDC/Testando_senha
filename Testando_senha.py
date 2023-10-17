while True:
    print("Vamos criar uma nova senha")
    senha = str(input("Digite sua nova senha "))
    tamanho = len(senha)
    if tamanho < 5:
        print(f'Sua senha e fraca pois so contém {tamanho} digitos.')
    elif tamanho > 5:
        verificando_senha = str(input("Digite sua nova senha novamente "))
        if senha != verificando_senha:
            print("Suas senha não correspondem. Tente novamente")
        else:
            print("Sua senha foi criada com sucesso")
            break
print("Obrigado")
