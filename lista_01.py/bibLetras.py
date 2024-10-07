def testaVogal (a):
    vogal = 0
    vogais = ["a", "e", "i", "o", "u", "á","é", "í", "ó", "ú", "â", "ê", "î", "ô", "û", "ã", "à", "A", "E", "I", "O", "U","õ" ]
    for i in range(len(vogais)):
        if vogais[i] == a:
            vogal += 1
    if vogal >0:
        return True
    else:
        return False