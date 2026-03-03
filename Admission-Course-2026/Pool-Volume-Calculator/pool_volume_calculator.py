

print("---------------------------------------------------------------------------------------------------------------------------------")
input("Hola, bienvenido a la calculadora de volumen para tu pileta, vamos a necesitar alguos datos para calcularlo, estas ready?")
print("---------------------------------------------------------------------------------------------------------------------------------")

input("Primero, vamos a necesitar el ancho de la pileta, ingresalo sin unidades, solo el numero, gracias.")
ancho = float(input("Ingrese el ancho de la pileta:"))

input("Ahora, vamos a necesitar la profundiad de la pile, ingresala.")
profundidad = float(input("Ingrese la profundidad de la pileta:"))

input("Ultimo dato, vamos a necesitar el largo de la pileta")
largo = float(input("Ingrese el largo de la pileta:"))


volumen = ancho * profundidad * largo
print(f"Ahora si, el volumen de la pileta es: {volumen} , gracias por usar nuestra calculadora.")


if profundidad > 1.9:
    print(f"¡Cuidado! {profundidad} metros de profundidad es mucho. Asegurate de tener las medidas de seguridad necesarias para no tener accidentes.")
else: print("La pileta es bajita, divertite tranquilo")

