class CompteBanquaire(object):
    def __init__(self,nom,solde): #construction de la classe
        self.nom = nom
        self.solde = solde
    def depot(self,montant):
        self.solde += montant
        print(f"dêpot de {montant} éffectué")
    def retrait(self,montant):
        if(montant > self.solde):
            print("votre montant ne correspond à votre solde")
        else:
            self.solde -= montant
            print(f"retrait de {montant} éffectué")
    def affiche(self):
        print(f"le solde du compte banquaire de {self.nom} est de {self.solde} XOF")

