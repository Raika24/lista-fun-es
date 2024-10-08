import bibGaleriaArte

cont = 60
valor_total = 0

for i in range(cont):
    nomes_obras = str.upper(input("Nome da obra: "))
    preco = bibGaleriaArte.consultaPreco (nomes_obras)
    artista =bibGaleriaArte.consultaArtista (nomes_obras)
    if artista == "Leonardo Resende":
        valor_total += preco

print(f"Valor total das obras de Leonardo Resende: R${valor_total:.2f}")