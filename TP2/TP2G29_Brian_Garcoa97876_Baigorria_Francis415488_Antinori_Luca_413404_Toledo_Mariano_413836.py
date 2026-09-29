# ==============================================================================
# DEFINICIÓN DE FUNCIONES (Procesamiento de líneas)
# ==============================================================================

def procesar_linea_adicionales(linea):
    """
    Extrae los montos de adicionales de una línea que comienza con '#'.
    Convierte cada monto a entero (int) eliminando los espacios.
    """
    a_l = int(linea[2:7].strip())
    m_z = int(linea[8:13].strip())
    u = int(linea[14:19].strip())
    return a_l, m_z, u


def procesar_linea_paciente(linea):
    """
    Extrae los datos del paciente de una línea estándar.
    Limpia los espacios fijos con .strip().
    """
    nombre = linea[0:25].strip()
    codigo = linea[25:31].strip()
    monto = int(linea[31:39].strip())

    # El caracter 39 es opcional (alta complejidad 'X')
    complejo = False
    if len(linea) > 39 and linea[39] == 'X':
        complejo = True


    return nombre, codigo, monto, complejo


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

# Variables de control de adicionales
montos_A_L = montos_M_Z = montos_U = 0

# Inicialización de contadores y acumuladores para los resultados (r1 a r10)
r1 = 0  # Total tratamientos
r2 = r3 = r4 = r5 = r6 = r11 = 0  # Contadores A, B, C, E, P

# Variables para r7 (Promedio capítulo 19)
acum_monto_cap19 = 0
cant_trat_cap19 = 0

monto_base_menor_r11 = 0
bandera_linea_r11 = False

# Variables para r8 y r9 (Mayor importe no 'U')
r8 = ""     # Nombre del paciente con mayor importe
r9 = -1.0   # Mayor importe final

# Variables para r10 (Porcentaje alta complejidad > promedio general)
monto_base_menor_compl = 0
cant_alta_complejidad = 0
cant_alta_comp_mayor_prom = 0

# Variables auxiliares para calcular el promedio general de TODOS los tratamientos
acum_monto_general = 0

# --- PRIMERA PASADA O CONTROL DEL ARCHIVO ---
# Dado que r10 nos pide comparar tratamientos contra el "promedio pagado por TODOS los tratamientos",
# necesitamos calcular ese promedio general primero. Al no poder usar arreglos, leeremos el archivo dos veces.

# --- PASO 1: Calcular el Promedio General de todos los tratamientos ---
txt = open("tratamientos.txt", "r")

while True:
    linea = txt.readline()
    if linea == "":
        break

    if linea[0] == '#':
        montos_A_L, montos_M_Z, montos_U = procesar_linea_adicionales(linea)
    else:
        nombre_pac, cod_ICD10, monto_base, trat_complejo = procesar_linea_paciente(linea)
        r1 += 1 # Contamos de manera preliminar el total para el promedio general

        # Determinar letra capitular y número de enfermedad
        letra = cod_ICD10[0]

        # Buscar el número de enfermedad a la derecha del punto
        pos_punto = cod_ICD10.find('.')
        num_enfermedad = int(cod_ICD10[pos_punto + 1:])

        # Calcular monto intermedio sumando adicionales
        monto_intermedio = monto_base
        if 'A' <= letra <= 'L':
            monto_intermedio += montos_A_L
        elif 'M' <= letra <= 'Z' and letra != 'U':
            monto_intermedio += montos_M_Z
        elif letra == 'U':
            monto_intermedio += montos_U

        # Sumar el porcentaje según el número de enfermedad
        monto_final = monto_intermedio + (monto_intermedio * num_enfermedad / 100)

        # Recargo por alta complejidad
        if trat_complejo:
            monto_final += (monto_final * 0.05)


        acum_monto_general += monto_final

txt.close()

# Promedio general global de todo el archivo
promedio_general_todos = 0.0
if r1 > 0:
    promedio_general_todos = acum_monto_general / r1


# --- PASO 2: Procesamiento Final y Estadísticas ---
# Reiniciamos r1 y abrimos el archivo nuevamente para procesar todos los puntos limpios
r1 = 0
txt = open("tratamientos.txt", "r")

