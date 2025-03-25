import re
import random

rsp = input("Vamos jogar palavra chave!\nVocê sabe como jogar?\n.").strip().lower()
    
if rsp in ("nao","n",'não'):
        print("\nÉ bem simples.\nVocê ira escrever uma frase e trocar alguma palavra que da frase por um ( - )\nEste caractere será trocado por uma palavra aleatoria.")
        
elif rsp in ("sim","s"):
        print("\nOk vamos lá!")
else:
        print("\nInsira sim ou não.")
        exit()

while True:
    palavras = ["Cavalos elétricos", "Toupeiras albinas", "Cacto cantante", "Pinguins mafiosos", "Macacos filósofos", "Gelatina radioativa", "Gnmos puonk", 
                "Cyborgs preguiçosos", "Esquilos depressivos", "Caveiras aromáticas", "Vikings veganos", "Crianças imortais", "Piratas sedentários", "Pandas incendiários", 
                "Coelhos cyborgs", "Zumbis narcisistas", "Cachorros astronautas", "Lulas detetives", "Cangurus góticos", "Bodes dançarinos", "Caracóis ninjas", "Sapos aristocratas", 
                "Tomates vingativos", "Tiranossauros míopes", "Fantasmas ansiosos", "Baleias skatistas", "Pombos hackers", "Jacarés gourmet", "Samurais gripados", "Robôs bêbados", 
                "Esfinges fofoqueiras", "Minotauros hipsters", "Crianças demoníacas", "Cervejas falantes", "Gatos samurais", "Fadas psicodélicas", "Tatu-bolas telepatas", 
                "Lobos existencialistas", "Cegonhas psicopatas", "Formigas socialistas"]
   
    texto = input("Insira a sua frase:\n.").strip().lower()
    novo_texto = re.sub(r"-", lambda _: random.choice(palavras), texto)
    print(novo_texto)
    
    loop = input("\nQuer jogar denovo?\n.").strip().lower()

    if loop in ("sim","s"):
           print("\nBora lá") 
    elif loop in ("nao","n",'não'):
            print("\nOk, adeus!")
            exit()
    else:
        print("Insira sim ou não.")
        exit()