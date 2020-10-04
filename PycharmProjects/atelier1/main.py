""""
#auteur: Johanna Fericean
#date : 07/09/2020
#description : atelier 1 de programmation L3
#version =1
"""
#exercice 1

def calcul_salaire(nb_heures:int,taux_horaire:int):
    """cette fonction calcul le salaire en fonction du nombre d'heures et le taux horaires
     en comptant les heures supplémentaires"""
    total = nb_heures * taux_horaire
    if(nb_heures>160):
        total+= (nb_heures-160)*taux_horaire*0.25
        if(nb_heures>200):
            total+= (nb_heures-200)*taux_horaire*0.25
    return(total)

#appel de la fonction calcul_salaire
#print(calcul_salaire(201,2))




#exercice 7

def election():
    """
    cette fonction :
    """
    liste_candidats=[]
    gagnant=0
    candidat_favoris = 0
    i =0
    while i<4:
        liste_candidats.append(int(input("donnez le score")))
        i+=1

    if(liste_candidats[0]>50):
        print (" il est élu")
    elif(liste_candidats[0]>12,5):
        for i in (1,3):
            if (liste_candidats[i]>liste_candidats[0]):
                if (liste_candidats[i] > 50):
                     gagnant = 1
                else :
                   candidat_favoris+=1

    if(candidat_favoris==0):
        print("favorable")
    if(candidat_favoris>0):
        if(gagnant==1):
            print("perdu")
        else:
            print("défavorable")


#election()



#exercice 8

def assurance()->str:
    #l'age minimum pour avoir plus d'offres
    AGE_MINIMUM = 25
    #l'ancienneté minimal(en année) de permis  pour avoir plus d'offres
    ANCIENNETE_MIN_PERMIS = 2
    #l'ancienneté(en année) nécessaire pour avoir la couleur supérieure
    ANCIENNETE_MIN_ASSUR = 1
    # les différents tarifs sont associés à un score numérique dans un dico
    tarifs = dict()
    tarifs[-1]= "pas assuré" #si l'individu a -1 point il n'est pas assuré
    tarifs[0] = "tarif rouge"# si l'individu a 0 point il a le tarif rouge etc
    tarifs[1] = "tarif orange"
    tarifs[2] = "tarif vert"
    tarifs[3]= " tarif bleu"

    #initialisation de la variable nb_points
    nb_points = -1
    # saisies des données
    age = int(input("quel âge avez vous ?"))
    anciennete_permis = int(input("depuis combien de temps avez vous votre permis ?"))
    nb_accident = int(input("combien d'accidents avez vous eu ?"))
    anciennete_client = int(input("depuis combien d'années êtes vous assuré dans notre assurance ?"))

    #selon leur age, leur ancienneté de permis, leurs nombres d'accidents, ils recoivent des points
    if((age<AGE_MINIMUM)and(anciennete_permis<ANCIENNETE_MIN_PERMIS)):
        if(nb_accident==0):
            #1 point pour accéder au tarif rouge
            nb_points+=1
    elif((age>AGE_MINIMUM)and(anciennete_permis>=ANCIENNETE_MIN_PERMIS)):
        if(nb_accident==0):
            # 3 points pour accéder au tarif vert
            nb_points+=3
        if(nb_accident==1):
            # 2 points pour accéder au tarif orange
            nb_points+=2
        if(nb_accident==2):
            # 1 point pour accéder au tarif rouge
            nb_points+=1
    else:
        if(nb_accident==0):
            #2 points pour accéder au tarif orange
            nb_points+=2
        if(nb_accident==1):
            #1 point pour accéder au tarif rouge
            nb_points+=1

    if (anciennete_client >= ANCIENNETE_MIN_ASSUR):
        #si le client est assuré depuis au moins 1 an il gagne un point pour avoir le tarif supérieur
        nb_points+=1

    print(tarifs[nb_points])

assurance()




