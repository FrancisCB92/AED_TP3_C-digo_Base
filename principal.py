import ModuloFunciones

""" PENDIENTES
[ ] Tiene la estructura del Parcial 3, en el módulo crear las clases y añadir las funciones como métodos, la estrutura de
 datos principal es el vector: hay que modificar el "ModuloFunciones.py"

[ ] hay que cambiar la función strip() de CartaTratamientos, posiblemente se quejen, recien aparece en la FICHA 26 y no hay ejemplos de
de uso de archivos con formato csv.
"""


# tema de lo que se puede usar y lo que no, hasta ficha 21: estructura básica tomada de los parciales y ejemplos de las fichas
# No queda clara la consigna cuando dice
# """Si el código de algoritmo informado para un tratamiento en el archivo csv NO ESTÁ en esta tabla, entonces el monto final
# para ese tratamiento debe ser calculado en forma normal, de acuerdo a lo indicado en el TP2.""
def CartaTratamientos():
    print("función de opción 1 carga de tratamientos")
    m = open("tratamientos_prueba.cvs")

    # para leer linea por línea y asignar los valores en variables
    for linea in m:
        fila= (linea.strip())
        print(fila)
        dni, nombre, apellido, icd10, monto, complejidad, id_alg = fila.split(",")
        print("dni "+ dni, "nombre " + nombre, "apellido " + apellido, "icd10 " + icd10, "monto "+ monto, "complejidad " + complejidad, "id_alg " + id_alg)


    # texto = "."

# Función principal del menú de opciones del programa.
def principal():
    op = -1

    # es una lista vacia "[]" para listas!, es la estructura de datos princiapal
    v = []

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
