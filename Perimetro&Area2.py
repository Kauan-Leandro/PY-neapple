import math as mt  # Importa o módulo 'math' para cálculos matemáticos
lados = []  # Inicializa uma lista vazia (não está sendo usada no código atual)

# Inicia um loop infinito para permitir múltiplos cálculos
while True:
    # Solicita ao usuário que escolha uma forma geométrica
    op1 = input("Qual forma você deseja calcular?\n.").strip().lower()

    # Verifica se a forma escolhida é um quadrado
    if op1 in ("quadrado", "qua", "q"):  # QUADRADO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):  # ÁREA
            lado = float(input("O cálculo de área é (Lado²). Qual o valor do lado(aresta)?\n."))
            resultado = lado * lado  # Calcula a área do quadrado
            print("A área do quadrado é ", resultado, "\n")

        elif op2 in ("perimetro", "perímetro", "p"):  # PERÍMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 4). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 4  # Calcula o perímetro do quadrado
            print("O perímetro do quadrado é ", resultado, "\n")

        else:
            print("Insira área ou perímetro.")  # Mensagem para entrada inválida

    # Verifica se a forma escolhida é um triângulo
    elif op1 in ("tri", "triangulo", "t", "triângulo"):  # TRIÂNGULO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):  # ÁREA
            base = float(input("O cálculo de área é (Base x Altura/2). Qual o valor da base(b)?\n."))
            altura = float(input("\nQual o valor de Altura(h)?\n."))
            resultado = (base * altura) / 2  # Calcula a área do triângulo
            print("A área do triângulo é ", resultado, "\n")

        elif op2 in ("perimetro", "perímetro", "p"):  # PERÍMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 3). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 3  # Calcula o perímetro do triângulo
            print("O perímetro do triângulo é ", resultado, "\n")

        else:
            print("Insira área ou perímetro.")  # Mensagem para entrada inválida

    # Verifica se a forma escolhida é um pentágono
    elif op1 in ("pent", "penta", "p", "pentágono", "pentagono"):  # PENTÁGONO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):  # ÁREA
            lado = float(input("O cálculo de área é ((Lados*5)*Apótema). Qual o valor dos lados(Aresta)?\n."))
            apotema = float(input("Qual o valor do apótema(ap/a)?\n."))
            resultado = (lado * 5 * apotema) / 2  # Calcula a área do pentágono
            print("A área do pentágono é ", resultado, "\n")

        elif op2 in ("perimetro", "perímetro", "p"):  # PERÍMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 5). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 5  # Calcula o perímetro do pentágono
            print("O perímetro do pentágono é ", resultado, "\n")

        else:
            print("Insira área ou perímetro.")  # Mensagem para entrada inválida

    # Verifica se a forma escolhida é um hexágono
    elif op1 in ("hex", "h", "hexágono"):  # HEXÁGONO
        reg = input("É um hexágono regular ou irregular?\n.").strip().lower()

        if reg in ('reg', 'regular', 'r'):  # HEXÁGONO REGULAR
            op2 = input("Você quer calcular área ou perímetro?\n.").strip().lower()

            if op2 in ("perimetro", "perímetro", "p"):  # PERÍMETRO
                lado = float(input("O cálculo para formas regulares é: (Lados * 6). Qual o valor do lado?\n."))
                resultado = lado * 6  # Calcula o perímetro do hexágono
                print("O perímetro do hexágono é ", resultado, "\n")

            elif op2 in ("area", "área", "a"):  # ÁREA
                lado = float(input("Qual o valor dos lados(L)?\n."))
                resultado = (3 * mt.sqrt(3) / 2) * lado ** 2  # Calcula a área do hexágono
                print("A área do hexágono é ", resultado, "\n")

            else:
                print("Insira área ou perímetro.")  # Mensagem para entrada inválida

    # Verifica se a forma escolhida é um heptágono
    elif op1 in ("hept", "hepta", "h", "heptágono", "heptagono"):  # HEPTÁGONO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):  # ÁREA
            lado = float(input("O cálculo de área é ((Lados*7)*Apótema/2). Qual o valor dos lados(Aresta)?\n."))
            apotema = float(input("Qual o valor do apótema(ap/a)?\n."))
            resultado = (lado * 7 * apotema) / 2  # Calcula a área do heptágono
            print("A área do heptágono é ", resultado, "\n")

        elif op2 in ("perimetro", "perímetro", "p"):  # PERÍMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 7). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 7  # Calcula o perímetro do heptágono
            print("O perímetro do heptágono é ", resultado, "\n")

        else:
            print("Insira área ou perímetro.")  # Mensagem para entrada inválida

    # Verifica se a forma escolhida é um octógono
    elif op1 in ("oct", "octo", "o", "octógono", "octogono"):  # OCTÓGONO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):  # ÁREA
            lado = float(input("O cálculo de área é ((Lados*8)*Apótema/2). Qual o valor dos lados(Aresta)?\n."))
            apotema = float(input("Qual o valor do apótema(ap/a)?\n."))
            resultado = (lado * 8 * apotema) / 2  # Calcula a área do octógono
            print("A área do octógono é ", resultado, "\n")

        elif op2 in ("perimetro", "perímetro", "p"):  # PERÍMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 8). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 8  # Calcula o perímetro do octógono
            print("O perímetro do octógono é ", resultado, "\n")

        else:
            print("Insira área ou perímetro.")  # Mensagem para entrada inválida

    # Verifica se a forma escolhida é um eneágono
    elif op1 in ("ene", "eneágono", "eneagono"):  # ENEÁGONO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):  # ÁREA
            lado = float(input("O cálculo de área é ((Lados*9)*Apótema/2). Qual o valor dos lados(Aresta)?\n."))
            apotema = float(input("Qual o valor do apótema(ap/a)?\n."))
            resultado = (lado * 9 * apotema) / 2  # Calcula a área do eneágono
            print("A área do eneágono é ", resultado, "\n")

        elif op2 in ("perimetro", "perímetro", "p"):  # PERÍMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 9). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 9  # Calcula o perímetro do eneágono
            print("O perímetro do eneágono é ", resultado, "\n")

        else:
            print("Insira área ou perímetro.")  # Mensagem para entrada inválida

    # Verifica se a forma escolhida é um decágono
    elif op1 in ("dec", "decágono", "decagono"):  # DECÁGONO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):  # ÁREA
            lado = float(input("O cálculo de área é ((Lados*10)*Apótema/2). Qual o valor dos lados(Aresta)?\n."))
            apotema = float(input("Qual o valor do apótema(ap/a)?\n."))
            resultado = (lado * 10 * apotema) / 2  # Calcula a área do decágono
            print("A área do decágono é ", resultado, "\n")

        elif op2 in ("perimetro", "perímetro", "p"):  # PERÍMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 10). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 10  # Calcula o perímetro do decágono
            print("O perímetro do decágono é ", resultado, "\n")

        else:
            print("Insira área ou perímetro.")  # Mensagem para entrada inválida

    else:
        print("Forma geométrica não reconhecida. Tente novamente.")  # Mensagem para forma inválida

    # Pergunta ao usuário se deseja realizar outro cálculo
    volta = input("Deseja fazer outro cálculo?\n.").strip().lower()
    if volta in ("não", "nao", "n", "no"):  # Se o usuário não quiser continuar
        break  # Encerra o loop e o programa