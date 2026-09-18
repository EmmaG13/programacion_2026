print(" PRACTICA 2")

#Variables

s = 10000
sum_dia = 1000



print("Bienvenido, su saldo es: $" + str(s))
print("Usted ha retirado $" + str(sum_dia) + " el dia de hoy.")

r = float(input("¿Cuanto desea retirar?: "))

sum_dia = sum_dia + r

if r % 50 != 0:
    print("MONTO NO VALIDO, DEBE SER MULTIPLO DE 50")
elif r > s:
    print("SALDO INSUFICIENTE")
elif sum_dia >= 6000:
    print("LIMITE DE RETIRO DIARIO ALCANZADO")
else:
    s = s - r
    print("Su nuevo saldo es: $" + str(s))