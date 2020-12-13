class Voiture(object):

    def __init__(self):
        self.nom = "Ma voiture" # on ajoute un paramètre
        self.roues = "4"

    def donneLeModule(self):
        return print('250')
        
    def getRoues(self):
        return print(self.roues)

    def setRoues(self, nbr):
        self.roues = nbr




maVoiture = Voiture() # On décalre une variable
print(maVoiture.nom) # On appele un des paramètres
maVoiture.donneLeModule() # On appele la function
maVoiture.getRoues() # On appele la fonction qui permet de dire le nombre de roue
maVoiture.setRoues(8) # On change le nombre de roue
maVoiture.getRoues() # On reapele la fonction