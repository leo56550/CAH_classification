# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 22:36:11 2021

@author: leobu
"""


from dist import *
from distance_ward import *
import numpy as np



#fonction affichant la matrice des distances de ward entre chaque points du tableau donné
def mat_war_dist(tab) :
    
    taille_mat = len(tab)
    mat = np.empty((taille_mat , taille_mat))
    
    
    print("taille mat:" , taille_mat)
    
    for i in range(0,len(tab)):
        for j in range(i+1,len(tab)) : 
            point_i = tab[i]
            point_j = tab[j]
            distance_ward_ij = distance_ward([point_i], [point_j])
            mat[i,j] = distance_ward_ij
            mat[j,i] = distance_ward_ij
   
    return mat
