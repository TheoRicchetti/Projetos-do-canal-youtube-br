from random import*
acho=""
senha= input("Digite a senha que vc quer encontrar: ")
letras=['1','2','3''4','5','6','7','8','9','0']
while(acho !=senha):
    acho=""
    for letra in senha:
        acholetra=letras[randint(0,49)]
        acho=str(acholetra) + str(acho)
    print(acho)
print("Senha encontrada foi: {}".format(acho))
