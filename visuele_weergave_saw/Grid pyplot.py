# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 18:44:42 2022

@author: ahpva
"""

import matplotlib.pyplot as plt
import numpy as np

def saw_graphic_square(moves):
    """Functie die van gegeven string zetten in een vierkant grid een
    visuele weergave maakt."""
    # Bepaling hoogte en breedte beeld
    lengte_moves = len(moves)
    hoogte = breedte = 2*lengte_moves
    plt.rcParams["figure.figsize"] = (hoogte,breedte)
    
    # Verwerking data punten
    x_range = np.arange(0,breedte+1,1)
    y_range = np.arange(0,breedte+1,1)
    data = np.array([[x,y] for x in x_range for y in y_range])
    plt.yticks(y_range)
    plt.scatter(data[:, 0], data[:, 1],linewidths=6)
    
    # Markering middenpunt
    middenpunt = lengte_moves,lengte_moves
    plt.scatter(middenpunt[0], middenpunt[1], color = 'r',linewidths=6)
    plt.show()


if __name__ == "__main__":
    saw_graphic_square('huts')
