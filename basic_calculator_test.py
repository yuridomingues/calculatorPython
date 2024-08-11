"""TEM COMO TIRAR ESSA FUNÇÃO (PrimeiroCalculo)??"""

import os
import time

def main ():
    while True:
        number = None
        result_number = None
        operator = None
        i = 0

        print(">>> CALCULADORA: Quantas operações quiser <<<<<\n\n")
                    
        print("Soma [+]")
        print("Subtração [-]")
        print("Multiplicação [*]")
        print("Divisão [/]\n\n")
        print("Finalizar a operação [=]")

        i+=1
        number = input(f"N {i}: ")
        number = float(number)
        operator = input (": ")
        i+=1
        result_number = input(f"N {i}: ")
        result_number = float(result_number)

        result_number = firstCalculation (number, result_number, operator)

        while True:
            operator = input(": ")

            # Verificando se o usuario deseja finalizar a conta
            if operator == '=':
                print(f"{result_number}")
                operator = input("\nDeseja realizar outro calculo? [S]im ou [N]ão: ")
                operator = operator.lower()
                if operator == 's':
                    os.system('cls')
                    main()
                else:
                    print("OBRIGADO POR USAR NOSSA CALCULADORA ;)")
                    time.sleep(5)
                    return 0
            i+=1
            number = input(f"N {i}: ")
            number = float(number)
            
            if operator == '+':
                result_number = sum(number, result_number)
            elif operator == '-':
                result_number = subtraction(number, result_number)
            elif operator == '*':
                result_number = multiplication(number, result_number)
            elif operator == '/':
                result_number = division(number, result_number)
            else:
                print("\n\nPor favor, informe um operador valido! Reiniciando...")
                time.sleep(2.5)
                os.system('cls')
                continue


"""FUNÇÕES"""

# Função que vai realizar o calculo dos primeiros 2 numeros

def firstCalculation (numero, numero_calculado, operador):
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
def sum (numero, numero_calculado):
    return numero_calculado + numero

# Função que vai subtrair os numeros
def subtraction (numero, numero_calculado):
    return numero_calculado - numero

# Função que vai multiplicar os numeros
def multiplication (numero, numero_calculado):
    return numero_calculado * numero

# Função que vai dividir os numeros
def division (numero, numero_calculado):
    return numero_calculado / numero

try:
    main()
except:
    main()