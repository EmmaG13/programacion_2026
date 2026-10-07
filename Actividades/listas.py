import time


def suma_objetivo(lista, objetivo):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] + lista[j] == objetivo:
                return True
    return False


def mediryprobar(funcion, lista, objetivo):




    inicio = time.perf_counter()
    resultado = funcion(lista, objetivo)
    fim = time.perf_counter()

    tiempo_total = fim - inicio



    print(f"Tiempo total de ejecucion: {tiempo_total:.6f}")


if __name__ == '__main__':



    lista = [1, 2, 3, 4, 5, 6]
    lista1 = [i for i in range(1000)]
    lista2 = [i for i in range(2000)]
    lista3 = [i for i in range(4000)]
    lista4 = [i for i in range(8000)]


    objetivo = 9
    objetivo2 = 98





    print("--- Pruebas de rendimiento ---")
    mediryprobar(suma_objetivo, lista, objetivo)
    mediryprobar(suma_objetivo, lista1, objetivo2)
    mediryprobar(suma_objetivo, lista2, objetivo)
    mediryprobar(suma_objetivo, lista3, objetivo)
    mediryprobar(suma_objetivo, lista4, objetivo2)


#----------EL IMPOSIBLE-----------


imposible = 99999

print(" El peor caso ")
mediryprobar(suma_objetivo, lista1, imposible)
mediryprobar(suma_objetivo, lista2, imposible)
mediryprobar(suma_objetivo, lista3, imposible)
mediryprobar(suma_objetivo, lista4, imposible)