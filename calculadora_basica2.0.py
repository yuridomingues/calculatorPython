import os
import time

def main ():
    while True:
        numero = None
        numero_calculado = None
        operador = None
        i = 0

        print(">>> CALCULADORA: Quantas operações quiser <<<<<\n\n")
                    
        print("Soma [+]")
        print("Subtração [-]")
        print("Multiplicação [*]")
        print("Divisão [/]\n\n")
        print("Finalizar a operação [=]")

        i+=1
        numero = input(f"N {i}: ")
        numero = float(numero)
        operador = input (": ")
        i+=1
        numero_calculado = input(f"N {i}: ")
        numero_calculado = float(numero_calculado)

        numero_calculado = PrimeiroCalculo (numero, numero_calculado, operador)

        while True:
            operador = input(": ")

            if operador == '=':
                print(f"{numero_calculado}")
                operador = input("\nDeseja realizar outro calculo? [S]im ou [N]ão: ")
                operador = operador.lower()
                if operador == 's':
                    os.system('cls')
                    main()
                else:
                    print("FIZ UM JEITO MERDA DE FINALIZAR O PROGRAMA, TEM UM BREAK NA LINHA 59 PRA MEXER DEPOIS! VAI FECHAR EM 5 SEG")
                    time.sleep(5)
                    break
            i+=1
            numero = input(f"N {i}: ")
            numero = float(numero)
            if operador == '+':
                numero_calculado = Soma(numero, numero_calculado)
            elif operador == '-':
                numero_calculado = Subtracao(numero, numero_calculado)
            elif operador == '*':
                numero_calculado = Multiplicacao(numero, numero_calculado)
            elif operador == '/':
                numero_calculado = Divisao(numero, numero_calculado)
            else:
                print("\n\nPor favor, informe um operador valido! Reiniciando...")
                time.sleep(2.5)
                os.system('cls')
                continue

        break #temporario

"""FUNÇÕES"""

# Função que vai realizar o calculo dos primeiros 2 numeros
def PrimeiroCalculo (numero, numero_calculado, operador):
    if operador == '+':
        return numero + numero_calculado
    elif operador == '-':
        return numero - numero_calculado
    elif operador == '*':
        return numero * numero_calculado
    elif operador == '/':
        return numero / numero_calculado
    else:
        print("\n\nPor favor, informe um operador valido! Reiniciando...")
        time.sleep(2.5)
        os.system('cls')
        main()

# Função que vai somar os numeros
def Soma (numero, numero_calculado):
    return numero_calculado + numero

# Função que vai subtrair os numeros
def Subtracao (numero, numero_calculado):
    return numero_calculado - numero

# Função que vai multiplicar os numeros
def Multiplicacao (numero, numero_calculado):
    return numero_calculado * numero

# Função que vai dividir os numeros
def Divisao (numero, numero_calculado):
    return numero_calculado / numero

try:
    main()
except:
    main()
