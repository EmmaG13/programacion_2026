print("PRACTICA 1")

# Pedir datos al usuario

datos = input("Introduce la temperatura, frecuencia y saturación (separadas por comas): ")

# Separar por comas

lista = datos.split(",")

# translate cada dato a número entero y guardar en variables con nombres simples

t = int(lista[0])
f = int(lista[1])
s = int(lista[2])

# Evaluar las condiciones

if s < 90 or f > 120:
    print("ROJO")
elif t >= 39:
    print("AMARILLO")
else:
    print("VERDE")