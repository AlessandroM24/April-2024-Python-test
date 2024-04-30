# ESERCIZIO 2

voti_1 = [10, 9, 9, 10, 9, 10, 9]
voti_2 = [5, 6, 4, 8, 9, 8, 9, 10, 10, 10]


def calcola_media(lista_voti):
    totale_voti = 0
    gradi_voti = {"h": 0, "a": 0, "l": 0}
    lista_completa = []

    for voto in lista_voti:
        totale_voti += voto
        if voto >= 9:
            gradi_voti["h"] += 1
        elif voto >= 7:
            gradi_voti["a"] += 1
        else:
            gradi_voti["l"] += 1

    media = round(totale_voti / len(lista_voti), 3)
    lista_completa.append(media)
    lista_completa.append(gradi_voti)
    if gradi_voti["a"] == 0 and gradi_voti["l"] == 0:
        lista_completa.append("La classe è stata brava")
    return lista_completa


print(calcola_media(voti_1))
print(calcola_media(voti_2))
