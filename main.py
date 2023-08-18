from second import *
#name: main.py
#goal: programme qui permet de crée un compte faire le dêpot et le retrait et afficher les informations sur le compte.
#author: EKLOU Kossi Dodji

#exemple de programme
i = "oui"
print("programme pour crée un compte bancaire et éffectuée des opérations")
nom = input("Entrez votre nom : ")


compte0 = CompteBanquaire(nom,0) #instancier une classe qui prend pour paramètre le montant et le nom
while i == "oui":
    choix = 0
    compte0.affiche()
    print("1- Effectuée un dêpot")
    print("2- Effectuée un retrait")
    choix = int(input("Tapez votre choix 1 ou 2 pour éffectuée l'opération : "))
    if choix == 1:
        montant = int(input("entrez votre montant : "))
        compte0.depot(montant)
        compte0.affiche()
    elif choix == 2:
        montant1 = int(input("entrez votre montant : "))
        compte0.retrait(montant1)
        compte0.affiche()
    else:
        print("Erreur de frappe")
    i = input("voulez vous éffectuer encore une opération  tapez oui ou non : ")
