# Ejercicio  2.3.Ídem anterior: Escribir  un programa  que solicite diez valores expresados en grados  Fahrenheit 
# y  los muestre convertidosa  grados  Celsius.  Considereque la  fórmula  para conversión de grados Celsius a grados 
# Fahrenheit es:F = 9/ 5  x C+  32

def CelciusToFahrenheit(celcius):
    return 9 / 5 * celcius + 32

def FahrenheitToCelcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 


print(FahrenheitToCelcius(32))
print(CelciusToFahrenheit(15))

for i in range (10):
    c = int(input("Ingrese un valor expresado en ºC: "))
    print(f"{c} ºC equivalen a {CelciusToFahrenheit(c)}")

