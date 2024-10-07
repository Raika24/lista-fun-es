import bibNumeros

numero = int(input("Digite um número inteiro: "))
qd = bibNumeros.contaDivisores(numero)

if qd == 2:
    print("Primo")
else:
    print("Não primo")