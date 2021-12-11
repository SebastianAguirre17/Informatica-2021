#Ejercicio 1.4. Expresar la situación que se describe a continuación, a través de asignación	sobre variables (Python 3) cuyos identificadores son dinero y paraguas:
#Bartolomé vende paraguas. Tiene 10 paraguas y $10000.
#	a) Escriba instrucciones que permitan ver en pantalla los valores iniciales de las variables dinero y paraguas.
#	b) Agregue instrucciones que describan las respectivas variaciones que resultan de la venta de 5 paraguas, 
#		a $400 cada uno (utilice variables para representar la cantidad vendida y el precio de venta), y muestre en pantalla las consecuencias de la venta.
#	c) Agregue instrucciones para representar y mostrar la venta de la mitad (entera) de paraguas restantes, con la respectiva variación de las variables dinero y paraguas.

# a)
PRECIO 		= 400
dinero 		= 10000 # en $
paraguas 	= 10
vendidas 	= 0
acumVentas 	= 0

# b)
print(f'La cantidad de paraguas es de {paraguas} y su valor es de ${dinero}')
