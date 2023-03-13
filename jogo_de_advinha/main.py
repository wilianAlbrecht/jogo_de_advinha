# make a mini game where the computer randomly chooses a number and the user tries to guess it, at the end write on the screen the number of times the user tried until he got the correct number

# faça um mini jogo em que a maquina escolhe aleatoriamente um numero e o usuario tente advinhar, no fim escreva na tela a quantidade de vezes que o usuario tentou até acertar o numero correto


from advinha_PTBR import *
from advinha_EN import *


print("1-Português.")
print("2-English.")

lang = input("")

if lang == "1":
    advinha_PTBR()
    print("Desenvolvido por Wilian ALbrecht.")
if lang == "2":
    advinha_EN()
    print("Developed by Wilian ALbrecht.")


