import random as rd

numeros = list(range(1, 101))
aleatorio = rd.choice(numeros)
chute = int(input("Tente adivinhar o número que estou pensando entre 1 e 100.\n.").strip())

while chute != aleatorio:
    if chute > aleatorio:
        print("O número que você digitou é maior que o número que estou pensando.")
    elif chute < aleatorio:
        print("O número que você digitou é menor que o número que estou pensando.")
        
    chute = int(input("Tente novamente:\n.").strip())
    if chute == aleatorio:
        print("Parabéns! Você acertou!")