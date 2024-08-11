"""TEM COMO TIRAR ESSA FUNÇÃO (PrimeiroCalculo)??"""
# Sim, so precisaremos implementar a funcao dentro da main. - Yuri
# Mas o lance é tirar esses calculos do programa, mas nao sei se tem como - Jao, Malvadao

import os
import time

def main ():
    while True:
        number = None
        result_number = None
        operator = None
        i = 0

        print(">>> CALCULATOR: As many operations as you want <<<<<\n\n")
                    
        print("Sum [+]")
        print("Subtraction [-]")
        print("Multiplication [*]")
        print("Division [/]\n\n")
        print("Finish the operation [=]")


        i+=1
        number = float(input(f"N {i}: "))
        operator = input (": ")
        i+=1
        result_number = float(input(f"N {i}: "))

        result_number = firstCalculation (number, result_number, operator)

        while True:
            operator = input(": ")

            # Checking if the user wants to close the account

            if operator == '=':
                print(f"{result_number}")
                operator = input("\nDo you want to perform another calculation? [Yes] or [N]no: ")
                operator = operator.lower()
                if operator == 'y':
                    os.system('cls')
                    main()
                else:
                    print("Thank you for using our calculator ;)")
                    time.sleep(5)
                    return 0
            i+=1
            number = float(input(f"N {i}: "))
            
            if operator == '+':
                result_number = sum(number, result_number)
            elif operator == '-':
                result_number = subtraction(number, result_number)
            elif operator == '*':
                result_number = multiplication(number, result_number)
            elif operator == '/':
                result_number = division(number, result_number)
            else:
                print("\n\nPlease enter a valid operator! Restarting...")
                time.sleep(2.5)
                os.system('cls')
                continue


# Function that will calculate the first 2 numbers

def firstCalculation (number, calculated_number, operator):
    if operator == '+':
        return number + calculated_number
    elif operator == '-':
        return number - calculated_number
    elif operator == '*':
        return number * calculated_number
    elif operator == '/':
        return number / calculated_number
    else:
        print("\n\nPlease enter a valid operator! Restarting...")
        time.sleep(2.5)
        os.system('cls')
        main()


# numbers sum
def sum (number, calculated_number):
    return calculated_number + number

# numbers substraction
def subtraction (number, calculated_number):
    return calculated_number - number

# numbers multiplication
def multiplication (number, calculated_number):
    return calculated_number * number

# numbers division
def division (number, calculated_number):
    return calculated_number / number

try:
    main()
except:
    main()