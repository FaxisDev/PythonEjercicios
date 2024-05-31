""" Ejercicio
Escribe un programa que pida al usuario una calificación (0-100) y determine si ha aprobado (>=60) o reprobado (<60).
Adicionalmente, clasifica la calificación en A (90-100), B (80-89), C (70-79), D (60-69) o F (<60). """

calificacion = float(input("Ingresa tu calificacion del 0 al 100: "))


if calificacion >= 60:
    print("Tu calificacion es aprobatoria: ")
    if calificacion >= 90 and calificacion <= 100:
        print("Obtuviste un A")
    elif calificacion >= 80 and calificacion <= 89:
        print("Obtuviste un B")
    elif calificacion >= 70 and calificacion <= 79:
        print("Obtuviste un C")
    elif calificacion >= 60 and calificacion <= 69:
        print("Obtuviste un D")
    else:
        print("Te excediste, no podemos determinar tu calificacion")
if calificacion < 0:
    print("Estas loco")
else:
    print("Reprobaste, obtuviste F!")
