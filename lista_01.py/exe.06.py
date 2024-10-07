import bibLetras

qtde_vogal = 0
for i in range(6):
    caractere = str.lower(input("Digite uma letra: "))
    v = bibLetras.testaVogal(caractere)
    if v == True:
        qtde_vogal += 1

print(f"Quantidade de vogais: {qtde_vogal}")