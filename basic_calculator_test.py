import os
import time

def main():
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

        i += 1
        number = get_valid_number(f"N {i}: ")
        operator = input(": ")
        i += 1
        result_number = get_valid_number(f"N {i}: ")

        result_number = first_calculation(number, result_number, operator)

        while True:
            operator = input(": ")

            # Checking if the user wants to close the account
            if operator == '=':
                print(f"{result_number}")
                operator = input("\nDo you want to perform another calculation? [Yes] or [N]no: ")
                operator = operator.lower()
                if operator == 'y':
                    os.system('cls')
                    break
                else:
                    print("Thank you for using our calculator ;)")
                    time.sleep(5)
                    return 0

            i += 1
            number = get_valid_number(f"N {i}: ")
            
            operator_functions = {
                '+': sum,
                '-': subtraction,
                '*': multiplication,
                '/': division
            }

            if operator in operator_functions:
                result_number = operator_functions[operator](number, result_number)
            else:
                print("\n\nPlease enter a valid operator! Restarting...")
                time.sleep(2.5)
                os.system('cls')
                continue


def first_calculation(number, calculated_number, operator):
    operator_functions = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    if operator in operator_functions:
        return operator_functions[operator](number, calculated_number)
    else:
        print("\n\nPlease enter a valid operator! Restarting...")
        time.sleep(2.5)
        os.system('cls')
        main()


def sum(number, calculated_number):
    return calculated_number + number


def subtraction(number, calculated_number):
    return calculated_number - number


def multiplication(number, calculated_number):
    return calculated_number * number


def division(number, calculated_number):
    return calculated_number / number


def get_valid_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Please enter a valid number!")


try:
    main()
except:
    main()