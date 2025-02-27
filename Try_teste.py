try:
    numerador = int(input("\nDigite o numerador: "))
    denominador = int(input("\nDigite o denominador: "))

    resultado = numerador/denominador

    print(f"\nO resultado da divisão é: {resultado}")

except ZeroDivisionError:
    print("\nERRO: Não é possivel dividir por 0.")

except ValueError:
    print("\nERRO: Por favor, digite um número inteiro.")

finally:
    print("\nFim do programa!\n")