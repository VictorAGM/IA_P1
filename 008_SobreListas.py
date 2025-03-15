

numeros=[1,2,3,4,5]

#Imprime el contenido de la lista
print("El contenido de la lista es: ", numeros)

#Copiar datos e imprimir el estado actual de la lista
numeros[0]=numeros[1]
print("\n El nuevo contenido de la lista es: ", numeros)

numeros[4]=numeros[3]
print("\n El nuevo contenido de la lista es: ", numeros)

#Cantidad de datos en la lista
print("\n La cantidad de datos en la lista es: ", len(numeros))

#Borrar datos de la lista

del numeros[0]
print("\n El nuevo contenido de la lista es: ", numeros)

#Uso de indices negativos
print("\n El ultimo numero de la lista es ", numeros[-1])
print("\n El penultimo numero de la lista es ", numeros[-2])

##EJERCICIO
"""
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.
escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado
por el usuario (Paso 1)
escribir una línea de código que elimine el último elemento de la lista (Paso 2)
escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
"""

sombrero=[1,2,3,4,5]

sombrero[2]=int(input("Escribe el valor que deseas en lugar del 3: "))

del sombrero[-1]
print(sombrero)
print("La longitud de la lista es: ", len(sombrero))

##Usando append e insert
numeros.append(6)   ##Agrega un numero al final de la lista
print(numeros)

numeros.insert(0,1) ##Agrega un numero en la posicion 0
print(numeros)

##Intercambiar datos en la lista

numeros[0],numeros[1]=numeros[1],numeros[0]
print(numeros)

#Haciendolo con for
length=len(numeros)

for i in range (length//2):
    numeros[i],numeros[length-1-i]=numeros[length-1-i],numeros[i]
print(numeros)

##Ejercicio
""""
"Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:
paso 1: crea una lista vacía llamada beatles;
paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista:
 John Lennon, Paul McCartney y George Harrison;
paso 3: emplea el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: 
Stu Sutcliffe, y Pete Best;
paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista."
"""

beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    beatles.append(input("Escribe el nombre de un miembro de los Beatles: "))
    
print(beatles)
del beatles[-1]
print(beatles)
del beatles[-1]
print(beatles)
beatles.insert(0,"Ringo Starr")

##Ordenar una lista
numeros=[]

ndatos=int(input("Cuantos datos deseas ingresar: "))

for i in range(ndatos):
    numeros.append(int(input("Escribe un numero: ")))

numeros.sort()

print(numeros)