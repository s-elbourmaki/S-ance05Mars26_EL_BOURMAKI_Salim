class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class Salarie(Personne):
    def __init__(self, nom, age, salaire, numero_somme):
        Personne.__init__(self, nom, age) 
        self.salaire = salaire
        self.numero_somme = numero_somme

class Etudiant(Personne):
    def __init__(self, nom, age, cne_etudiant, notes):
        Personne.__init__(self, nom, age)
        self.cne_etudiant = cne_etudiant
        self.notes = notes

class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, age, salaire, numero_somme, cne_etudiant, notes, departement, annee_inscription):
        Salarie.__init__(self, nom, age, salaire, numero_somme)
        Etudiant.__init__(self, nom, age, cne_etudiant, notes)
        self.departement = departement
        self.annee_inscription = annee_inscription

    def AfficherInfos(self):
        print(f"--- Doctorant: {self.nom} ---")
        print(f"Annee d'Inscription: {self.annee_inscription}")
        print(f"CNE: {self.cne_etudiant} | Salaire: {self.salaire}")
        print(f"Département: {self.departement}")

if __name__ == "__main__":
    mon_doctorant = Doctorant("Salim EL BOURMAKI", 26, 0000, "S123", "S132150978", [15, 18], "Genie Informatique", 2026)
    mon_doctorant.AfficherInfos()
