# ESERCIZIO 1

class Prodotto:
    def __init__(self, nome, prezzo, scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta

    def __str__(self):
        return f"Nome: {self.nome}, prezzo: {self.prezzo}, scorta: {self.scorta}"
