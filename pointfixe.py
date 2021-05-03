"""Ma123-TP2-FERRAZ_Marc-Aurele-MAYNARD_Mathieu-1PD2
   Methode du point fixe"""

import math
from math import *
import matplotlib.pyplot as plt

def PointFixe(g, x0, epsilon, Nitermax):
    n = 1
    xold = x0
    xnew = g(xold)
    erreur = xnew - xold
    liste_des_n = []
    liste_des_xold = []
    liste_des_erreurs = []
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = g(xold)
        n = n +1
        erreur = xnew - xold
        erreur_sur_le_calcul = abs(xold - xnew)
        xold = xnew
        print("xnew =",xnew, "n =", n, "xnew - xold =", xnew-xold)
        liste_des_n.append(n)
        liste_des_xold.append(xold)
        liste_des_erreurs.append(erreur_sur_le_calcul)
    plt.semilogy(liste_des_n, liste_des_erreurs)
    plt.title("évolution des erreurs")
    plt.xlabel('n') 
    plt.ylabel('erreurs') 
    plt.grid()
    plt.show()

    return xnew

#fonction 0:

def g0(x):
    return (1+ sin(x))/2

#fonction 1:

def g1plus(x):
    return(9-3*x)**0.25 

def g1neg(x):
    return -(9-3*x)**0.25

#fonction 2:

def g2plus(x):
    return acos((2+x)/3)

def g2neg(x):
    return -(acos((2+x)/3))

print("="*10)

#fonction 3:

def g3(x):
    return log(7/x)

#Fonction 4:

def g4neg(x):
    return (exp(x)-10)

def g4plus(x):
    return log(10+x)

#Fonction 5:

def g5(x):
    return  atan(((x+5)/2))

#Fonction 6:

def g6(x):
    return log((x**2.0)+3)


#Fonction 7:

def g7(x):
    return (7-4*log(x))/3

#Fonction 8:

def g8plus(x):
    return ((2*(x**2)-(4*x)+17)**0.25)


def g8neg(x):
    return -((2*(x**2)-(4*x)+17)**0.25)

#Fonction 9:

def g9(x):
    return log(2*sin(x)+7)

#Fonction 10:

def g10(x):
    return log(10)-log(log(x**2+4))


#affichage des solutions:

print("========fonction 0========")
z = PointFixe(g0, 0, 1E-10, 1E4)

print("========fonction 1========")
aplus = PointFixe(g1plus,0,1E-10,1E4)
aneg = PointFixe(g1neg,0,1E-10,1E4)
print("les solutions de l'équation sont:")
print(aplus)
print(aneg)

print("========fonction 2========")
bplus= PointFixe(g2plus,0,1E-10,1E4)
bneg= PointFixe(g2neg,0,1E-10,1E4)
print("les solutions de l'équation sont:")
print(bneg)
print(bplus)

print("========fonction 3========")
c= PointFixe(g3,1,1E-10,1E4)
print("les solutions de l'équation sont:")
print(c)

print("========fonction 4========")
dneg= PointFixe(g4neg,1,1E-10,1E4)
dplus= PointFixe(g4plus,1,1E-10,1E4)
print("les solutions de l'équation sont:")
print(dplus)
print(dneg)

print("========fonction 5========")
e=PointFixe(g5,0,1E-10,1E4)
print("les solutions de l'équation sont:")
print(e)

print("========fonction 6========")
f=PointFixe(g6,0,1E-10,1E4)
print("les solutions de l'équation sont:")
print(f)

print("========fonction 7========")
g=PointFixe(g7,1,1E-10,1E4)
print("les solutions de l'équation sont:")
print(g)

print("========fonction 8========")
hplus=PointFixe(g8plus,0,1E-10,1E4)

hneg=PointFixe(g8neg,0,1E-10,1E4)
print("les solutions de l'équation sont:")
print(hneg) 
print(hplus)

print("========fonction 9========")
i=PointFixe(g9,0,1E-10,1E4)
print("les solutions de l'équation sont:")
print(i)

print("========fonction 10========")
j=PointFixe(g10,0,1E-10,1E4)
print("les solutions de l'équation sont:")
print(j)