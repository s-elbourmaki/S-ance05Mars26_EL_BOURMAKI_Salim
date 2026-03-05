class Vehicule:
    def demarrer(self):
        print("Le véhicule démarre")

class Voiture(Vehicule):
    def demarrer(self):  # Redéfinition
        print("La voiture démarre en douceur")

class Moto(Vehicule):
    def demarrer(self):  # Redéfinition
        print("La moto rugit au démarrage!")

# Utilisation polymorphe
vehicules = [Voiture(), Moto()]

for v in vehicules:
    v.demarrer()  # Appelle la bonne version
