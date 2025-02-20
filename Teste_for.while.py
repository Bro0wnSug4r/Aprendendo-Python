numero = int(input("\nDigite um número interio e positivo: "))
x = 0

while numero <= 0:
    print("Número inválido! Digite um número maior que 0.")
    numero = int(input("\nDigite um número interio e positivo: "))

for x in range(numero+1):
    print (x)

print("\n")