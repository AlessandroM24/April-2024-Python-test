# ESERCIZIO 4

numeri_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeri_2 = [-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26]
numeri_3 = [6, -25, 3, 7, 5, 5, 7, -3, 23]


def num_pari(lista_numeri, quantita_pari):
    lista_numeri_invertita = lista_numeri[::-1]
    numeri_pari_presi = 0
    lista_numeri_pari = []

    for numero in lista_numeri_invertita:
        if numero % 2 == 0:
            lista_numeri_pari.append(numero)
            numeri_pari_presi += 1
            if numeri_pari_presi == quantita_pari:
                break
    lista_numeri_pari = lista_numeri_pari[::-1]
    return lista_numeri_pari


print(num_pari(numeri_1, 3))
print(num_pari(numeri_2, 2))
print(num_pari(numeri_3, 1))
