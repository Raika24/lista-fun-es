import ANO
lista_estacao = []
lista_visitantes = []
for i in range(6):
    mes = str.lower(input("Mês: "))
    E = ANO.defineEstacao (mes)
    qtde_visitantes = int(input("Quantidade de visitantes: "))
     
    
    lista_visitantes.append(qtde_visitantes)

    lista_estacao.append(E)

M_visitacao = lista_visitantes[0]
estacao_M_visitacao = lista_estacao[0]
for i in range(len(lista_visitantes)):
    if lista_visitantes[i] > M_visitacao:
        M_visitacao = lista_visitantes[i]
        estacao_M_visitacao = lista_estacao[i]

print(f"O maior número de visitantes em um único mês, foi no período {estacao_M_visitacao} ")