var=1
print(var)


edad="20"
print(edad)
print("Me llamo Victor y tengo " + edad)

var=1+5
print(var)

#Asignar el resultado de una operación a una variable
a=3
b=4
c=(a**2+b**2)**0.5
print(c)

#Ejercicio
john=3
mary=5
adan=6

print(john,mary,adan,sep=",")

total_apples=john+mary+adan

print(total_apples)

#Abreviacion de operaciones
a=1
a+=1
print(a)

a*=2
print(a)

#Convertidor de Millas a Kilometros
millas=12.34
kilometros=45.23

millas_a_kilometros=millas*1.61
kilometros_a_millas=kilometros/1.61

print(millas,"millas son",round(millas_a_kilometros,2),"kilometros")
print(kilometros,"kilometros son",round(kilometros_a_millas,2),"millas")

#Calcular para X en la sig. expresion: 3x3 - 2x2 + 3x - 1

x = 1
x = float(x)


y=(3*x**3)-(2*x**2)+3*x-1
print("y =", y)
