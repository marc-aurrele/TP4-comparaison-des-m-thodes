"""Ma123-TP2-FERRAZ_Marc-Aurele-MAYNARD_Mathieu-1PD2
   Methode du point fixe"""

import math
from math import *
import matplotlib.pyplot as plt


def Secante(f, x0, x1, epsilon, Nitermax):
    n = 1
    liste_des_n = []
    liste_des_x0 = []
    liste_des_erreurs = []
    liste_des_x2 = []
    while abs(x1 - x0) > epsilon and n < Nitermax:
        n = n + 1
        x2 = x0-f(x0)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
        liste_des_n.append(n)
        liste_des_x0.append(x0)
        liste_des_x2.append(x2)

    for x in liste_des_x2:
        erreur = abs(x - x0)
        liste_des_erreurs.append(erreur)
    print("liste_des_n", liste_des_n)
    print("liste_des_x0", liste_des_x0)
    print("liste_des_erreurs", liste_des_erreurs)

    plt.figure()
    plt.semilogy(liste_des_n, liste_des_erreurs)
    plt.title("évolution des erreurs")
    plt.xlabel('n') 
    plt.ylabel('erreurs') 
    plt.grid()
    plt.show()
    return x0

#fonction 0:
def f0(x):
    return 2*x - (1 + sin(x))


#fonction 1:
def f1(x):
    return x**4 + 3*x - 9

#fonction 2:
def f2(x):
    return 3*cos(x) - x - 2

#fonction 3:
def f3(x):
    return x*exp(x) - 7


#affichage des solutions:
print("="*10, "fonction 0", "="*10)
z = Secante(f0, 0, 1, 1E-10, 1E4)
print(z)

print("="*10, "fonction 1", "="*10)
a = Secante(f1, 1, 2, 1E-10, 1E4)
b = Secante(f1, -2, -1,1E-10, 1E4)
print(a)
print(b)

print("="*10, "fonction 2", "="*10)
c = Secante(f2, -2, -1, 1E-10, 1E4)
d = Secante(f2, 0, 1, 1E-10, 1E4)
print(c)
print(d)

print("="*10, "fonction 3", "="*10)
e = Secante(f3, 1, 2, 1E-10, 1E4)
print(e)
