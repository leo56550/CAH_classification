# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:50:33 2021

@author: leobu
"""


import matplotlib.pyplot as plt


def transfo_coord_to_list(tab) :
    x =[]
    y =[]
    for valeur in tab:
        x.append(valeur[1])
        y.append(valeur[2])

    return x,y

def tracage_points(tab) : 
    
    x, y = transfo_coord_to_list(tab)
    
    plt.scatter(x,y)
    
    plt.title('Nuage de points avec Matplotlib')
    plt.xlabel('x')
    plt.ylabel('y')
    
    for i in range(0, len(tab)):
        plt.annotate(tab[i][0], (x[i], y[i]),fontsize = 15)
    
    return 
