# coding: utf-8

class Voiture:

    def __init__(self):
        self.nom = "Basic"
        self.roues = 4
        self.moteur = 1

    def start(self):
        print("La voiture démarre")


class VoitureSport(Voiture):

    def __init__(self):
        self.nom = "Ferrari"

    def down(self):
        print("La voiture s'arrête")



ma_voiture = Voiture()
print(ma_voiture.nom)
print(ma_voiture.roues)

mvp = VoitureSport()
mvp.start()
mvp.down()