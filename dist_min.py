# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:02:31 2021

@author: leobu
"""

from dist import *
from tableau_points_t import * 



# retourne les indexs des points les plus proches dans le tableau donné
def dist_min(tab) : 
      
    point_0 = tab[0]
    point_1 = tab[1]
                                       
    distance_mini = dist(point_0,point_1)
    I=0
    J=0
    for i in range(0,len(tab)-1):
        for j in range(i+1,len(tab)-1) : 
            point_i = tab[i]
            point_j = tab[j]
            distance_ij = dist(point_i,point_j)
            if distance_ij < distance_mini :
                distance_mini = distance_ij
                I=i
                J=j
                
    return (I,J)



    
