# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 15:29:19 2021

@author: leobu
"""

import numpy as np
from dist import *
from tableau_points_t import *
from barycentre import *


#fonction retournat la matrice des distances eucliidiennes au carré de chaques points du tableau donné
def mat_square_dist(tab) : 
    mat = np.empty((len(tab),len(tab)))
    
    
    for i in range(0,len(tab)-1):
        for j in range(i+1,len(tab)) : 
            point_i = tab[i]
            point_j = tab[j]
            distance_carre_ij = dist_sqr(point_i,point_j)
            mat[i,j] = distance_carre_ij
            mat[j,i] = distance_carre_ij
   
    return mat

#cette version accepte des groupes de points dans les entrées du tableau
def mat_square_dist_2(tab) :

  mat = np.empty((len(tab),len(tab)))
    
    
  for i in range(0,len(tab)-1):
      for j in range(i+1,len(tab)) : 
         point_i = barycentre(tab[i])
         point_j = barycentre(tab[j])
         distance_carre_ij = dist_sqr(point_i,point_j)
         mat[i,j] = distance_carre_ij
         mat[j,i] = distance_carre_ij
   
  return mat





