# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 04:23:27 2022

@author: LEVI
"""

import pandas as pd
import numpy as np


#Datos CSV
datos=pd.read_csv('Movie_Ratings.csv', header=None)
datos=datos.drop(datos.columns[[0]],axis='columns')
datos=datos.drop(0)
datos=datos.fillna(0)
datos=datos.astype(int)
datos=datos.values.tolist()
#print(datos)

##Metricas
def euclidiana(A,B):
    suma=0
    for i in range(len(A)):
        if (A[i]==0 or B[i]==0):
            suma=suma+0
        else:
            suma=(A[i]-B[i])**2+suma
    return np.sqrt(suma)


def manhattan(A,B):
    suma=0
    for i in range(len(A)):
        if (A[i]==0 or B[i]==0):
            suma=suma+0
        else:
            suma=abs(A[i]-B[i])+suma
    return suma


def coseno(A,B):
    xy=0
    x=0
    y=0
    for i in range(len(A)):
        if (A[i]==0 or B[i]==0):
            xy=xy+0
            x=x+0
            y=y+0
        else:
            xy=(A[i]*B[i])+xy
            x=A[i]**2+x
            y=B[i]**2+y
    return xy/(np.sqrt(x)*np.sqrt(y))


def pearson(A,B):
    n=len(A)
    xy=0
    x2=0
    y2=0
    x=0
    y=0
    for i in range(len(A)):
        if (A[i]==0 or B[i]==0):
            xy=xy+0
            x2=x2+0
            y2=y2+0
            x=x+0
            y=y+0
            n=n-1
        else:
            xy=(A[i]*B[i])+xy
            x2=A[i]**2+x2
            y2=B[i]**2+y2
            x=A[i]+x
            y=B[i]+y
    
    return (xy-(x*y/n))/((np.sqrt(x2-(x**2/n)))*(np.sqrt(y2-(y**2/n))))




def distancia_x(X,M,N):
    for i in range(len(M[0])):
        columna=[fila[i] for fila in M]
        d=euclidiana(X,columna)
        print(N[i],d)

def distancia_m(X,M,N):
    for i in range(len(M[0])):
        columna=[fila[i] for fila in M]
        d=manhattan(X,columna)
        print(N[i],d)

def similitud_cos(X,M,N):
    for i in range(len(M[0])):
        columna=[fila[i] for fila in M]
        d=coseno(X,columna)
        print(N[i],d)

def correlacion_pear(X,M,N):
    for i in range(len(M[0])):
        columna=[fila[i] for fila in M]
        d=pearson(X,columna)
        print(N[i],d)


Nombres=["Patrick C","Heather","Bryan","Patrick T","Thomas","aaron","vanessa","greg","brian","ben","Katherine","Jonathan","Zwe","Erin","Chris","Zak","Matt","Chris","Josh","Amy","Valerie","Gary","Stephen","Jessica","Jeff"]
Nombres2=['Angelica','Bill','Chan','Dan','Haylei','Jordyn','Sam','Veronica']


canciones=[[3.5,2,5,3,0,0,5,3],
           [2,3.5,1,4,4,4.5,2,0],
           [0,4,1,4.5,1,4,0,0],
           [4.5,0,3,0,4,5,3,5],
           [5,2,5,3,0,5,5,4],
           [1.5,3.5,1,4.5,0,4.5,4,2.5],
           [2.5,0,0,4,4,4,5,3],
           [2,3,0,2,1,4,0,0]]

Amy=[5,5,3,5,0]
Bill=[2,5,1,5,9]
x=[4,2,3,5,1]
Clara=[4.75,4.5,5,4.25,4]
Robert=[4,3,5,2,1]

x2=[3,5,4,2,1,5,5,2,3,2,4,4,4,1,5,2,3,5,2,3,1,1,4,2]

#print(coseno(Clara,Robert))
#print(pearson(Clara,Robert))

#print(euclidiana(Amy,x))


Angelica=[3.5,2,0,4.5,5,1.5,2.5,2]
Patrick=[0,4,5,4,5,4,0,0,2,4,3,3,0,0,0,5,4,4,5,4,1,3,4,0,1]

'''print('Distancia Euclidea Angelica con los demás:')
distancia_x(Angelica,canciones,Nombres2)
print()
print('Distancia Manhattan Angelica con los demás:')
distancia_m(Angelica,canciones,Nombres2)
print()
print('Correlacion Pearson Angelica con los demás:')
correlacion_pear(Angelica,canciones,Nombres2)
print()
print('Similitud coseno Angelica con los demás:')
similitud_cos(Angelica,canciones,Nombres2)
#distancia_m(punto,canciones)
#distancia_cos(punto,canciones)'''

print('Distancia Euclidea Patrick con los demás:')
distancia_x(Patrick,datos,Nombres)
print()
print('Distancia Manhattan Patrick con los demás:')
distancia_m(Patrick,datos,Nombres)
print()
print('Correlacion Pearson Patrick con los demás:')
correlacion_pear(Patrick,datos,Nombres)
print()
print('Similitud coseno Patrick con los demás:')
similitud_cos(Patrick,datos,Nombres)

        
