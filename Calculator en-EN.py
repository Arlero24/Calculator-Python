def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero."

def calculadora_interactiva():
    print("Calculator By: alex_juegos_historias")
    while True:
        print("\nAvailable operations:")
        print("1. Sum")
        print("2. Remainder")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        opcion = input("Select an operation (1/2/3/4/5): ")

        if opcion == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            resultado = suma(num1, num2)
            print("The result of the sum is:", resultado)

        elif opcion == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            resultado = resta(num1, num2)
            print("The result of the subtraction is:", resultado)

        elif opcion == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            resultado = multiplicacion(num1, num2)
            print("The result of the multiplication is:", resultado)

        elif opcion == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = division(num1, num2)
            print("The result of the division is:", resultado)

        elif opcion == '5':
            print("Bye.")
            break

        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    calculadora_interactiva()
