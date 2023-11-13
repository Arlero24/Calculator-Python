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
        return "Error: No es pot dividir entre zero."

def calculadora_interactiva():
    print("Calculadora By: alex_juegos_historias")
    while True:
        print("\nOperacions disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicació")
        print("4. Divisió")
        print("5. Sortir")

        opcion = input("Seleccioneu una operació (1/2/3/4/5): ")

        if opcion == '1':
            num1 = float(input("Introduïu el primer número: "))
            num2 = float(input("Introduïu el segon número: "))
            resultado = suma(num1, num2)
            print("El resultat de la suma és:", resultado)

        elif opcion == '2':
            num1 = float(input("Introduïu el primer número: "))
            num2 = float(input("Introduïu el segon número: "))
            resultado = resta(num1, num2)
            print("El resultat de la resta és:", resultado)

        elif opcion == '3':
            num1 = float(input("Introduïu el primer número: "))
            num2 = float(input("Introduïu el segon número: "))
            resultado = multiplicacion(num1, num2)
            print("El resultat de la multiplicació és:", resultado)

        elif opcion == '4':
            num1 = float(input("Introduïu el primer número: "))
            num2 = float(input("Introduïu el segon número: "))
            resultado = division(num1, num2)
            print("El resultat de la divisió és:", resultado)

        elif opcion == '5':
            print("Gràcies")
            break

        else:
            print("Opció invàlida. Seleccioneu una opció vàlida.")


if __name__ == "__main__":
    calculadora_interactiva()
