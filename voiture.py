from datetime import datetime
import numpy as np
marques={'kia':1,'citroen':2,'ferrari':3,'ford':4,'mercedes':5}
class Voiture :

    def __init__(self,matricule='',marque='',kilometrage=0,date_circulation=datetime.now()):
        self.matricule=matricule
        self.marque=marque
        self.kilometrage=kilometrage
        self.date_circulation=date_circulation
    def saisie(self):
        self.matricule=input("saisir la matricule")
        self.marque=input("saisir la marque")
        self.kilometrage=int (input("saisir le kilometrage"))
        #s =input("saisir la date de circulation");
        self.date_circulation=datetime.strptime(input("saisir la date de circulation"),'%d/%m/%Y')
    
    def afficher(self):
        date=self.date_circulation.strftime('%d/%m/%Y')
        print('%-10s|%-10s|%-8d|%-15s' %(self.matricule,self.marque,self.kilometrage,date))

    def convertir_en_vecteur(self):
        marque =np.array([marques[self.marque],self.kilometrage,self.date_circulation.year])
        return marque


if(__name__ == '__main__'):
    v =Voiture()
    v.saisie()
    v.afficher()
    print(v.convertir_en_vecteur())