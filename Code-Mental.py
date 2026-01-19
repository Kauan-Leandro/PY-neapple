import os

def clear():  # Limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    choice = input("Escolha uma opção:\n1. Contar vogais\n2. Separar caracteres\n3. Sair\n")
    clear()
    while choice in ['1', '2', '3', '4']:
        if choice == '1':
            contar_vogais()
            break
        elif choice == '2':
            separar_caracteres()
            break
        elif choice == '3':
            pares_impares()
            break
        elif choice == '4':
            sair()
        else:
            print("Opção inválida. Tente novamente.")
            choice = input("Escolha uma opção:\n1. Contar vogais\n2. Separar caracteres\n3. Pares & Impares\n4. Sair\n")
            clear()

def separar_caracteres():
    clear()
    print("[SEPARADOR DE CARACTERES]")
    texto = input("Digite uma palavra/frase: ").strip()
    if texto == '':
        print("Nenhum caractere digitado.")
        return

    # Separar os caracteres em uma única linha
    caracteres_separados = '-'.join(list(texto))
    print(f"Caracteres separados: {caracteres_separados}")

def contar_vogais():
    clear()
    print("[CONTADOR DE VOGAIS]")
    texto = input("Digite uma palavra/frase: ").strip()
    if texto == '':
        print("Nenhum caractere digitado.")
        return

    contador = 0
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Determinar se é uma palavra ou frase
    tipo = 'frase' if ' ' in texto else 'palavra'

    # Contar vogais
    for char in texto:
        if char in vogais:
            contador += 1

    # Exibir resultado
    if contador == 1:
        print(f"A {tipo} possui {contador} vogal.")
    elif contador > 1:
        print(f"A {tipo} possui {contador} vogais.")
    else:
        print("Nenhuma vogal encontrada.")

def sair():
    print("Saindo...")
    exit()

def pares_impares():
    clear()
    print("[PARES E ÍMPARES]")
    numeros = input("Digite números separados por espaço: ").strip()
    if numeros == '':
        print("Nenhum número digitado.")
        return

    numeros = list(map(int, numeros.split()))
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

main()