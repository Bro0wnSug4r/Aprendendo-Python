numero = int(input("\nDigite um número (ou digite 0 para finalizar): "))
soma = 0 

while (numero != 0):
   soma += numero 
   numero = int(input("\nDigite um número (ou digite 0 para finalizar): "))
    
if numero == 0:
        print(f"\nA soma dos números é: {soma}\n")