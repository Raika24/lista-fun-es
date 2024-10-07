import ANO

qtde_total_visitantes = 0
for i in range (6):
    mes = str.lower(input("Mês: "))
    E = ANO.defineEstacao (mes)
    qtde_visitantes = int(input("Quantidade de visitantes: "))
    if E == "Primavera":
        qtde_total_visitantes += qtde_visitantes

print(qtde_total_visitantes)