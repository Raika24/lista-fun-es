import bibNumeros

qtde = 0
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    m = bibNumeros.testaMultiplo4(numero)
    if m == True :
        qtde += 1
    
if qtde > 0:
    print(f"Quantidade de múltiplos: {qtde} ")
else:
    print("0")