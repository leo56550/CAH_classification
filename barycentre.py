# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:05:58 2021

@author: leobu
"""

import matplotlib.pyplot as plt
from  tableau_points_t import *


#fonction retourant le barycentre de n points
def barycentre(tab):
    barycentre = ['',0,0]
  
    for i in range(0,len(tab)):
        point_i = tab[i]
        barycentre[1] += point_i[1]
        barycentre[2] += point_i[2]
        
    barycentre[1] /= len(tab)
    barycentre[2] /= len(tab)
       
    
    return barycentre





