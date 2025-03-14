##Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas 
# que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True if n es mayor o igual que 100.
#No debes crear ningún bloque if

n=int(input("ingrese cualquier numero: "))
print(n>=100) ## si el numero es mayor o igual a 100, imprime True, si no, imprime False


#Comparador de numeros
numero_1=int(input("Escribe el primer numero: "))
numero_2=int(input("Escribe el segundo numero: "))
numero_3=int(input("Escribe el tercer numero: "))

ngrande=numero_1 #Se supone que el primer numero es el mas grande

if numero_1<numero_2:
    ngrande=numero_2
    
if ngrande<numero_3:
    ngrande=numero_3
    
print("El numero más grande es: ", ngrande)

##Funcion Max y Min
mnumero_1=int(input("Escribe el primer numero: "))
mnumero_2=int(input("Escribe el primer numero: "))
mnumero_3=int(input("Escribe el primer numero: "))

print("El numero más grande es: ", max(mnumero_1,mnumero_2,mnumero_3)) ##max es una funcion que devuelve el numero mas grande
print("El numero más pequeño es: ", min(mnumero_1,mnumero_2,mnumero_3)) ##min es una funcion que devuelve el numero mas pequeño

# ##Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que
#  filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.
# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo,
# grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"
# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

# imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
# imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
# imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.


planta=input("Escribe el nombre de una planta: ")

if planta=="ESPATIFILIO":
    print("¡El Espatifilo! es la mejor planta de todos los tiempos!")

elif planta=="espatifilo":
    print("No, ¡quiero un gran Espatifilo!")

else:
    print("¡Espatifilo!, ¡No",planta,"!")

##si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
##si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
##Debe aceptar un valor de punto flotante: el ingreso.
##A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales

ingreso=float(input("Ingrese su ingreso anual: "))

if ingreso <= 85528:
    impuesto=ingreso*0.18-556.02

else:
    impuesto=14839.02+(ingreso-85528)*0.32

if impuesto<0:
    impuesto=0


impuesto=round(impuesto,0)
print("Su impuesto a pagar es: ",impuesto,"pesos")

##Año bisiesto o normal respecto al calendario Gregoriano

año=int(input("Ingrese un año: "))

if año<1582:
    print("El año no esta dentro del calendario Gregoriano")
elif año%4!=0:                                                    ##Se usa el reisduo para saber si es completamente divisible o no entre 4. Si el residuo es 0, es divisible.
    print("El año no es bisiesto")
elif año%100!=0:
    print("El año es bisiesto")
elif año%400!=0:
    print("El año no es bisiesto")
else:                                               ##En caso de no caer en las demás reglas, el año será obligatoriamnete bisiesto
    print("El año es bisiesto")

