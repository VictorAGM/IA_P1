
##Las tuplas se leen igual que una lista, pero estas son inmutables, y se declaran con parentesis

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

#Los diccionarios son una estructura de datos que se declaran con llaves, y se componen de pares de llave-valor

diccionario={1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves", 5:"Viernes", 6:"Sabado", 7:"Domingo"}

def dia_semana(dia):
    return diccionario[dia]

for dias in diccionario:
    print(dia_semana(dias))

##Formas de actualizar el diccionario

diccionario[8]="Día que no existe"

diccionario.update({9:"Día que tampoco existe"})

print(diccionario)

#Para eliminar un elemento del diccionario

diccionario.pop(9)
print(diccionario)

del diccionario[8]
print(diccionario)

#Para copiar un diccionario

diccionario_copia=diccionario.copy()
print(diccionario_copia)
