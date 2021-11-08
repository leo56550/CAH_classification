# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:33:31 2021

@author: leobu
"""
import numpy as np
from tableau_points_t import *
from tracage_points import *
from dist import *
from dist_min import *
from mat_square_dist import * 
from mat_ward_dist import *
from barycentre import * 
from distance_ward import * 
from trouve_dist_min_in_matrice import *


#programme principal réalisant la classification CAH, non automatisé



#reglage de la précision d'affichage des float

np.set_printoptions(precision=2, suppress = True )

#question  1
#test dist : 
 
pointA = ['A',0,8]
pointB = ['B',4,6]

print("test question 1 : ",dist(pointA, pointB))
#/////////////////////////////////////////////////



#question 2
#test dist_min


print("test question 2 : La distance minimum se situe entre le couple de points", dist_min(tableau))

#/////////////////////////////////////////////////

#question 3
#affichage du tableau

tracage_points(tableau)
mat = mat_square_dist(tableau)
print("test question 3 :" , mat)
print("le point le plus proche dans maths",trouve_distmin_in_mat(mat))

# On identifie les index 0 et 2, c'est à dire les points M1 et M3,
# et sont éloignés d'une distance de 1

#///////////////////////////////////////////////

#question 4 
#création de Gamma1


gamma1 = [ tableau[0] , tableau[2] ]

print("gamma1:", gamma1)
#on définit la distance d'un ensemble à un point par 
#la distance entre ce point et le barycentre de l'ensemble
barycentre_gamma1 = barycentre(gamma1)

print("Le barycentre de gamma 1 est : ", barycentre_gamma1)



#affichage de la matrice de distance entre gamma1 et les 5 points restants

classe = []
classe.append(barycentre_gamma1)
classe.append(tableau[1])#M2
classe.append(tableau[3])#M4
classe.append(tableau[4])#M5
classe.append(tableau[5])#M6
classe.append(tableau[6])#M7
classe.append(tableau[7])#M8


print("matrice des distances euclidiennes: ")
mat = mat_square_dist(classe)
print(mat)
print(trouve_distmin_in_mat(mat))
# ce sont les index 2 et 3 dans mat qui ont la distance la plus faible(1.0)
# ce sont les points M4 et M5

#question 5 

#calcul et affichage de la matrice entre l'objet gamma1, gamma2 et les points restants
print("fusion de M4 et M5  ")
gamma2 = [ tableau[3], # M4
           tableau[4]] # M5
          

classe = []
classe.append(barycentre_gamma1)
classe.append(barycentre(gamma2))
classe.append(tableau[1])#M2
classe.append(tableau[5])#M6
classe.append(tableau[6])#M7
classe.append(tableau[7])#M8



print("Matrice entre gamma1, gamma2,M2,6,7,8 ")
mat = mat_square_dist(classe)
print(mat)
print(trouve_distmin_in_mat(mat))
# ce sont les index 3 et 4 dans mat qui ont la distance la plus faible(1.0)
# ce sont les points M6 et M7
print("fusion de M6 et M7, -> dans gamma3  ")

gamma3 = [ tableau[5], # M6
           tableau[6]] # M7
classe = []
classe.append(barycentre_gamma1)
classe.append(barycentre(gamma2))
classe.append(barycentre(gamma3))
classe.append(tableau[1])#M2
classe.append(tableau[7])#M8





print("Matrice entre gamma1, gamma2, gamma3,M5 ")
mat = mat_square_dist(classe)
print(mat)
print(trouve_distmin_in_mat(mat))
# ce sont les index 0 et 3 dans mat qui ont la distance la plus faible(1.25)
# c'est la classe gamma1 et le point M2



# On fusionne M2 dans gamma1
print("Fusion de gamma1(M1 et M3) et de M2 -> dans gamma1 ")
gamma1.append(tableau[1])#M2

classe = []
classe.append(barycentre_gamma1)
classe.append(barycentre(gamma2))
classe.append(barycentre(gamma3))
classe.append(tableau[7])#m8

print("Matrice entre gamma1, gamma2,gamma3 et M8 ")
mat = mat_square_dist(classe)
print(mat)
print(trouve_distmin_in_mat(mat))
# ce sont les index 2 et 3 dans mat qui ont la distance la plus faible(3.25)
# c'est la classe gamma3 et le point M8


# On fusionne M8 dans gamma3
print("fusion de gamma3(M6 et M7) avec M8 -> gamma3")
gamma3.append(tableau[7]) # M8
classe = []
classe.append(barycentre_gamma1)
classe.append(barycentre(gamma2))
classe.append(barycentre(gamma3))
#nous n'avons plus de points seuls

print("Matrice entre gamma1, gamma2 et gamma3 ")
mat = mat_square_dist(classe)
print(mat)
print(trouve_distmin_in_mat(mat))
# ce sont les index 0 et 1 dans mat qui ont la distance la plus faible(5.0)
# ce sont  les classes gamma1 et gamma2



# On fusionne gamma1 et gamma2 
print("fusion de gamma1 et gamma2 -> dans gamma1")
gamma1 += gamma2

classe = []
classe.append(barycentre_gamma1)
classe.append(barycentre(gamma3))

print("Matrice entre gamma1, et gamma3 ")
mat = mat_square_dist(classe)
print(mat)
print(trouve_distmin_in_mat(mat))
# ce sont les index 0 et 1 dans mat qui ont la distance la plus faible(20.7)
# ce sont  les classes gamma1 et gamma3

#on fusionne gamma1 et gamma3

gamma1 += gamma3


#On s'arrete quand il n'ya plus qu'un seul groupe.




























