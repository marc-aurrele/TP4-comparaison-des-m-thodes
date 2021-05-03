"""Ma123-TP2-FERRAZ_Marc-Aurele-MAYNARD_Mathieu-1PD2
   Methode du point fixe"""

import math
from math import * 
import matplotlib.pyplot as plt

def Newton(f, fder, x0, epsilon, Nitermax):
    n = 1
    liste_des_n = []
    liste_des_xold = []
    liste_des_erreurs = []
    xold = x0
    xnew = xold - ((f(xold))/fder(xold))
    erreur = xnew - xold
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = xold - ((f(xold))/fder(xold))
        n = n +1
        erreur = xnew - xold
        erreur_sur_le_calcul = abs(xold - xnew)
        xold = xnew
        print("xnew =",xnew, "n =", n, "xnew - xold =", xnew-xold)
        liste_des_n.append(n)
        liste_des_xold.append(xold)
        liste_des_erreurs.append(erreur_sur_le_calcul)
    plt.plot(liste_des_n, liste_des_erreurs)
    plt.title("évolution des erreurs")
    plt.xlabel('n') 
    plt.ylabel('erreurs') 
    plt.grid()
    plt.show()
    return xnew


#définition des fonctions:
#fonction 0:
def f0(x):
    return 2*x - (1 + sin(x))
def f0der(x):
    return 2 - cos(x)

#fonction 1:
def f1(x):
    return x**4 +3*x - 9

def f1der(x):
    return 4*x**3 + 3

#fonction 2:
def f2(x):
    return 3*cos(x) - x - 2

def f2der(x):
    return -3*sin(x) -1

#fonction 3:
def f3(x):
    return x*exp(x) - 7

def f3der(x):
    return exp(x) + x*exp(x)

#fonction 4:
def f4(x):
    return exp(x) - x -10

def f4der(x):
    return exp(x) - 1

#fonction 5:
def f5(x):
    return 2*tan(x) - x - 5

def f5der(x):
    return (2/cos(x)**2) -1

#fonction 6:
def f6(x):
    return exp(x) - x**2 -3

def f6der(x):
    return exp(x) -2*x

#fonction 7:
def f7(x):
    return 3*x + 4*log(x) - 7

def f7der(x):
    return 3 + (4/x)

#fonction 8:
def f8(x):
    return x**4 - 2*x**2 -4*x - 17

def f8der(x):
    return 4*x**3 - 4*x +4

#fonction 9:
def f9(x):
    return exp(x) - 2*sin(x) - 7

def f9der(x):
    return exp(x) -2*cos(x)

#fonction 10:
def f10(x):
    return log(x**2 + 4)*exp(x) - 10

def f10der(x):
    return (2*x/(x**2 + 4))*exp(x) + log(x**2 + 4)*exp(x)

#affichage des solutions:
print("========fonction 0========")
z = Newton(f0, f0der, 0, 1E-10, 1E4)
print("les solutions de l'équation sont:", z)

print("========fonction 1========")
a = Newton(f1, f1der, -2, 1E-10, 1E4)
b = Newton(f1, f1der, 0, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a, ";", b)

print("========fonction 2========")
a = Newton(f2, f2der, -5, 1E-10, 1E4)
b = Newton(f2, f2der, -2, 1E-10, 1E4)
c = Newton(f2, f2der, 1, 1E-10, 1E4) 
print("les solutions de l'équation sont: ", a, ";", b, ";", c)

print("========fonction 3========")
a = Newton(f3, f3der, 2, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a)

print("========fonction 4========")
a = Newton(f4, f4der, -10, 1E-10, 1E4)
b = Newton(f4, f4der, 3, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a, ";", b)

print("========fonction 5========")
a = Newton(f5, f5der, -2, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a)

print("========fonction 6========")
a = Newton(f6, f6der, 2, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a)

print("========fonction 7========")
a = Newton(f7, f7der, 2, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a)

print("========fonction 8========")
a = Newton(f8, f8der, -3, 1E-10, 1E4)
b = Newton(f8, f8der, 3, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a, ";", b)

print("========fonction 9========")
a = Newton(f9, f9der, 3, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a)

print("========fonction 10========")
a = Newton(f10, f10der, 2, 1E-10, 1E4)
print("les solutions de l'équation sont: ", a)