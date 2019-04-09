datos = read.table("../salida7.txt", header = T)
attach(datos)


t.test(datos$Menor_R, conf.level = 0.95)

t.test(datos$Menor_costo_total, conf.level = 0.95)
