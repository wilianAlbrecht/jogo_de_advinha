import os
from random import randint


def advinha_EN():
    os.system("cls") or None

    print("You chose english... \n")
    print("How to play: ")
    print("1- The computer will choose a random number from 0 to 9")
    print("2- You need guess the correct number ")
    print("3- You start with 3 lifes, each wrong answer you will lost 1 life")
    print("4- if you lost all lifes, the game will be over \n\n")

    letra = input("Press any key... \n")

    if letra != "":
        inicio()
    else:
        inicio()

def inicio():
    os.system("cls")
    print("started ...")

    vidas = 3
    num = int(randint(0, 9))

    palpite = 0

    while palpite != num:

        print("\n\nyou have {} lifes".format(vidas))

        palpite = int(input("\nYou guess is: "))

        if palpite == num:
            os.system("cls")
            print("congratulations, you answer is correct. {} lives left ".format(vidas))
        else:
            os.system("cls")
            print("Wrong answer, try again")
            vidas = vidas -1
            if vidas > 0:
                continue
            else: 
                print("\n\n-----game over-----")
                print("Yours lifes is over. The correct answer is {}".format(num))
                break
            
        
    print("\n\nThank you to played.\n\n")

                