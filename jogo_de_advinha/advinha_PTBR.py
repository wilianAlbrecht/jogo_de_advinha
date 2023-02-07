import os
from random import randint

def advinha_PTBR():
    
    os.system("cls")

    print("Voce escolheu português... \n")
    print("Como jogar: ")
    print("1- O computador ira sortar um numero aleatorio de 0 a 9 ")
    print("2- Você terá que advinhar qual o numero foi sorteado ")
    print("3- Você começará com apenas 3 vidas, cada erro ira consumir uma vida")
    print("4- Se as vidas chegar a 0 você perderá \n\n")

    letra = input("pressione qualquer tecla para continuar... \n")

    if letra != "":
        inicio()
    else:
        inicio()


def inicio():
    os.system("cls")
    print("começou ...")

    vidas = 3
    num = int(randint(0, 9))

    palpite = 0

    while palpite != num:

        print("\n\nvocê tem {} vidas".format(vidas))

        palpite = int(input("\nSeu palpite: "))

        if palpite == num:
            os.system("cls")
            print("parabéns você acertou com {} vidas restantes ".format(vidas))
        else:
            os.system("cls")
            print("Numero errado")
            vidas = vidas -1
            if vidas > 0:
                continue
            else: 
                print("\n\n-----game over-----")
                print("Suas vidas chegaram ao fim. A respota correta era {}".format(num))
                break
        
    
    print("\n\nObrigado por jogar.\n\n")

            