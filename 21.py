class Personne: #EL BOURMAKI Salim
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

personne1 = Personne('Salim', 21, 'salimelbourmaki1@gmail.com')

print(f"Nom: {personne1.nom}")  
print(f"Âge: {personne1.age}")    
print(f"Email: {personne1.email}")

personne1.nom = 'Salim EL BOURMAKI'     
personne1.age += 1                 
personne1.email = 'salimelbourmaki1@gmail.com'

print(f"Nouveau nom: {personne1.nom}") 
print(f"Nouvel âge: {personne1.age}") 