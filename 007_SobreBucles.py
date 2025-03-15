##Bucle infinito

##while True:
#    print("Estoy atrapado en un bucle infinito")


##Bucle while simple

while numero:=int(input("Escribe un numero: "))!=0:
    if numero%2==0:
        print("El numero es par")

    else: 
        print("El numero es impar")


    
#While con contador

contador=10

while contador>0:
    print("El contador está en: ", contador)
    contador -=1

print("El contador ha llegado a: ", contador)


"""
Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

pedirá al usuario que ingrese un número entero;
utilizará un bucle while;
comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto
del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. 
Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla,
y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."
¡El mago está contando contigo! No lo decepciones."
"""

numero_secreto=777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero=int(input("Adivina el numero: "))

while numero!=numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero=int(input("Adivina el numero: "))

print("¡Bien hecho, muggle! Eres libre ahora.") ##El bucle termina una vez que el numero ingresado es igual al numero secreto

##Bucle for

numero=1

for expo in range(16):
    print("2 elevado a la ", expo, "es igual a: ", numero)
    numero*=2


#Conteo de mississippis

import time

for i in range (5):
    print (i+1,"mississippi")
    time.sleep(1)

print("¡Listo o no, aquí vengo!")

##time.sleep(1) hace que la función se detenga un segundo antes del siguiente bucle, para usar esta funcion es necesario
# importar la libreria time

"""
Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como
la palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.
No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la sentencia break."
"""

while True:
    palabra=(input("Escribe un palabra para salir del bucle: "))

    if palabra=="chupacabra":
        break

print("Haz dejado el bucle con éxito")

"""""
pedir al usuario que ingrese una palabra.
utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados
métodos de cadena y el método upper() muy pronto, no te preocupes
utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada"

"""

userword=input("Escribe una palabra: ")
userword=userword.upper()


for letra in userword: 
    if letra=="A":
        continue
    elif letra=="E":
        continue
    elif letra=="I":
        continue
    elif letra=="O":
        continue
    elif letra=="U":
        continue

    print(letra)

""" "
Tu programa debe:

pedir al usuario que ingrese una palabra.
utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; 
emplea la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A , E , I , O , U de la palabra ingresada.
asigna las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla."
"""

word_without_vowels=""
userword=input("Escribe una palabra: ")
userword=userword.upper()

for letra in userword:
    if letra=="A":
        continue
    elif letra=="E":
        continue
    elif letra=="I":
        continue
    elif letra=="O":
        continue
    elif letra=="U":
        continue
    else:
        word_without_vowels+=letra

print(word_without_vowels)

""""
Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se
puede construir utilizando estos bloques.
Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden
completar la siguiente capa, terminan su trabajo inmediatamente."
"""

bloques=(int(input("Escribe el numero de bloques: ")))

altura=0
capa=1

while bloques>=capa:
    altura+=1
    bloques-=capa
    capa+=1
    
else:
    print("La altura de la piramide es: ", altura)
        
""" "
toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
si es par, evalúa un nuevo c0 como c0 ÷ 2;
de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
si c0 ≠ 1, salta al punto 2."
"""

c0=int(input("Escribe un numero: "))
pasos=0

if c0>0:
    while c0!=1:
        if c0%2==0:
            c0/=2
            pasos+=1
            print(c0)
        else:
            c0=3*c0+1
            pasos+=1
            print(c0)

    print("El numero de pasos fue: ", pasos)

    


else: 
    print("El numero debe ser positivo y diferente de 0")
