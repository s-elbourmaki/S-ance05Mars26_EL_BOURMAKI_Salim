class Voiture:
    def __init__(self, marque, vitesse=0):
        self.marque = marque
        self.vitesse = vitesse
        self.en_marche = False

    def demarrer(self):
        """Démarre la voiture"""
        self.en_marche = True
        print(f"La {self.marque} démarre !")

    def accelerer(self, increment):
        if self.en_marche:
            self.vitesse += increment
            print(f"Vitesse: {self.vitesse} km/h")

    def arreter(self):
        self.en_marche = False
        self.vitesse = 0
        print(f"La {self.marque} s'arrête.")

# Utilisation
ma_voiture = Voiture("Mercedes")
ma_voiture.demarrer()      # Appel de méthode
ma_voiture.accelerer(360)   # Modification d'état