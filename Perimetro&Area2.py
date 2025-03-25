import numpy as np
import math as mt
lados = []
while True:
    op1 = input ("Qual forma você deseja calcular?\n.").strip().lower()
#AS CONDICIONAIS A SEGUIR SÃO TODAS 2D
    if op1 in ("quadrado", "qua", "q"):#QUADRADO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):#AREA
            lado = float(input("O cálculo de área é (Lado²). Qual o valor do lado(aresta)?\n."))
            resultado = lado * lado

            print("A área do quadrado é ", resultado,"\n")
            volta = input("Deseja fazer outro cálculo?\n.").strip().lower()

            if volta in ("não", "nao", "n", "no"):
                break

        elif op2 in ("perimetro", "perímetro", "p"):#PERIMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 4). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 4

            print("O perímetro do quadrado é ", resultado,"\n")
            volta = input("Deseja fazer outro cálculo?\n.").strip().lower()

            if volta in ("não", "nao", "n", "no"):
                break
        else:
            print("Insira área ou perímetro.")
    elif op1 in ("tri", "triangulo", "t", "triângulo"):#TRIANGULO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):#AREA
            base = float(input("O cálculo de área é (Base x Altura/2). Qual o valor da base(b)?\n."))
            altura = float(input("\nQual o valor de Altura(h)?\n."))

            resultado = (base * altura)/2
            print("A área do triângulo é ", resultado,"\n")
            volta = input("Deseja fazer outro cálculo?\n.").strip().lower()

            if volta in ("não", "nao", "n", "no"):
                break

        elif op2 in ("perimetro", "perímetro", "p"):#PERIMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 3). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 3

            print("O perímetro do triângulo é ", resultado,"\n")
            volta = input("Deseja fazer outro cálculo?\n.").strip().lower()

            if volta in ("não", "nao", "n", "no"):
                break
        else:
            print("Insira área ou perímetro.")
    elif op1 in ("pent", "penta", "p", "pentágono", "pentagono"):#PENTAGONO
        op2 = input("Você deseja calcular área ou perímetro?\n.").strip().lower()

        if op2 in ("area", "área", "a"):#AREA
            lado = float(input("O cálculo de área é ((Lados*5)*Apótema). Qual o valor dos lados(Aresta)?\n."))
            apotema = float(input("Qual o valor do apótema(ap/a)?\n."))

            resultado = (lado * 5) * apotema
            print("A área do pentágono é ", resultado,"\n")
            volta = input("Deseja fazer outro cálculo?\n.").strip().lower()

            if volta in ("não", "nao", "n", "no"):
                break

        elif op2 in ("perimetro", "perímetro", "p"):#PERIMETRO
            lado = float(input("O cálculo de perímetro é (Lado x 5). Qual o valor do lado(aresta)?\n."))
            resultado = lado * 5

            print("O perímetro do pentágono é ", resultado,"\n")
            volta = input("Deseja fazer outro cálculo?\n.").strip().lower()

            if volta in ("não", "nao", "n", "no"):
                break
        else:
            print("Insira área ou perímetro.")
    elif op1 in ("hex", "h",'hexágono'):#apague...
        reg = input("É um hexágono regular ou irregular?\n.").strip().lower()#REGULAR OU IRREGULAR
        
        if reg in ('reg', 'regular', 'r'):#REGULAR
            op2 = input("Você quer calcular área ou perímetro?\n.").strip().lower()

            if op2 in ("perimetro", "perímetro", "p"):#PERIMETRO
                lado = input(float("O calculo para formas regulares é: (Lados * 6). Qual o valor do lado?\n."))
                resultado = lado * 6

                print("O perímetro do hexágono é ", resultado,"\n")
            volta = input("Deseja fazer outro cálculo?\n.").strip().lower()

            if volta in ("não", "nao", "n", "no"):
                break
            if op2 in ("area", "área", "a"):#AREA
                vl = str(input("O cálculo de área é possivel ser feito usando um apotema ou calculando os lados.\nQual deles você possui?\n."))
                if vl in ('apotema', 'apótema', 'ap', 'a'):#CALCULO COM APÓTEMA
                    apotema = float(input("Qual o valor do apótema(ap/a)?\n."))
            
                    def area_hexagono_por_apotema(apotema):
                        return 2 * mt.sqrt(3) * apotema ** 2

                    resultado = apotema
                    print("A área do pentágono é ", resultado,"\n")

                elif vl in ('lado','lados', 'l', 'ld'):#CALCULO COM LADOS
                    lado = float(input("Qual o valor dos lados(L)?\n."))
            
                    def area_hexagono_por_lado(lado):
                        return (3 * mt.sqrt(3) / 2) * lado ** 2

                    resultado = lado
                    print("A área do pentágono é ", resultado,"\n")

                volta = input("Deseja fazer outro cálculo?\n.").strip().lower()

            if volta in ("não", "nao", "n", "no"):
                break
            else:
                print("Insira área ou perímetro.")
