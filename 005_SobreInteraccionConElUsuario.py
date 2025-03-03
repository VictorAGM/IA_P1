# Practica sobre el funcionamiento de input en Python

# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor, ingresa tu nombre: ")

# Solicitar al usuario que ingrese su edad
edad = input("Por favor, ingresa tu edad: ")

# Convertir la edad a un entero
edad = int(edad)

# Mostrar un mensaje personalizado utilizando los datos ingresados
print(f"Hola {nombre}, tienes {edad} años.")


# Dibujar con la replicación
print("Esto es un cuadrado")
print("+"+10*"-"+"+")
print(("|"+" "*10+"|\n")*5,end="")
print("+"+10*"-"+"+")

#Entradas y salidas simples
flotante_a=float(input("Ingresa el valor\"a\" aquí"))# ingresa un valor flotante para la variable a aquí
flotante_b=float(input("Ingresa el valor\"a\" aquí"))# ingresa un valor flotante para la variable b aquí

print("La suma de ambos valores sera:" + str(flotante_a+flotante_b))# mostrar el resultado de la suma aquí
print("La resta de ambos valores sera:" + str (flotante_a-flotante_b))# mostrar el resultado de la resta aquí
print("La resta de ambos valores sera:" + str (flotante_a*flotante_b))# mostrar el resultado de la multiplicación aquí
print("La resta de ambos valores sera:" + str (flotante_a/flotante_b))# mostrar el resultado de la división aquí

print("\n¡Eso es todo, amigos!")

#Creacion de una calculadora de hora final

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura 
hour = hour + mins // 60 
mins = mins % 60 
hour = hour % 24 
print(hour, ":", mins, sep='')

