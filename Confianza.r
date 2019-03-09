datos = read.table("salida6.txt", header = T)
attach(datos)


t.test(datos$tiempo_total, conf.level = 0.95)

t.test(datos$promedio_pasajeros, conf.level = 0.95)
t.test(datos$num_max, conf.level = 0.95)
#t.test(datos$X.cajero1, conf.level = 0.95)
#t.test(datos$X.cajero2, conf.level = 0.95)
#t.test(datos$X.cajero3, conf.level = 0.95)

