""" @auteur : johanna
date : 10/09/2020
description : atelier3 exercice 2
version 1
"""

#exercice 5

def present(L,e):
    if e in L:
        return(True)
    else:
        return(False)

def test_present(present:callable):
    liste_vide=[]
    liste=[2,5,8,4,6,9,456,1,3]
    test_debut=2
    test_fin=3
    test_milieu=6
    test_pas_present=999
    msg_succes = " succès"
    msg_echec = " echec"
    e=5

    if not(present(liste_vide,e)):
        msg= msg_succes
    else:
        msg =msg_echec

    if present(liste, test_fin):
        msg += msg_succes +" test_fin "
    else:
        msg += msg_echec + " test_fin "

    if present(liste, test_debut):
        msg += msg_succes + " test_debut "
    else:
        msg += msg_echec + " test_debut"

    if present(liste, test_milieu ):
        msg += msg_succes + " test_milieu "
    else:
        msg += msg_echec + " test_milieu "

    if not present(liste,test_pas_present):
        msg += msg_succes + " test_pas_present "
    else:
        msg += msg_echec + " test_pas_present "
    return msg


def present1 (L,e):
    for i in range(0,len(L)):
        if(L[i]==e):
            return(True)
    else:
         return(False)

def present2(L,e):
    b= False
    for i in range(0,len(L)):
        if(L[i]==e):
            b=True
    return(b)

def present3(L,e):
    b=False
    for i in range(0,len(L)):
        if (L[i] == e):
            b = True
    return (b)


def present4(L,e):
    b= False
    i=0
    while(i<len(L)):
        if(L[i]==e):
            b=True
        i+=1
    return(b)
print(test_present(present))
print(test_present(present1))
print(test_present(present2))
print(test_present(present3))
print(test_present(present4))


def test_pos(pos:callable):
    liste=[2,3,1,2,2,3]
    test_1 = pos(liste,1)
    test_2 = pos(liste,2)
    test_3 = pos(liste,3)
    msg_succes = "succès"
    msg_echec = " echec"
    msg=""

    liste_1=[0,3,4]
    liste_2=[1,5]

    print(test_1)
    print(test_2)
    print(test_3)
    if len(test_1)==1 :
        if test_1[0]==2:
            msg+=msg_succes + "test 1"
        else:
            msg+= msg_echec + "bon_numéro test 1"
    else:
        msg += msg_echec + "mauvaise taille test 1"

    if len(test_2)==3 :
        estOk = True
        for i in range(0,len(test_2)):
            for j in range(0,len(liste_1)):
                if test_2[i]!=liste_1[i] :
                    estOk = False
        if (estOk):
            msg += msg_succes + "test 2"
        else:
            msg+= msg_echec + "bon_numéro test 2"
    else:
        msg += msg_echec + "mauvaise taille test 2"




    return(msg)


def pos1(L,e):
    Lres= []
    for i in range(0,len(L)):
        if L[i]==e:
            Lres.append(i)
    return Lres

def pos3(L,e):
    Lres= []
    for i in range(0,len(L),1):
        if L[i]==e:
            Lres.append(i)
    return Lres

def pos2(L,e):
    Lres= []
    for i in range(0,len(L)):
        if(L[i]==e):
            Lres.append(i)
    return Lres

def pos4(L,e):
    nb= L.count(e)
    Lres = [0]*nb
    j=0
    for i in range(0,len(L)):
        if(L[i]==e):
            Lres[j]=i
            j+=1
    return Lres

print(test_pos(pos1))
print(test_pos(pos2))
print(test_pos(pos3))
print(test_pos(pos4))