while True:
    linea = txt.readline()
    if linea == "":
        break

    if linea[0] == '#':
        bandera_linea_r11 = True
        montos_A_L, montos_M_Z, montos_U = procesar_linea_adicionales(linea)
    else:
        # Extraer datos usando la función
        nombre_pac, cod_ICD10, monto_base, trat_complejo = procesar_linea_paciente(linea)

        # r1: Cantidad total de tratamientos
        r1 += 1

        # Determinar componentes del código ICD10
        letra = cod_ICD10[0]
        pos_punto = cod_ICD10.find('.')
        num_enfermedad = int(cod_ICD10[pos_punto + 1:])

        if monto_base_menor_r11 > monto_base:
            monto_base_menor_r11 = monto_base




        # r2 a r6: Conteo por iniciales específicas
        if letra == 'A': r2 += 1
        elif letra == 'B': r3 += 1
        elif letra == 'C': r4 += 1
        elif letra == 'E': r5 += 1
        elif letra == 'P': r6 += 1

        # --- CÁLCULO DEL IMPORTE FINAL DEL TRATAMIENTO ---
        monto_intermedio = monto_base
        if 'A' <= letra <= 'L':
            monto_intermedio += montos_A_L
        elif 'M' <= letra <= 'Z' and letra != 'U':
            monto_intermedio += montos_M_Z
        elif letra == 'U':
            monto_intermedio += montos_U

        monto_final = monto_intermedio + (monto_intermedio * num_enfermedad / 100)

        if trat_complejo:
            monto_final += (monto_final * 0.05)
            if bandera_linea_r11:
                r11 = monto_final

        bandera_linea_r11 = False

        # --- FIN CÁLCULO IMPORTE FINAL ---

        # r7: Capítulo 19 del estándar ICD10 (Códigos S00 a T98)
        # Extraemos el número capitular antes del punto (ej: de 'S04.1' toma el '04' -> 4)
        num_capitulo = int(cod_ICD10[1:pos_punto])
        if (letra == 'S' and 0 <= num_capitulo <= 99) or (letra == 'T' and 0 <= num_capitulo <= 98):
            acum_monto_cap19 += monto_final
            cant_trat_cap19 += 1

        # r8 y r9: Mayor importe final excluyendo la letra U
        if letra != 'U':
            if monto_final > r9:
                r9 = monto_final
                r8 = nombre_pac

        # r10: Tratamientos de alta complejidad
        if trat_complejo:
            cant_alta_complejidad += 1
            if monto_final > promedio_general_todos:
                cant_alta_comp_mayor_prom += 1


txt.close()

# --- Cálculos finales de promedios y porcentajes ---

# r7: Promedio del capítulo 19
r7 = 0.0
if cant_trat_cap19 > 0:
    r7 = round(acum_monto_cap19 / cant_trat_cap19, 2)

# Redondeo del mayor importe obtenido (r9)
if r9 != -1.0:
    r9 = round(r9, 2)
else:
    r9 = 0.0

# r10: Porcentaje entero
r10 = 0
if cant_alta_complejidad > 0:
    r10 = int((cant_alta_comp_mayor_prom * 100) // cant_alta_complejidad)


# ==============================================================================
# SALIDAS OBLIGATORIAS (Estrictamente bajo el formato exigido)
# ==============================================================================
print('(r1) Cantidad de tratamientos cargados:', r1)
print('(r2) Cantidad de tratamientos "A":', r2)
print('(r3) Cantidad de tratamientos "B":', r3)
print('(r4) Cantidad de tratamientos "C":', r4)
print('(r5) Cantidad de tratamientos "E":', r5)
print('(r6) Cantidad de tratamientos "P":', r6)
print('(r7) Importe final promedio (capitulo 19):', r7)
print('(r8) Paciente (no tipo "U") que pago el mayor importe final:', r8)
print('(r9) Mayor importe pagado por ese paciente:', r9)
print('(r10) Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:', r10)
print("r11 consigna extra:" , r11)