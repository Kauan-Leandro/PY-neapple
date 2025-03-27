import random as rd
from colorama import Fore, Style

# 1 = JOGADOR /// 2 = INIMIGO
# ATAQUE X2
# DEFESA X1

# PERSONAGENS
# 1 = GUERREIRO
# 2 = MAGO

def Guerreiro():  # Função que define o personagem guerreiro
    print(Fore.LIGHTYELLOW_EX + "Você escolheu o guerreiro!")
    life1 = 30
    defesa = 6
    ataque = 10
    return life1, defesa, ataque

def Mago():  # Função que define o personagem mago
    print(Fore.LIGHTYELLOW_EX + "Você escolheu o mago!")
    life1 = 20
    defesa = 4
    ataque = 15
    return life1, defesa, ataque

def D6():  # Função que simula um dado de 6 faces
    return rd.choice([1, 2, 3, 4, 5, 6])

def Ataque_1(life2, ataque):  # Função que simula um ataque do jogador
    input(Fore.LIGHTRED_EX + "[VEZ DO JOGADOR]...")
    atk1 = D6() + ataque
    def2 = D6()
    print(Fore.LIGHTBLUE_EX + "O ataque foi de: ", atk1)
    print(Fore.LIGHTGREEN_EX + "A defesa foi de: ", def2)
    if atk1 > def2:
        print(Fore.LIGHTRED_EX + "-- O ataque foi bem sucedido!")
        life2 = Vida_Oponente(life2, atk1, def2)
    else:
        print(Fore.LIGHTRED_EX + "-- O ataque falhou!")
    return life2

def Ataque_2(life1, ataque_inimigo):  # Função que simula um ataque do inimigo
    input(Fore.LIGHTRED_EX + "[VEZ DO INIMIGO]...")
    atk2 = D6() + ataque_inimigo
    def1 = D6()
    print(Fore.LIGHTGREEN_EX + "O ataque foi de: ", atk2)
    print(Fore.LIGHTBLUE_EX + "A defesa foi de: ", def1)
    if atk2 > def1:
        print(Fore.LIGHTRED_EX + "-- O ataque foi bem sucedido!")
        life1 = Vida_Jogador(life1, atk2, def1)
    else:
        print(Fore.LIGHTRED_EX + "-- O ataque falhou!")
    return life1

def Vida_Oponente(life2, atk1, def2):  # Função que simula a perca de vida do oponente
    life2 -= (atk1 - def2)
    return life2

def Vida_Jogador(life1, atk2, def1):  # Função que simula a perca de vida do jogador
    life1 -= (atk2 - def1)
    return life1

def status(life1, life2):  # Função que mostra o status do jogador e do inimigo
    print(Fore.LIGHTBLUE_EX + "A vida do jogador é: ", life1)
    print(Fore.LIGHTGREEN_EX + "A vida do inimigo é: ", life2)

def selecionar_inimigo():  # Função que seleciona um inimigo aleatoriamente
    inimigos = [
        {"nome": "Goblin", "vida": 40, "ataque": 8},
        {"nome": "Orc", "vida": 50, "ataque": 12},
        {"nome": "Dragão", "vida": 70, "ataque": 20},
    ]
    return rd.choice(inimigos)

def prologo():  # Função que exibe o prólogo do jogo
    print(Fore.LIGHTYELLOW_EX + "\nVocê foi capturado por um império cruel e agora servirá de entretenimento no coliseu.")
    print(Fore.LIGHTYELLOW_EX + "Sua única chance de liberdade é derrotar os três inimigos que serão enviados contra você.")
    print(Fore.LIGHTYELLOW_EX + "Após derrotar cada inimigo, você será recompensado com uma arma ou armadura mais forte.")
    print(Fore.LIGHTYELLOW_EX + "Lute pela sua vida e conquiste sua liberdade!\n")
    input(Fore.LIGHTRED_EX + "Pressione Enter para continuar...\n")

def recompensa(ataque, defesa):  # Função que concede uma recompensa ao jogador
    print(Fore.LIGHTGREEN_EX + "Parabéns! Você recebeu uma recompensa!")
    escolha = input(Fore.LIGHTCYAN_EX + "Escolha sua recompensa:\n1-[ARMA MAIS FORTE]\n2-[ARMADURA MAIS FORTE]\n.")
    if escolha == "1":
        ataque += 5
        print(Fore.LIGHTGREEN_EX + "Seu ataque aumentou em 5 pontos!")
    elif escolha == "2":
        defesa += 3
        print(Fore.LIGHTGREEN_EX + "Sua defesa aumentou em 3 pontos!")
    else:
        print(Fore.RED + "Você não escolheu uma recompensa válida!")
    return ataque, defesa

def main():  # Função principal
    global life1, life2, defesa, ataque
    prologo()  # Exibe o prólogo
    print(Fore.RED + "Escolha seu personagem:")
    print(Fore.LIGHTCYAN_EX + "1 - Guerreiro")
    print(Fore.LIGHTCYAN_EX + "2 - Mago")
    personagem = input(Fore.RED + "Digite o número correspondente ao personagem: ")  # Escolha do personagem
    if personagem == "1":
        life1, defesa, ataque = Guerreiro()
        arma = input(Fore.RED + "Escolha sua arma:\n1-[ESPADA CURTA]\n2-[LANÇA]\n3-[ESPADA LARGA]\n.")
        if arma == "1":
            ataque += 5
        elif arma == "2":
            ataque += 10
        elif arma == "3":
            ataque += 15
        else:
            print(Fore.RED + "Você não escolheu nenhuma arma!")
            exit()
    elif personagem == "2":
        life1, defesa, ataque = Mago()
        magia = input(Fore.RED + "Escolha sua magia:\n1-[FOGO]\n2-[GELO]\n3-[RAIO]\n.")
        if magia == "1":
            ataque += 5
        elif magia == "2":
            ataque += 10
        elif magia == "3":
            ataque += 15
        else:
            print(Fore.RED + "Você não escolheu nenhuma magia!")
            exit()
    else:
        print(Fore.RED + "Você não escolheu nenhum personagem!")
        exit()

    inimigos_derrotados = 0
    while inimigos_derrotados < 3:  # O jogador precisa derrotar 3 inimigos
        inimigo = selecionar_inimigo()
        life2 = inimigo["vida"]
        ataque_inimigo = inimigo["ataque"]
        print(Fore.LIGHTMAGENTA_EX + f"Você enfrentará um {inimigo['nome']} com {life2} de vida e {ataque_inimigo} de ataque!\n")

        while life1 > 0 and life2 > 0:
            action = input(Fore.RED + "[CONTINUAR = ENTER]").upper()  # Ação do jogador
            if action == "":  # Jogador ataca
                life2 = Ataque_1(life2, ataque)
                if life2 <= 0:  # Verifica se o inimigo morreu
                    print(Fore.LIGHTGREEN_EX + f"Você derrotou o {inimigo['nome']}!")
                    inimigos_derrotados += 1
                    ataque, defesa = recompensa(ataque, defesa)  # Concede recompensa
                    break
                status(life1, life2)
                life1 = Ataque_2(life1, ataque_inimigo)  # Inimigo ataca
                if life1 <= 0:  # Verifica se o jogador morreu
                    print(Fore.RED + "Você perdeu!")
                    exit()
                status(life1, life2)

    print(Fore.LIGHTGREEN_EX + "Parabéns! Você derrotou todos os inimigos e conquistou sua liberdade!")

if __name__ == "__main__":
    main()