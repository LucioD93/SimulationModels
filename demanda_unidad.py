from random import randrange

#Ejercicio 7.

def simulacion_diaria(unidades_listas,unidades_espera, lista):
    p1 = randrange(0, 100)
    if p1<=5:
        demanda_diaria=12
    elif 5<p1<=20:
        demanda_diaria=13
    elif 20<p1<=45:
        demanda_diaria=14
    elif 45<p1<=80:
        demanda_diaria=15
    elif 80<p1<=95:
        demanda_diaria=16
    else:
        demanda_diaria=17
    #print (demanda_diaria)

    p2 = randrange(0, 100)
    q=100
    if p2<=20:
        tiempo_entrega=1
    elif 20<p2<=50:
        tiempo_entrega=2
    elif 50<p2<=85:
        tiempo_entrega=3
    else:
        tiempo_entrega=4
    #print (tiempo_entrega)

    lista1=[]
    # Lista que maneja la llegada de los pedidos por dias.
    for i in lista:
        aux=i[0]
        if i[1]==1:
            unidades_listas=unidades_listas+aux
            lista.remove((aux,1))
        elif i[1]==2:
            lista.remove((aux,2))
            lista1.append((aux,1))
        elif i[1]==3:
            lista.remove((aux,3))
            lista1.append((aux,2))
        else:
            lista.remove((aux,4))
            lista1.append((aux,3))
    
    lista=lista1

    lista.append((q,tiempo_entrega))
   
    # Si las unidades listas es menor a la demanda diaria se agrega a las unidades en espera la diferencia.
    if unidades_listas<demanda_diaria:
        unidades_espera= unidades_espera + demanda_diaria-unidades_listas
    else: #Si es mayor o igual se entrega el pedido y no se guarda en almacenamiento.
        unidades_listas=unidades_listas-demanda_diaria
    
    if unidades_listas<unidades_espera:
        unidades_espera=unidades_espera-unidades_listas
        unidades_listas=0
    else:
        unidades_listas=unidades_listas - unidades_espera
        unidades_espera=0
    
    #El costo de inventario se estima en 0.20 dólares por unidad por día, y se carga a las unidades en inventario al final del día.
    costo_inventario=0.2*unidades_listas

    #La escasez cuesta 1 dólar por cada unidad que falte.
    costo_escasez=1*unidades_espera
    
    #El costo de pedido es 10 dólares por pedido. Los pedidos llegan al inicio del día.
    costo_pedido=10*q

    #Costo_variable=costo_almacenamiento, el costo_pedido y el costo_escasez.
    costo_variable=costo_inventario+costo_escasez+costo_pedido

    return unidades_listas, unidades_espera, lista, costo_variable

if __name__ == "__main__":

    menordef=10000000000000000000000000000000000
    preciodef=1000000000000000000000000000000000
    print( "Menor R, Menor costo total")

    for i in range(15):
        for i in range(1):
            inicio=0
            unidades_listas=0
            unidades_espera=0
            lista=[]
            precio=1000000000000000000000000000000000000000000000000000000000000000000000000
            while inicio!=30: #Simular un mes.
                unidades_listas, unidades_espera, lista, costo= simulacion_diaria(unidades_listas, unidades_espera, lista)
                if costo<precio:
                    precio=costo
                    menorR=unidades_listas
                inicio+=1
            
            if precio<preciodef:
                menordef=menorR
                preciodef=precio
    
        print (menordef, preciodef)
    
