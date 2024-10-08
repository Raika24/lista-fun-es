import bibGaleriaArte

cont = 5
qtde_total = 0

for i in range(cont):
    nome_obra = str.lower(input("Nome: "))
    artista = bibGaleriaArte.consultaArtista(nome_obra)
    tipo = bibGaleriaArte.consultaTipo (nome_obra)

    if artista == "Adélia Machado": 
       if tipo == "Escultura":
          qtde_obras = bibGaleriaArte.consultaQuantObras(artista)
          qtde_total += 1

print(F"Quantidade de esculturas de Adélia Machado: {qtde_total}")