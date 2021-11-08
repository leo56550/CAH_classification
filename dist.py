# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 11:14:41 2021

@author: leobu
"""



from math import *

# calculates the euclidian distance between
# 2 points ['name', x, y ]

def dist_sqr(a,b) : 
    #print("dist_sqr:" , a, b)
    return pow(a[1]-b[1],2)+pow(a[2]-b[2],2)

def dist(a,b) :
    return sqrt(dist_sqr(a, b))



    
