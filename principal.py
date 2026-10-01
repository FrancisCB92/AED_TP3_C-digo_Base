import ModuloFunciones



def CartaTratamientos():
    print("función de opción 1 carga de tratamientos")
    m = open("tratamientos_prueba.cvs")

    for linea in m:
        fila= (linea.strip())
        print(fila)
        dni, nombre, apellido, icd10, monto, complejidad, id_alg = fila.split(",")
        print("dni "+ dni, "nombre " + nombre, "apellido " + apellido, "icd10 " + icd10, "monto "+ monto, "complejidad " + complejidad, "id_alg " + id_alg)


    # texto = "."

# Función principal del menú de opciones del programa.
def principal():
    op = -1

    # Bucle principal del menú: se repite hasta seleccionar la opción 5.
    while op != 5:
        print("1. Cargar Tratamientos")
        print("2. Mostrar ordenado")
        print("3. Salir")

        op = int(input("Ingrese número de opción: "))

        if op == 1:
            print("opcion 1 seleccionada")
            CartaTratamientos()

        elif op == 2:
            print("opcion 2 seleccionada")



# Si este archivo se ejecuta directamente, comienza la aplicación.
if __name__ == "__main__":
    principal()
