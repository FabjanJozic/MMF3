import numpy as np


def der_2(function, x, h):
    '''Derivacija funkcije 2. reda. 
    x : varijabla
    h : pomak
    '''
    return (function(x+h) - 2*function(x) + function(x-h))/h**2, h


def e(x):
    '''Eksponencijalna funkcija.'''
    e = np.exp(x)
    return e

