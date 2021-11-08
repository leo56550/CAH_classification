# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:36:15 2021

@author: leobu
"""

def trouve_distmin_in_mat(matrice):
    I = -1
    J = -1
    distance_min = float('inf')
    for i in range(0,len(matrice)) : 
        for j in range(i+1,len(matrice)) : 
            if distance_min > matrice[i,j]:
                distance_min = matrice[i,j]
                I = i
                J = j
                
    
    return I,J,distance_min