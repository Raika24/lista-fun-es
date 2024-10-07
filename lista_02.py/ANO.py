def defineEstacao (mes):
  
  if mes == "dezembro" or mes == "janeiro" or mes == "fevereiro":
    estacao = "Inverno"
    return estacao
  elif mes == "março" or mes == "abril" or mes == "maio":
    estacao = "Primavera"
    return estacao
  elif mes == "setembro" or mes == "novembro"  or  mes == "outubro":
    estacao = "Outono"
    return estacao
  elif mes == "junho" or mes == "julho" or mes == "agosto":
    estacao = "Verão"
    return estacao