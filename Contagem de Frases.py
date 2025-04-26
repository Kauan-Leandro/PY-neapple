# Solicita ao usuário que insira uma frase e remove espaços em branco no início e no final da entrada
texto = input("Digite uma frase:\n.").strip()

# Inicializa as variáveis globais para contar vogais, consoantes e dígitos
vogais = 0
consoantes = 0
digitos = 0

# Função para exibir os resultados das contagens
def Resultado():
    # Exibe o número de vogais
    print("O número de vogais é: ", vogais)
    # Exibe o número de consoantes
    print("O número de consoantes é: ", consoantes)
    # Exibe o número de dígitos
    print("O número de dígitos é: ", digitos)

# Função para contar as vogais na string fornecida
def Contagem_Vogais(texto):
    global vogais  # Declara que a variável vogais é global
    for char in texto:  # Itera sobre cada caractere da string
        # Verifica se o caractere é uma vogal (incluindo vogais acentuadas)
        if char.lower() in "aeiouáàãâéèêíìîóòõôúùû":
            vogais += 1  # Incrementa o contador de vogais

# Função para contar as consoantes na string fornecida
def Contagem_Consoantes(texto):
    global consoantes  # Declara que a variável consoantes é global
    for char in texto:  # Itera sobre cada caractere da string
        # Verifica se o caractere é uma consoante
        if char.lower() in "bcdfghjklmnpqrstvwxyz":
            consoantes += 1  # Incrementa o contador de consoantes

# Função para contar os dígitos na string fornecida
def Contagem_Digitos(texto):
    global digitos  # Declara que a variável digitos é global
    for char in texto:  # Itera sobre cada caractere da string
        # Verifica se o caractere é um dígito
        if char.isdigit():
            digitos += 1  # Incrementa o contador de dígitos

# Chama a função para contar as vogais no texto
Contagem_Vogais(texto)
# Chama a função para contar as consoantes no texto
Contagem_Consoantes(texto)
# Chama a função para contar os dígitos no texto
Contagem_Digitos(texto)
# Exibe os resultados das contagens
Resultado()