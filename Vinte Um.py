import random as rd
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dicionário que associa cada carta ao seu valor numérico
cartas = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

naipes = ['♥', '♦', '♠', '♣']

buy = [0]
hand = 0
score = 0

# Cria o baralho completo combinando cada carta com cada naipe
baralho_completo = [f"{carta}{naipe}" for carta in cartas for naipe in naipes]

def intro():
    clear()
    input("Você...")
    input("Sim, você!")
    input("Você mesmo!")
    input("Vamos jogar um jogo. Pegue aquele baralho ali.")

# Inicia o jogo embaralhando o baralho e distribuindo as duas primeiras cartas ao jogador
def start(): 
    clear()
    rd.shuffle(baralho_completo)
    hand = baralho_completo[0:2]
    print(f'Suas cartas são: {", ".join(hand)}')
    score = sum([cartas[carta[:-1]] for carta in hand])
    print(f'Sua pontuação é: {score}')
    return hand, score

# Função que permite ao jogador comprar cartas ou parar
def Buy(hand, score):
    game = ''
    while score < 21:
        game = input("Você compra ou para?\n[C]comprar\n[P]parar\n.").lower()
        if game == 'p':
            if score < 21 and score >= 18:
                print(f"Você para com {score} pontos.")
                break
            else:
                print("Você ainda não consegue parar!\nSó pode parar com 18 ou mais pontos.")
                continue
        elif game == 'c':
            rd.shuffle(baralho_completo)
            nova_carta = baralho_completo.pop(0)
            hand.append(nova_carta)
            clear()
            print(f'Suas cartas agora são: {", ".join(hand)}.')
            score = sum([cartas[carta[:-1]] for carta in hand])
            print(f"Sua pontuação agora é: {score}.")
            if score > 21:
                print("Você perdeu! Sua pontuação passou de 21.")
                break
            elif score == 21:
                print("Parabéns, você venceu!")
                break
            else:
                continue

        if score == 21:
            print('Parabéns, você venceu!')
            break

intro()
hand, score = start()
Buy(hand, score)