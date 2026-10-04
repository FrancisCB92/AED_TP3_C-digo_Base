""" PENDIENTES
[ ] Tiene la estructura del Parcial 3, en el módulo crear las clases y añadir las funciones como métodos
[ ] hay que cambiar la función strip() de CargaTratamientos, posiblemente se quejen, porque recien se usa
en la FICHA 26 y no hay ejemplo. No encuentro usos de archivos con formato csv en las fichas.
[ ] tema de lo que se puede usar y lo que no, hasta ficha 21: estructura básica tomada de los parciales
 y ejemplos de las fichas
[ ] todavía hay caracteres que hacen que la salida tenga saltos de línea parece, limpiar
[ ] No queda clara la consigna cuando dice:
        Si el código de algoritmo informado para un tratamiento en el archivo csv NO ESTÁ en esta tabla,
        entonces el monto final para ese tratamiento debe ser calculado en forma normal,
        de acuerdo a lo indicado en el TP2.
[] ¿Dónde colocar las funciones/algoritmos? cómo métodos o como un módulo de funciones?

--el ModuloTP1 es para adaptar los calculos de ese TP a este trabajo práctico, adaptándolo: doble testeo
"""

# importamos los módulos
import ModuloClase
import ModuloAlgoritmos


# función de la primera opción para cargar los tratamientos en el vector, tomando las filas del archivo CSV
def CargaTratamientos(v):
    print("función de opción 1 carga de tratamientos")

    # solución provisoria para saltar la primera fila donde están las etiquetas de las columnas en el archivo CSV
    cantidad_tratamientos = -1

    # con esto abrimos el archivo cvs
    m = open("tratamientos_prueba.cvs")

    # para leer línea por línea y asignar los valores en variables y luego crear el objeto instanciado
    # desde la clase del módulo importado "ModuloClase.py"
    for linea in m:
        cantidad_tratamientos += 1

        # --Seguramente tenemos que cambiar la función split() probablemente no se puede usar, no está en las fichas
        # la determinación de la "alta complejidad" del tratamiento procesado se determina con el metodo ContTratamAComplejidad()
        # interno en cada objeto creado e incorporado a vector "v" que funciona como una base de datos (estructura de datos)
        # --parece que el formato de cada valor no está "limpio", hay que quitar los saltos de líneas (sin usar funciones que
        # no estén en las fichas del teórico, posiblemente el manejo de estos CSV se explicó en clases porque no aparecen en
        # las fichas.
        dni, nombre, apellido, icd10, monto, complejidad, id_alg = linea.split(",")

        v.append(ModuloClase.Tratamiento(cantidad_tratamientos,
                                         dni,
                                         nombre,
                                         apellido,
                                         icd10,
                                         monto,
                                         complejidad,
                                         id_alg))

    # dos ejemplos que muestran las dos primeras fijas ya como objetos dentro de vector que pide la consigna
    # llama al metodo especial __str__ para imprimir por  (de los modelos del Parcial3)
    # print(v[1])
    # print(v[2])

    # el primer resultado: cantidad de tratamientos cargados
    r1_1 = cantidad_tratamientos
    return r1_1, v


# función para calcular montos finales, de la 2da opción del menú
def calculomontofinal(v):
    monto_final = 0
    monto_base = 0
    cont_tratamiento = 0
    acumulador_dif = 0

    for t in v:
        cont_tratamiento += 1
        if int(t.id_alg) == 1:
            monto_final = ModuloAlgoritmos.Algoritmo1(t.conttratamacomplejidad(), t.monto, t.icd10)
        if int(t.id_alg) == 2:
            monto_final = ModuloAlgoritmos.Algoritmo2(t.conttratamacomplejidad(), t.monto, t.icd10)
        if int(t.id_alg) == 3:
            monto_final = ModuloAlgoritmos.Algoritmo3(t.conttratamacomplejidad(), t.monto, t.icd10)
        else:
            print("acá es por cálculo del monto normal")

        diferencia = monto_final - monto_base
        acumulador_dif += diferencia

    promedio = acumulador_dif/cont_tratamiento
    return promedio

#función que retorna el apellido del quinto paciente con tratamiento complejo
def r1_2(v):
    contador_r1_2 = 0
    for t in v:
        if t.conttratamacomplejidad():
            contador_r1_2 += 1

        if contador_r1_2 >= 5:
            return (t.apellido)
    return False



# el punto r2.1: hay que calcular los montos finales
def r2_1(v, montos_base, montos_finales):
    r21 = 0
    for t in v:
        print(t)

    print("hay que terminar con los algoritmos de calculo de montos finales antes")


# Función principal del menú de opciones del programa: se ejecuta esta primero por el control
# de ejecución con la variable __name__ (en la consigna del TP).
def principal():
    v = []
    op = -1

    # Bucle principal del menú: se repite hasta seleccionar la opción 3.
    while op != 0:
        print("1. Cargar Tratamientos")
        print("2. Mostrar Resultados")
        print("0. Salir")

        op = int(input("Ingrese opción: "))

        if op == 1:
            print("opcion 1 seleccionada")
            r11, v = CargaTratamientos(v)
            #r1.1: Cantidad de tratamientos cargados.
            print("r1.1: Cantidad de tratamientos cargados: " + str(r11))

            """r1.2: El apellido del paciente del quinto tratamiento de alta complejidad procesado. (Si
            no hubiera 5 tratamientos de alta complejidad, mostrar “No hay suficientes
            tratamientos de alta complejidad.”)"""
            r12 = r1_2(v)
            if r12 == False:
                print("r1.2: No hay suficientes tratamientos de alta complejidad")
            else:
                print("r1.2: El apellido del 5to paciente con tratamiento complejo es: " + r12)


        if op == 2:
            print("opción 2 seleccionada")
            if v:
                calculomontofinal(v)
            else:
                print("No hay tratamientos cargados")



if __name__ == "__main__":
    principal()
