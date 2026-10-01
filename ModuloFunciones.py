
# [*] calculo de porcentaje extra NORMAL? es una función aparte o del TP2?? ver consignas

# def CalcularPorcExtraNormal ()


"""
Si el monto_base es menor o igual a 60000, entonces
porcentaje_extra = 0.
Si el monto_base es mayor a 60000, entonces:
    - Calcular porcentaje_extra en forma normal.
    - Si el tratamiento es de alta complejidad y el ICD10 no es “U”
    agregar una suma fija igual a la mitad del monto base original.
Sea monto_final = monto_base + porcentaje_extra + suma_fija.
///////////////////////////////
Si el tratamiento NO es de alta complejidad, la
suma fija debe quedar en 0. Lo mismo vale si
es de alta complejidad pero el ICD10 es “U”.
"""

def Algoritmo1 (monto_base, alta_complejidad, ICD10):
    porcentaje_extra = 0
    suma_fija = 0
    if monto_base > 60000:
        #CalcularPorcExtraNormal()
        print("calculo % extra normal")
        if alta_complejidad and ICD10 != "U":
            suma_fija = monto_base/2
    monto_final = monto_base + porcentaje_extra + suma_fija
    return monto_final





"""
Si la letra del ICD10 está entre “A” y “P” (ambas incluidas), entonces
porcentaje_extra = cálculo normal sin importar la complejidad del
tratamiento.
Para todo otro ICD10:
    Si el tratamiento es de alta complejidad entonces:
        - Calcular porcentaje_extra duplicando el número indicado a
        la derecha del punto en el IDC10.
    Sino (el tratamiento NO es de alta complejidad):
        - El porcentaje_extra debe ser igual al 15% del monto base en
        todos los casos.
Sea monto_final = monto_base + porcentaje_extra
"""

def Algoritmo2 (monto_base, alta_complejidad, ICD10):
    porcentaje_extra = 0

    # [*] VER si son estos los códigos!
    if ICD10 in "ABCDEFGHIJKLMNOP":
        # CalcularPorcExtraNormal()
        print("calculo de % extra normal")
    else:
        if alta_complejidad:
            # porcentaje_extra = (tomar valor después de la derecha del código ICD10)
            print("calculo tomando valor de la derecha FALTA")
        else:
            porcentaje_extra = (monto_base* 15)/100

    monto_final = monto_base + porcentaje_extra
    return monto_final





"""
Sea monto_extra = 0
Si el tratamiento es de alta complejidad, entonces:
    - Calcular el monto_extra como el 30% del monto base
Sin importar la complejidad, adicionar al monto_extra los siguientes
valores:
    - Si la letra ICD10 está entre “A” y “L”, un monto fijo de 20.000
    - Si la letra ICD10 está entre “M” y “P”, un monto fijo de
        15.000 + 5.000 x <Bloque ICD10>
    - Cualquier otra letra: 10% del monto base
Si monto_extra supera a 60.000, entonces limitar el monto_extra a
60.000
Sea monto_final = monto_base + monto_extra"""

def Algoritmo3 (alta_complejidad, monto_base, ICD10):
    monto_extra = 0
    if alta_complejidad:
        monto_extra = (monto_base * 30)/100

    if ICD10 in "ABCDEFGHIJKL":
        monto_extra = monto_extra + 20000
    elif ICD10 in "MNOP":
        # no se entiende la consigna!! monto_extra = monto_extra + 15000 + 5000 x <Bloque ICD10>
        print("no se entiende la consigna")
    else:
        monto_extra = (monto_base * 10) / 100

    if monto_extra > 60000:
        monto_extra = 60000

    return monto_extra
