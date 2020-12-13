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



maV = Voiture()
print(dir(maV)) ## Montres les fonctionnalités
print(maV.__dict__) ## Montre les paramètres