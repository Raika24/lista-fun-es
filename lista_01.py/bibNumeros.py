def testaMultiplo4 (a):
    if a % 4 == 0:
        return True
    else:
        return False

def contaDivisores (a):
    qtde_divisores = 0
    for i in range (1,a+1):
        if a % i == 0:
            qtde_divisores += 1
    
    return qtde_divisores

