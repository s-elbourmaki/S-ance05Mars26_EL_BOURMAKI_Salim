class Personne: #EL BOURMAKI Salim
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

# 1. Création de l'instance
personne1 = Personne('Salim', 21, 'salimelbourmaki1@gmail.com')

# 2. LECTURE des attributs
print(f"Nom: {personne1.nom}")     # Affiche: Salim
print(f"Âge: {personne1.age}")     # Affiche: 21
print(f"Email: {personne1.email}") # Affiche: salimelbourmaki1@gmail.com

# 3. MODIFICATION des attributs
personne1.nom = 'Salim EL BOURMAKI'     # Changement du nom
personne1.age += 1                 # Incrémentation de l'âge
personne1.email = 'salimelbourmaki1@gmail.com'

# 4. Vérification des changements
print(f"Nouveau nom: {personne1.nom}") # Salim EL BOURMAKI
print(f"Nouvel âge: {personne1.age}") # 22