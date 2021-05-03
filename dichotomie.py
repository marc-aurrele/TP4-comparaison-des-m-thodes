"""Ma123-TP2-FERRAZ_Marc-Aurele-MAYNARD_Mathieu-1PD2
   Methode du point fixe"""

import math
from math import *
import matplotlib.pyplot as plt

def Dichotomie(f, a0, b0, epsilon, Nitermax):
    n = 1
    liste_des_n = []
    liste_des_m = []
    liste_des_erreurs = []
    while abs(b0 - a0) > epsilon and n < Nitermax:
        n = n + 1
        m = (a0 + b0)/2
        if f(a0) * f(m) <= 0:
            b0 = m
        else:
            a0 = m
        print("n = ", n)
        erreur = abs((b0 - a0)/2**(n +1))
        liste_des_n.append(n)
        liste_des_m.append(m)
        liste_des_erreurs.append(erreur)
    plt.semilogy(liste_des_n, liste_des_erreurs)
    plt.title("évolution des erreurs")
    plt.xlabel('n') 
    plt.ylabel('erreurs') 
    plt.grid()
    plt.show()
    return m

#fonction 0:
def f0(x):
    return 2*x - (1 + sin(x))

#fonction 1:
def f1(x):
    return x**4 +3*x - 9

#fonction 2:
def f2(x):
    return 3*cos(x) - x - 2

#fonction 3:
def f3(x):
    return x*exp(x) - 7

#affichage des solutions:

print("="*10, "fonction 0", "="*10)
z = Dichotomie(f0, 0, 1, 1E-10, 1E4)
print(z)

print("="*10, "fonction 1", "="*10)
a = Dichotomie(f1, 1, 2, 1E-10, 1E4)
b = Dichotomie(f1, -2, -1,1E-10, 1E4)
print(a)
print(b)

print("="*10, "fonction 2", "="*10)
c = Dichotomie(f2, -2, -1, 1E-10, 1E4)
d = Dichotomie(f2, 0, 1, 1E-10, 1E4)
print(c)
print(d)

print("="*10, "fonction 3", "="*10)
e = Dichotomie(f3, 1, 2, 1E-10, 1E4)
print(e)