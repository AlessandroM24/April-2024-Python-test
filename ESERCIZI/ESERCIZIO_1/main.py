# ESERCIZIO 1

from prodotto import Prodotto
from GestoreMagazzino import GestoreMagazzino

#  Prodotti e magazzino
prodotto1 = Prodotto("Pasta", 10, 5)
prodotto2 = Prodotto("Carne", 3, 10)
prodotto3 = Prodotto("Formaggio", 5, 3)
magazzino = GestoreMagazzino(10)

# Aggiunta dei prodotti al magazzino.
magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
magazzino.aggiungi_prodotto(prodotto3)

print(magazzino.ottenere_dizionario_prodotti())  # Stampa tutti i prodotti presenti nel magazzino.

print(magazzino.calcola_costi_magazzinaggio())

magazzino.rimuovi_prodotto(prodotto2)  # Rimuove prodotto2 dal magazzino.
print(magazzino.ottenere_dizionario_prodotti())  # Stampa tutti i prodotti tranne prodotto2 (è stato rimosso).
