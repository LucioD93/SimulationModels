import random 
from math import *
import numpy as np

#Ejercicio 6.

def calculonEmb():
    nEmbTotal= [127, 162,179, 75,223,186,124,45,100,171,
       235, 176, 130, 159,117,100,92,68,242,122,
       184, 84, 240, 319, 61,78,20,141,202,213,
       204, 360, 169, 206, 326,210,335,233,102,243,
       135, 310, 138, 95, 216,99,346,220,191,230,
       219, 225, 271, 270, 110,305,157,128,163,90,
       148, 70, 40, 80,105,159,141,150,164,200,
       213, 195, 134, 141,107,177,109,48,145,114,
       400, 212, 258, 198,229,175,199,177,194,185,
       303, 335, 310, 104,374,190,211,160,138,227,
       122, 230, 97, 166,232,187,212,125,119,90,
       286, 310, 115, 277,189,159,266,170,28,141,
       155, 309, 152, 122,262,111,254,124,138,190,
       136, 110, 396, 96,86,111,81,226,50,134,
       131, 120, 112, 140,280,145,208,333,250,221,
       318, 120, 72, 166,194,87,94,170,65,190,
       359, 312, 205, 77,197,359,174,140,167,181,
       143, 99, 297, 92,246,211,275,224,171,290,
       291, 220, 239, 126,89,66,35,26,129,234,
       181, 180, 58, 40,54,123,7,319,389,121]

    nEmb= random.choice(nEmbTotal)
    return nEmb

def simulacionEstacion(nPas,num,lista,tiempoInt,tiempoDes):
    nEmb= calculonEmb()
    s= np.random.binomial(num, 0.5,nEmb)
    for i in s:
        lista.append(i)
    nPas= nPas+ nEmb
    tiempoInt = tiempoInt+ 100*(1 + 0.1*log10(nPas))

    nDes=0
    lista1=[]
    for i in lista:
        if i==1:
            lista.remove(1)
            nDes+=1
        else:
            lista1.append(i-1)
            lista.remove(i)
    tiempoDes = tiempoDes+ 20*(1 + 0.1*log10(nDes + nEmb))
    lista=lista1
    nPas=nPas-nDes
    return nPas, lista,tiempoInt,tiempoDes, nEmb

def simulate():

    for i in range(1):
        estaciones=10
        nPas=0
        num=9
        lista=[]
        tiempoInt=0
        tiempoDes=0
        listaPas=[]
        listaEmb=[]
        while num!=0:
            nPas, lista,tiempoInt,tiempoDes, nEmb= simulacionEstacion(nPas,num,lista,tiempoInt,tiempoDes)
            num=num-1
            listaPas.append(nPas)
            listaEmb.append(nEmb)

        sum=0
        for i in listaPas:
            sum=sum+i
        promedioPasajeros=sum/10


        print(tiempoInt+tiempoDes, promedioPasajeros, max(listaEmb))


if __name__ == "__main__":
    print("tiempo_total promedio_pasajeros num_max")
    for i in range(1000):
        simulate()










