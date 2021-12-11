#Ejercicio 1.3. Mostrar el resultado de ejecutar en el intérprete de Python 3, la siguiente
#secuencia de instrucciones; elaborar conclusiones sobre qué sucede y compartirlas:

def main():
	tanque = 1000 # Esta variable representa la cantidad de agua que hay en el tanque
	pileta = 3000 # Esta variable representa la cantidad de agua que hay en la pileta
	balde = 10 # Esta variable representa la capacidad de agua del balde
	print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros' )
	cant_baldes = 1 # Esta variable representa la cantidad de veces que cargo el balde
	print ( 'Transvasa', cant_baldes, 'baldes de agua de:', balde, 'litros' )
	tanque = tanque - cant_baldes * balde
	pileta = pileta + cant_baldes * balde
	print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros' )
	cant_baldes = cant_baldes + 1
	print ( 'Transvasa', cant_baldes, 'baldes de agua de:', balde, 'litros' )
	tanque = tanque - cant_baldes * balde
	pileta = pileta + cant_baldes * balde
	print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros' )
	cant_baldes = cant_baldes + 1
	print ( 'Transvasa', cant_baldes, 'baldes de agua de:', balde, 'litros' )
	tanque = tanque - cant_baldes * balde
	pileta = pileta + cant_baldes * balde
	print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros' )

main()