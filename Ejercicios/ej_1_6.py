# Ejercicio 1.6. Mostrar el resultado de ejecutar en el intérprete de Python 3, los siguientes
# bloques de código; comparar y obtener conclusiones sobre qué sucede en cada caso:

for i in range ( 6 ):
    #print ("el valor del cuadrado de", i , "es ==>", i * i)
    print (f"el valor del cuadrado de {i} es ==> {i * i}")

print("*******************************************************")

for j in range (1, 6):
    print (j ,"dividido 3" )
    print ("división:", j / 3, " división entera:" , j // 3 , " resto:", j % 3 )

print("*******************************************************")

desde = 0
hasta = 6
salto = 2
for i in range (desde, hasta, salto):
    print ("la potencia", i , "de dos es:", 2 ** i )

print("*******************************************************")

for elem in [ 1, 2, 4, 3, 5, 6 ]:
    print(elem)