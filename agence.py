from voiture import Voiture
from datetime import datetime
import numpy as np
class Agence :
    
    def __init__(self):
        self.voitures = []
    
    def ajouter(self,v):
        self.voitures.append(v)

    def afficher(self):
        for v in self.voitures:
            v.afficher()

    def charger(self,nomfichier):
        with open(nomfichier,"r") as fichier :
            for ligne in fichier :
                segment=ligne.rstrip().split(';')
                matricule=segment[0]
                marque=segment[1]
                kilometrage=int(segment[2])
                date=datetime.strptime(segment[3],'%d/%m/%Y')
                v=Voiture(matricule,marque,kilometrage,date)
                self.ajouter(v)
    def rechercher(self):
        I=[]
        for v in self.voitures:
           vect= v.convertir_en_vecteur()
           I.append(vect)
        I=np.array(I)
        
        marque=input('donner marque ')
        kilometrage=int(input ('donner kilometrage '))
        date =datetime.strptime(input("saisir la date de circulation"),'%d/%m/%Y')
        vreq=Voiture(marque,kilometrage,date)
        indexreq=vreq.convertir_en_vecteur()





if(__name__ == '__main__'):
    a=Agence()
    a.charger('voitures.csv')
    a.afficher()
    print(a.rechercher())
