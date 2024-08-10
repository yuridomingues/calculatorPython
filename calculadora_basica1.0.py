import os
import time

# Função principal
def main():
    while True:
        print(">>> CALCULADORA BASICA DO BASICO DA BASE BASISTICA <<<<<\n\n")
                
        print("Soma [+]")
        print("Subtração [-]")
        print("Multiplicação [*]")
        print("Divisão [/]")

        numero1 = input("\n\n1° Valor: ")
        numero1 = float(numero1)
        operacao = input("\nOperação: ")
        numero2 = input("\n2° Valor: ")
        numero2 = float(numero2)

        # START IF
        if operacao == '+': # Caso o usuario queira realizar uma soma
            Soma(numero1, numero2)
    
        elif operacao == '-': # Caso o usuario queira realizar uma subtração
            Subtracao(numero1, numero2)

        elif operacao == '*': # Caso o usuario queira realizar uma multiplicação
            Multiplicacao(numero1, numero2)

        elif operacao == '/': # Caso o usuario queira realizar uma divisão
            Divisao(numero1, numero2)

        else: # Caso o usuario informe uma operação invalida
            print("ATENÇÃO: Informe uma operação valida!!! Reiniciando...")
            time.sleep(2.5)
            os.system('cls')
            continue
        # END IF

        operacao = input("\n\nDigite [S] caso queira realizar outra operação: ")
        operacao = operacao.lower()

        # START IF
        if operacao == 's': # Caso o usuario queira fazer outra operação
            os.system('cls')
            continue

        else: # Caso o usuario não queira fazer outra operação
            print("ADEUS")
            break
        # END IF

# Função de Soma
def Soma (numero1, numero2):
    os.system('cls')
    print(f"{numero1} + {numero2} = {numero1 + numero2}")

# Função de Subtração
def Subtracao (numero1, numero2):
    os.system('cls')
    print(f"{numero1} - {numero2} = {numero1 - numero2}")

# Função de Multiplicação
def Multiplicacao (numero1, numero2):
    os.system('cls')
    print(f"{numero1} * {numero2} = {numero1 * numero2}")

# Função de Divisão
def Divisao (numero1, numero2):
    os.system('cls')
    print(f"{numero1} / {numero2} = {numero1 / numero2}")


# O PROGRAMA COMEÇA AQUI
try: 
    main()
except:
    os.system('cls')
    main()
