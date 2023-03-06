print("")
print("Bienvenido ingeniero. Esta es la resolución de la actividad asincrona correspondiente a la semana 6")
print("")

print("---------------------------------------------------------------------------------------------------------------------")
print("")
print("Sumar 3 variables distintas y asignar el valor a una cuarta variable.")

suma1 = 8
suma2 = 5
suma3 = 2

suma = suma1 + suma2 + suma3
suma4 = suma

print("")
print(f"El resultado de sumar: {suma1} + {suma2} + {suma3} \nes: {suma4}")
print("")

print("---------------------------------------------------------------------------------------------------------------------")
print("")
print("Restar 4 variables siendo en la tercera variable más alta que la primera.")

resta1 = 3
resta2 = 9
resta3 = 6
resta4 = 10

resta = resta1 - resta2 - resta3 - resta4

print("")
print(f"El resultado de restar: {resta1} - {resta2} - {resta3} - {resta4} \nes: {resta}")
print("")

print("---------------------------------------------------------------------------------------------------------------------")
print("")
print("Multiplicar 2 variables asignarlas a otra variable y esa variable multiplicar por la segunda variable de suma y resta.")

multiplicacion1 = 9
multiplicacion2 = 5

primeraMultiplicacion = multiplicacion1 * multiplicacion2
multiplicacion3 = primeraMultiplicacion

print("")
print(f"El resultado de multiplicar: {multiplicacion1} * {multiplicacion2} \nes: {multiplicacion3}")
print("")

segundaMultiplicacion = multiplicacion3 * (suma2 * resta2)

print(f"El resultado de multiplicar la segunda variable de la suma y la resta: {suma2} * {resta2} \npor el resultado de la primera multiplicación: {multiplicacion3} \nes: {segundaMultiplicacion}")
print("")

print("---------------------------------------------------------------------------------------------------------------------")
print("")
print("Sacar a la primera variable de la multiplicación el exponente de la segunda variable de la multiplicación.")

exponente = multiplicacion1 ** multiplicacion2

print("")
print(f"El resultado de sacar el exponente de la primera y segunda variable de la multiplicación: {multiplicacion1} ** {multiplicacion2} \nes: {exponente}")
print("")

print("---------------------------------------------------------------------------------------------------------------------")
print("")
print("Sacar el módulo de la primera variable de la suma con la primera variable de la resta.")

modulo = suma1 % resta1
 
print("")
print(f"El resultado de sacar el modulo de la primera variable de la suma y la resta: {suma1} % {resta1} \nes: {modulo}")
print("")

print("---------------------------------------------------------------------------------------------------------------------")
print("")
print("Dividir la variable resultado del exponente entre la variable resultado del módulo.")

division = exponente / modulo

print("")
print(f"El resultado de dividir la respuesta del exponente entre el resultado del modulo: {exponente} / {modulo} \nes: {division}")
print("")

print("---------------------------------------------------------------------------------------------------------------------")
print("")
print("Realizar la división entera de la división normal.")

divisionEntera = exponente // modulo

print("")
print(f"El resultado de la división entera de la anterior división es: {divisionEntera}")
print("")

print("---------------------------------------------------------------------------------------------------------------------")
