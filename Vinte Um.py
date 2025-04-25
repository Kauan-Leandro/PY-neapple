import random as rd  # Importa o módulo random para embaralhar o baralho
import os  # Importa o módulo os para limpar a tela

def clear():  # Define uma função para limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela no Windows ou em outros sistemas

# Dicionário que associa cada carta ao seu valor numérico
cartas = {
    "A": 1,  # Ás vale 1
    "2": 2,  # Cartas numéricas valem seu próprio número
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,  # Valetes, Damas e Reis valem 10
    "Q": 10,
    "K": 10
}

# Lista com os símbolos dos naipes
naipes = ['♥', '♦', '♠', '♣']

# Inicializa variáveis (não usadas diretamente no código)
buy = [0]  # Não é usada
hand = 0  # Inicializa a mão como 0 (será substituída por uma lista mais tarde)
score = 0  # Inicializa o score como 0

# Cria o baralho completo combinando cada carta com cada naipe
baralho_completo = [f"{carta}{naipe}" for carta in cartas for naipe in naipes]

def intro():  # Função para introduzir o jogo
    clear()  # Limpa o terminal antes de iniciar a introdução
    input("Você...")  # Exibe mensagens para o jogador
    input("Sim, você!")
    input("Você mesmo!")
    input("Vamos jogar um jogo. Pegue aquele baralho ali.")

def start(): 
    clear()  # Limpa o terminal antes de iniciar o jogo
    rd.shuffle(baralho_completo)  # Embaralha o baralho completo
    hand = baralho_completo[0:2]  # Seleciona as duas primeiras cartas do baralho
    print(f'Suas cartas são: {", ".join(hand)}')  # Exibe as cartas da mão inicial
    score = sum([cartas[carta[:-1]] for carta in hand])  # Calcula o score inicial somando os valores das cartas
    print(f'Sua pontuação é: {score}')  # Exibe o score inicial
    return hand, score  # Retorna a mão e o score para serem usados na próxima função

def Buy(hand, score):  # Função para permitir que o jogador compre cartas ou pare
    game = ''  # Inicializa a variável que armazena a escolha do jogador
    while score < 21:  # Continua enquanto o score for menor que 21
        game = input("Você compra ou para?\n[C]comprar\n[P]parar\n.").lower()  # Pergunta ao jogador se ele quer comprar ou parar
        if game == 'p':  # Se o jogador escolher parar
            if score < 21 and score >= 18:  # Permite parar apenas se o score for entre 18 e 21
                print(f"Você para com {score} pontos.")  # Exibe a pontuação final
                break  # Sai do loop
            else:
                print("Você ainda não consegue parar!\nSó pode parar com 18 ou mais pontos.")  # Mensagem de erro
                continue  # Continua o loop
        elif game == 'c':  # Se o jogador escolher comprar
            rd.shuffle(baralho_completo)  # Embaralha o baralho novamente
            nova_carta = baralho_completo.pop(0)  # Retira a primeira carta do baralho
            hand.append(nova_carta)  # Adiciona a nova carta à mão
            clear()  # Limpa o terminal antes de mostrar as novas cartas
            print(f'Suas cartas agora são: {", ".join(hand)}.')  # Exibe todas as cartas na mão
            score = sum([cartas[carta[:-1]] for carta in hand])  # Recalcula o score somando os valores das cartas na mão
            print(f"Sua pontuação agora é: {score}.")  # Exibe o novo score
            if score > 21:  # Se o score ultrapassar 21
                print("Você perdeu! Sua pontuação passou de 21.")  # Exibe mensagem de derrota
                break  # Sai do loop
            elif score == 21:  # Se o score for exatamente 21
                print("Parabéns, você venceu!")  # Exibe mensagem de vitória
                break  # Sai do loop
            else:
                continue  # Continua o loop se o score estiver entre 0 e 21

        if score == 21:  # Verifica novamente se o score é 21 (redundante, pode ser removido)
            print('Parabéns, você venceu!')  # Exibe mensagem de vitória
            break  # Sai do loop

# Fluxo principal do jogo
intro()  # Chama a introdução do jogo
hand, score = start()  # Inicia o jogo e obtém a mão inicial e o score
Buy(hand, score)  # Permite que o jogador compre cartas ou pare