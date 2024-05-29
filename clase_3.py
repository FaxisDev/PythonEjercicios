numero = float(input("Ingresa un valor en grados Centigrados: "))

# El operador '==' Significa que el valor debe ser igual
# el operador '===' Significa identico a el valor
""" if numero == 4:
    print("El numero es correcto! ")
else:
    print("El valor no es correcto") """


# Operador de negacion != No es
""" if numero != 30:
    print("El numero que ignresaste no es correcto, no es 30")
else:
    print("Ingresaste el valor 30") """

# Mayor que '>' o menor que '<' y mayor o igual que '>=' y menor igual que '<='
""" if numero >= 25:
    print("Hiciste la operacion correctamente")
else:
    print("No llegaste mas de los 25")
 """

""" if numero < 25:
    print("Hiciste la operacion correctamente")
    if numero == 10:
        print("Escribiste 10")
    else:
        print("Si cumplsite la condicion de menor que 25, pero no fue 10")
else:
    print("No llegaste menos de los 25") """


# Ejercicio, determinar si un clima esta entre los rangos 25 - 50 centigrados
if numero >= 25:
    if numero <= 50:
        print("El clima esta rico")
    else:
        print("El clima esta horrible")
else:
    print("El clima esta horrible")

#Forma simplificada:
if numero >= 25 and numero <= 50:
    print("El clima esta rico")
else:
    print("El clima esta horrible")
