texto = input("Digite uma frase:\n.").strip()

vogais = 0
consoantes = 0
digitos = 0

def Resultado():
    print("O números de vogais é: ", vogais)
    print("O números de consoantes é: ", consoantes)
    print("O números de digitos é: ", digitos)

def Contagem_Vogais(texto):
    global vogais
    for char in texto:
        if char.lower() in "aeiouáàãâéèêíìîóòõôúùû":
            vogais += 1

def Contagem_Consoantes(texto):
    global consoantes
    for char in texto:
        if char.lower() in "bcdfghjklmnpqrstvwxyz":
            consoantes += 1

def Contagem_Digitos(texto):
    global digitos
    digitos = vogais + consoantes

Contagem_Vogais(texto)
Contagem_Consoantes(texto)
Contagem_Digitos(texto)
Resultado()