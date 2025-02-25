numero = int(input("\nDigite um número positivo: "))

while numero <= 0: 
    print ("\nNúmero iválido, digite um número positivo!")
    numero = int(input("\nDigite um número positivo: "))

if (numero > 0):    
    
    print("\nNúmeros ímpares:")
    for i in range (1, numero + 1):
        if i % 2 != 0:
           print(i)

print("\nFim da contagem!\n")
