# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:35:22 2021

@author: leobu
"""

from dist import * 
from barycentre import * 

#fonction retourant la distane de ward entre deux classes
def distance_ward(classe1,classe2) : 
   n1 = len(classe1)
   n2 = len(classe2)
   b1 = barycentre(classe1)
   b2 = barycentre(classe2)
   distance = ((n1)*(n2))/(n1+n2)*dist_sqr(b1, b2)
   return distance
    

