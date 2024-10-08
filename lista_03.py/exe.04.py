import bibGaleriaArte

cont = 5
valor_total = 0
qtde_obras = 0

for i in range (cont):
    nome_obra = str.lower(input("Nome: "))
    preco = bibGaleriaArte.consultaPreco (nome_obra)
    tipo = bibGaleriaArte.consultaTipo(nome_obra)
    if tipo == "Quadro":
        valor_total += preco
        qtde_obras += 1

media = valor_total / qtde_obras
print(f"Valor média dos quadros: {media:.2f} ")