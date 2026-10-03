# Entrada de datos
"""beneficiario = input("Agrega Beneficiario: ")
codigo = input("Codigo: ")
base = int(input("Base "))
"""

beneficiario = ""
codigo = ""
base = 0
capitulo = ""


# Extraer datos del código y determinar capítulo
def ExtraerDatosCodigo(codigo):
    letra = codigo[0]
    parte_decimal = codigo[4:]
    porcentaje = int(parte_decimal)
    numcapitulo = int(codigo[1:3])
    return letra, parte_decimal, porcentaje, numcapitulo


# punto a) Cálculo del monto
def sumafijapuntoa(monto):
    monto = base + 25000
    return monto

# punto b)
def sumafijapuntob(letra, monto):
    if "A" <= letra <= "L":
        monto += 25000
    elif "M" <= letra <= "Z" and letra != "U":
        monto += 40000
    elif letra == "U":
        monto += 100000
    return monto



# Aplicar porcentaje
def aplicarporcentaje(monto, porcentaje):
    monto_final = monto + (monto * porcentaje / 100)
    return monto_final


# esta es la adaptación de la determinación del capítulo: no lo necesitamos para este TP3, pero
# la consigna extra del TP1 incluía modificacines en el calculo del monto final en dos capitulos "E" y "F"
def consignaextra(letra, numcapitulo, monto_final):

    # la letra fue extraida con ExtraerDatosCodigo y luego se usa para determinar si
    # hay que seguir modificando el monto final (consigna extra de la entrega)
    if letra == "E":
        capitulo = "Capitulo IV  Enfermedades endocrinas, nutricionales y metabólicas"
        if numcapitulo > 5:
            mitad_base = base * 50 / 100
            monto_descuento = (monto_final * 37 / 100)
            if monto_descuento > mitad_base:
                monto_final = monto_final - monto_descuento

    elif letra == "F":
        capitulo = "Capitulo V Trastornos mentales y del comportamiento"
        if numcapitulo % 2 != 0:
            mitad_base = base * 50 / 100
            monto_descuento = (monto_final * 45 / 100)
            if monto_descuento > mitad_base:
                monto_final = monto_final - monto_descuento

    return monto_final

# Salida EXACTA



# los valores llegan desde principal.py donde se llama al módulo y arranca con esta función principal
#para poder hacer el "calculo normal" que seria el del TP1
def principal(Cod_ICD10, monto_base):
    codigo = Cod_ICD10
    base = monto_base

    letra, parte_decimal, porcentaje, numcapitulo = ExtraerDatosCodigo(codigo)

    #a. Monto fijo que se agrega al base para todos los tratamientos: 25000 pesos.
    monto = sumafijapuntoa(base)

    monto = sumafijapuntob(monto, letra)

    monto_final = aplicarporcentaje(monto, porcentaje)

    # cambiar la lógica de la consigna extra, fue una solución a las apuradas
    monto_final = consignaextra(letra, numcapitulo, monto_final)

    # prints para testeo

    print("Codigo:", codigo)
    print("Capitulo:", numcapitulo)
    print("Monto a pagar:", monto_final)

    return beneficiario, codigo, capitulo, monto_final

if __name__ == "__main__":
    # Único punto de arranque si se ejecuta este archivo directamente, los valores son de ejemplo
    print(principal("H70.1", "5200"))


