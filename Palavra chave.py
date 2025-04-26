import re  # Importa o módulo 're' para trabalhar com expressões regulares
import random  # Importa o módulo 'random' para gerar escolhas aleatórias

# Solicita ao usuário se ele sabe como jogar e converte a resposta para minúsculas, removendo espaços extras
rsp = input("Vamos jogar palavra chave!\nVocê sabe como jogar?\n.").strip().lower()

# Verifica a resposta do usuário
if rsp in ("nao", "n", 'não'):  # Se o usuário responder "não"
    # Explica as regras do jogo
    print("\nÉ bem simples.\nVocê irá escrever uma frase e trocar alguma palavra da frase por um ( - )\nEste caractere será trocado por uma palavra aleatória.")

elif rsp in ("sim", "s"):  # Se o usuário responder "sim"
    # Confirma que o jogo vai começar
    print("\nOk vamos lá!")
else:  # Se a resposta não for válida
    # Solicita uma entrada válida e encerra o programa
    print("\nInsira sim ou não.")
    exit()

# Inicia o loop principal do jogo
while True:
    # Lista de palavras aleatórias que serão usadas para substituir o caractere "-"
    palavras = [
        "Cavalos elétricos", "Toupeiras albinas", "Cacto cantante", "Pinguins mafiosos", "Macacos filósofos", 
        "Gelatina radioativa", "Gnmos puonk", "Cyborgs preguiçosos", "Esquilos depressivos", "Caveiras aromáticas", 
        "Vikings veganos", "Crianças imortais", "Piratas sedentários", "Pandas incendiários", "Coelhos cyborgs", 
        "Zumbis narcisistas", "Cachorros astronautas", "Lulas detetives", "Cangurus góticos", "Bodes dançarinos", 
        "Caracóis ninjas", "Sapos aristocratas", "Tomates vingativos", "Tiranossauros míopes", "Fantasmas ansiosos", 
        "Baleias skatistas", "Pombos hackers", "Jacarés gourmet", "Samurais gripados", "Robôs bêbados", 
        "Esfinges fofoqueiras", "Minotauros hipsters", "Crianças demoníacas", "Cervejas falantes", "Gatos samurais", 
        "Fadas psicodélicas", "Tatu-bolas telepatas", "Lobos existencialistas", "Cegonhas psicopatas", "Formigas socialistas"
    ]
   
    # Solicita ao usuário que insira uma frase e remove espaços extras
    texto = input("Insira a sua frase:\n.").strip().lower()
    
    # Substitui o caractere "-" na frase por uma palavra aleatória da lista 'palavras'
    novo_texto = re.sub(r"-", lambda _: random.choice(palavras), texto)
    
    # Exibe a nova frase com as substituições
    print(novo_texto)
    
    # Pergunta ao usuário se ele quer jogar novamente
    loop = input("\nQuer jogar de novo?\n.").strip().lower()

    if loop in ("sim", "s"):  # Se o usuário quiser jogar novamente
        print("\nBora lá") 
    elif loop in ("nao", "n", 'não'):  # Se o usuário não quiser jogar novamente
        print("\nOk, adeus!")
        exit()  # Encerra o programa
    else:  # Se a resposta não for válida
        print("Insira sim ou não.")
        exit()  # Encerra o programa