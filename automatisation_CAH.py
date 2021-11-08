# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:34:56 2021

@author: leobu
"""

#question6 -AUTOMATISATION de la classification CAH

#//////////////////////////////////////////////////////////////

from dist_min import * 
from tableau_points_t import * 
from barycentre import *
from mat_square_dist import *
from trouve_dist_min_in_matrice import *
import numpy as np

#//////////////////////////////////////////////////////////////


#reglage de la précision d'affichage des float
np.set_printoptions(precision=2, suppress = True )


# Chaque élément est seul est isolé dans son groupe
#création de la liste des groupes de points, chaques points est dans soon groupe
groups = []
for i in range(0, len(tableau)) : 
    groups.append([tableau[i].copy()])
    
print("Groupes initiaux:", groups)

def fusion_groupe(groupe1,groupe2) :
    print("fusion de ", groupe1 , " et ", groupe2)
    len2 = len(groupe2)
    for i in range(0,len2):
        groupe1.append(groupe2[i])
        
    groupe2.clear()
    

def classification_CAH(group) :
    
    while True:
        # recherche des 2 groupes les plus proches
        mat = mat_square_dist_2(group)
        I,J,distmin = trouve_distmin_in_mat(mat)
        print("I:", I, " J:", J, " min ", distmin)
        
        # fusion des groupes
        fusion_groupe(group[I],group[J])
        del group[J]
        
        print("Groupe après fusion:", group)
        
        if len(group) == 1:
            break
        
        
classification_CAH(groups)
        
        




