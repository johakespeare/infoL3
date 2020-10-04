import random

class De:
    compteur=0
    def __init__(self, nb_faces:int=6, nom:str=""):
        """
        :param nb_faces: nombre de faces du Dé (valeur par défaut : 6)
        :param nom: nom du dé ( valeur par défaut "" )
        De.compteur = compteur de Dés créés
        """
        self._nb_faces = nb_faces
        self._nom= nom
        De.compteur += 1

        if(self._nom == ""):
            self._nom= "De numero" + str(De.compteur)

    def getFaces(self):
        """
        fonction retourne le nombre de faces
        :return: nombre de faces du Dé
        """
        return(self._nb_faces)

    def setFaces(self, nb:int):
        """
        la fonction change le nombre de faces
        :param nb: le nouveau nombre de faces
        """
        if(nb>=3)and(nb<=120):
            self._nb_faces = nb
        else:
            print("le nb n'est pas compris dans l'intervalle")

    def getCompteur(cls):
        """
        :return:  le nombre de Dés créés
        """
        return(De.compteur)

    def getNom(self):
        """
        :return: le nom du Dé
        """
        return(self._nom)

    def lancer(self):
        """
        lance le Dé et retourne la valeur d'une face des Dés
        :return: valeur du dé
        """
        tirage = random.randint(1, self._nb_faces)
        return(tirage)

    def multilancer(self,nb_coups:int):
        """
        fonction qui lance plusieurs fois le dé et qui retourne le meilleur tirage
        :param nb_coups: nombre de fois qu'on lance le dé
        :return: le meilleur coup
        """
        max=0
        for i in range(nb_coups):
            coup = self.lancer()
            if coup>max:
                max = coup
        return(max)

    def __str__(self):
        """
        :return: string qui représente la classe
        """
        return("le dé a ", self._nb_faces , "faces")



class De_pipe(De):
    def __init__(self, nb_faces:int=6, borne_min: int = 0):
        super().__init__(nb_faces)
        self.__borne=borne_min

    def lancer(self):
        """
        :return:  le résultat du tirage du Dé qui est plus grand que la borne du Dé
        """
        tirage = random.randint(self.__borne, self._nb_faces)
        return(tirage)



class De_memoire(De):
    def __init__(self,nb_faces:int=6):
        super().__init__(nb_faces)
        self.__last_coup = 0

    def lancer(self):
        """
        fonction qui lance le Dé sans jamais avoir des successions de nombres identiques
        :return: le lancer du dé
        """
        tirage = random.randint(0, self._nb_faces)
        while self.__last_coup == tirage :
            tirage = random.randint(0, self._nb_faces)
        return(tirage)



class De_lettres():
    def __init__(self,liste_faces:list):
        self.liste_faces = liste_faces

    def lancer(self):
        """
        :return: le tirage du Dé
        """
        tirage = random.randint(0,len(self.liste_faces)-1)
        return(self.liste_faces[tirage])


if __name__ == "__main__":
    de = De()
    de1 = De_pipe(6,3)
    de2 = De()
    print(De.getCompteur(De))
    print(de2.getNom())
    print(de.multilancer(5))
    print(de1.__str__())
    print(de1.multilancer(5))
    de = De_lettres(["gagné","perdu","relancez","passez votre tour"])
    print(de.lancer())
    print(De.getCompteur(De))


+