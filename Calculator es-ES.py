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
        return "Error: No se puede dividir entre cero."

def calculadora_interactiva():
    print("Calculadora By: alex_juegos_historias")
    while True:
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Seleccione una operación (1/2/3/4/5): ")

        if opcion == '1':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = suma(num1, num2)
            print("El resultado de la suma es:", resultado)

        elif opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = resta(num1, num2)
            print("El resultado de la resta es:", resultado)

        elif opcion == '3':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion(num1, num2)
            print("El resultado de la multiplicación es:", resultado)

        elif opcion == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = division(num1, num2)
            print("El resultado de la división es:", resultado)

        elif opcion == '5':
            print("Gracias por usar la Calculadora Interactiva.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    calculadora_interactiva()
