import bibGaleriaArte

cont = 50
qtde_quadro = 0
qtde_escult = 0

for i in range(cont):
    nome_obra = str.upper(input("Nome: "))
    tipo = bibGaleriaArte.consultaTipo (nome_obra)
    if tipo == "Quadro":
        qtde_quadro += 1
    elif tipo == "Escultura":
        qtde_escult += 1

if qtde_quadro > qtde_escult:
    print("Dispõe-se uma quantidade maior de quadros do que esculturas.")
elif qtde_escult > qtde_quadro:
    print("Dispõe-se uma quantidade maior de esculturas do que quadros ")
elif qtde_quadro == qtde_escult:
    print("Quantidade igual de quadro e esculturas.")