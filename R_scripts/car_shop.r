datos = read.table("../salida9.txt", header = T)
attach(datos)


t.test(datos$nro_de_trabajos, conf.level = 0.95)

t.test(datos$tiempo_a_esperando, conf.level = 0.95)
t.test(datos$tiempo_de_terminacion, conf.level = 0.95)

