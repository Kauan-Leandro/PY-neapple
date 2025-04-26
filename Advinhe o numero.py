import random as rd  # Importa o módulo 'random' e o renomeia como 'rd' para gerar números aleatórios

numeros = list(range(1, 101))  # Cria uma lista de números de 1 a 100
aleatorio = rd.choice(numeros)  # Escolhe aleatoriamente um número da lista 'numeros'

# Solicita ao usuário que tente adivinhar o número, convertendo a entrada para inteiro e removendo espaços extras
chute = int(input("Tente adivinhar o número que estou pensando entre 1 e 100.\n.").strip())

# Inicia um loop que continuará até o usuário acertar o número
while chute != aleatorio:
    if chute > aleatorio:  # Verifica se o chute do usuário é maior que o número aleatório
        print("O número que você digitou é maior que o número que estou pensando.")
    elif chute < aleatorio:  # Verifica se o chute do usuário é menor que o número aleatório
        print("O número que você digitou é menor que o número que estou pensando.")
        
    # Solicita ao usuário que tente novamente, atualizando o valor de 'chute'
    chute = int(input("Tente novamente:\n.").strip())
    
    if chute == aleatorio:  # Verifica se o usuário acertou o número
        print("Parabéns! Você acertou!")  # Exibe uma mensagem de parabéns