datos = read.table("../salida8.txt", header = T)
attach(datos)


t.test(datos$comision, conf.level = 0.95)
