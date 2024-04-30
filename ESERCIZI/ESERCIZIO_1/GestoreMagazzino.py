# ESERCIZIO 1

class GestoreMagazzino:
    def __init__(self, costo_magazzinaggio):  # Costo per immagazzinare ogni prodotto per un mese.
        self.prodotti = {}
        self.costo_magazzinaggio = costo_magazzinaggio

    def aggiungi_prodotto(self, prodotto):
        self.prodotti[prodotto.nome] = prodotto

    def rimuovi_prodotto(self, prodotto):
        self.prodotti.pop(prodotto.nome, 0)

    def calcola_costi_magazzinaggio(self):
        totale = 0
        for prodotto in self.prodotti:
            totale += self.prodotti[prodotto].prezzo * self.prodotti[prodotto].scorta * self.costo_magazzinaggio
        return totale

    # Ritorna un nuovo dizionario contenente questa volta al posto dell'oggetto, il __str__ (to string) dell'oggetto
    # così da essere leggibile.
    def ottenere_dizionario_prodotti(self):
        prodotti_str = {}

        for prodotto in self.prodotti:
            prodotti_str[prodotto] = self.prodotti[prodotto].__str__()

        return prodotti_str
