# PENDIENTES
# [ ] falta control de ejecución con variable __name__
# [ ] % calculado de forma normal? no queda claro si es que simplemente se procede como en el TP1 o sólo
# se calcula el % de manera normal según el TP1 sin tener en cuenta por ej montos fijos del TP1
# "calculo normal": "...el numero despuesta del punto..." (en Whatsapp + punto <e> del TP1)




# def CalcularPorcExtraNormal ()
import ModuloTP1


def aplicaporcentaje(base, porcentaje):
    monto_porcenaje = (base * porcentaje) / 100

    return monto_porcenaje

"""
LA CONSIGNA:
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

def Algoritmo1(alta_complejidad, monto_base, ICD10):
    suma_fija = 0
    if monto_base > 60000:
        # no queda claro qué aplicar, qué parte del TP1: parece ser el punto e (el valor a la derecha del punto)
        # "calculo normal": "...el numero despuesta del punto..." (en Whatsapp + punto <e> del TP1)
        porcentaje_extra = aplicaporcentaje(monto_base, ICD10[4:])

        if alta_complejidad and ICD10[0] != "U":
            suma_fija = monto_base/2
    else:
        porcentaje_extra = 0

    monto_porcentaje = aplicaporcentaje(monto_base, porcentaje_extra)

    monto_final = monto_base + monto_porcentaje + suma_fija
    return monto_final


"""
LA CONSIGNA: 
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

def Algoritmo2(alta_complejidad, monto_base, ICD10):
    porcentaje_extra = 0
    if "A" <= ICD10[0] <= "P":
        # "calculo normal": "...el numero despuesta del punto..." (en Whatsapp + punto <e> del TP1)
        aplicaporcentaje(monto_base, ICD10[4:])
    else:
        if alta_complejidad:
            porcentaje_extra = 2* int(ICD10[4:])

        else:
            porcentaje_extra = aplicaporcentaje(monto_base, 15)


    monto_porcentaje = aplicaporcentaje(monto_base, porcentaje_extra)

    monto_final = monto_base + monto_porcentaje
    return monto_final





"""
LA CONSIGNA:
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
        Sea monto_final = monto_base + monto_extra
"""

def Algoritmo3 (alta_complejidad, monto_base, ICD10):
    monto_extra = 0
    if alta_complejidad:
        # "calculo normal": "...el numero despuesta del punto..." (en Whatsapp + punto <e> del TP1)
        aplicaporcentaje(monto_base, ICD10[4:])

    if "A" <= ICD10[0] <= "L":
        monto_extra = monto_extra + 20000
    elif "M" <= ICD10[0] <= "P":
        # bloque ICD10: ''... son los numeros después de la letra y antes del punto...'' (en grupo de Whatsapp)
        monto_extra = monto_extra + 15000 + 5000 * int(ICD10[1:3])
    else:
        monto_extra = aplicaporcentaje(monto_base, 10)

    if monto_extra > 60000:
        monto_extra = 60000

    return monto_extra

if __name__ == "__main__":
    # pruebas
    Algoritmo1(True, 37212.07, "C16.6")
    Algoritmo2(False, 35248.57, "M15.2")
    Algoritmo3(True, 29659.55, "F30.7")