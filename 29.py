class Vehicule:
    def __init__(self, marque, vitesse):
        self.__marque = marque
        self.__vitesse = vitesse
        print(f"Véhicule {self.__marque} créé")

class Voiture(Vehicule):
    def __init__(self, marque, vitesse, nb_portes):
        super().__init__(marque, vitesse)
        self.__nb_portes = nb_portes
        print(f"Voiture avec {self.__nb_portes} portes")

ma_voiture = Voiture("Peugeot", 50, 5)
print(f"Marque via mangling : {ma_voiture._Vehicule__marque}")