""" 

a = 12
b = 60
c = 90

d = a * b * c

print("El resultado de las multiplicaciones es: ", d)

 """
a = int(input("Ingresa numero: "))

for numero in range(1, 11000):
    d = a * numero
    if d % 2 == 0:
        print(f"{numero} x {a} = {d} es Par")
    else:
        print(f"{numero} x {a} = {d} es iPar")
