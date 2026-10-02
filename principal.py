""" PENDIENTES
[ ] Tiene la estructura del Parcial 3, en el módulo crear las clases y añadir las funciones como métodos, la estrutura de
 datos principal es el vector: hay que modificar el "ModuloClase.py"

[ ] hay que cambiar la función strip() de CartaTratamientos, posiblemente se quejen, recien aparece en la FICHA 26 y no hay ejemplos de
de uso de archivos con formato csv.



[ ] tema de lo que se puede usar y lo que no, hasta ficha 21: estructura básica tomada de los parciales y ejemplos de las fichas
[ ] Hay que buscar una alternativa a la función.split(), no aparece en las fichas
[ ] No queda clara la consigna cuando dice:
        Si el código de algoritmo informado para un tratamiento en el archivo csv NO ESTÁ en esta tabla, entonces el monto final
        para ese tratamiento debe ser calculado en forma normal, de acuerdo a lo indicado en el TP2.""
"""




import ModuloClase

def CartaTratamientos():
    print("función de opción 1 carga de tratamientos")
    cantidad_filas = 0
    m = open("tratamientos_prueba.cvs")
    v = [] # vector vacío, sin longitud, usamos el metodo append()

    # para leer linea por línea y asignar los valores en variables y luego crear el objeto instanciado
    # desde la clase del módulo importado "ModuloClase.py"
    for linea in m:
        cantidad_filas += 1
        fila = linea
        # cambiar la función split() probablemente no se puede usar, no está en las fichas
        dni, nombre, apellido, icd10, monto, complejidad, id_alg = fila.split(",")

        v.append(ModuloClase.Tratamiento(dni, nombre, apellido, icd10, monto, complejidad, id_alg))

    # dos ejemplos que muestran las dos primeras fijas ya como objetos dentro de vector que pide la consigna
    # llama al metodo especial __str__ para imprimir por  (de los modelos del Parcial3)
    print(v[1])
    print(v[2])


# Función principal del menú de opciones del programa: se ejecuta esta primero por el control
# de ejecución con la variable __name__ (en la consigna del TP).
def principal():
    op = -1

    # Bucle principal del menú: se repite hasta seleccionar la opción 3.
    while op != 0:
        print("1. Cargar Tratamientos")
        print("2. Mostrar Resultados")
        print("0. Salir")

        op = int(input("Ingrese opción:"))

        if op == 1:
            print("opcion 1 seleccionada")
            CartaTratamientos()

        if op == 2:
            print("opción 2 seleccionada")


if __name__ == "__main__":
    principal()
