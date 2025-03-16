

""""
Escribir una función que verifique si un año"
es bisiesto. Un año bisiesto ocurre en 
la mayoría de los años fin de siglo, pero no en todos. "
"""

def bisiesto(año):
    if año%4==0 and año%100!=0 or año%400==0:
        return True
    else:
        return False
    




""""
Escribe una función que tome 2 parámetros: Año y mes, y cuente cuántos días hay en ese mes en ese año."
"""

def dias_mes(año,mes):
    if año<1582 or mes<1 or mes>12:
        return None
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    res=dias[mes-1]
    if mes==2 and bisiesto(año):
        res=29
    return res


año=int(input("Escribe un año: "))  
mes=int(input("Escribe un mes: "))

print(dias_mes(año,mes))

"""""
Escribe una función que tome 3 parámetros: día, mes y año, y devuelva cuantos días han pasado desde el inicio del año."
"""

def dias_desde_inicio(año,mes,dia):
    if dias_mes(año,mes) is None:
        return None
    
    else:
        res=dia
        i=1
        while i<mes:
            res+=dias_mes(año,i)
            i+=1
        return res
    
año=int(input("Escribe un año: "))
mes=int(input("Escribe un mes: "))
dia=int(input("Escribe un dia: "))

print(dias_desde_inicio(año,mes,dia))

""""
Escribe una función que diga si un numero es primo o no "
"""

def es_primo(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input("Escribe un numero: "))
print(es_primo(n))

"""
Escribe una función que transforme los km por litro en millas por galón (EE. UU.). y una que haga de millas por galón a 100 km por litro."
"""
milla=1.609344
galon=3.785411784

def l100kmtompg(litros):
    return (100*1000)/(litros*milla/galon)

litros=float(input("Escribe los litros por 100 km: "))
print(l100kmtompg(litros))

def mpgtol100km(mpg):
    return 100/(mpg*galon/milla)

mpg=float(input("Escribe las millas por galon: "))
print(mpgtol100km(mpg))


