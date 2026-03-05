class Vehicule:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse
        print(f"Véhicule {marque} créé")

class Voiture(Vehicule):
    def __init__(self, marque, vitesse, nb_portes):
        super().__init__(marque, vitesse) # Appel du parent
        self.nb_portes = nb_portes
        print(f"Voiture avec {nb_portes} portes")
