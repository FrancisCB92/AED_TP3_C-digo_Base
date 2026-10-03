# Entrada de datos
beneficiario = input("Agrega Beneficiario: ")
codigo = input("Codigo: ")
base = int(input("Base "))

# Extraer datos del código
letra = codigo[0]
parte_decimal = codigo[4:]
porcentaje = int(parte_decimal)

# punto a) Cálculo del monto
monto = base + 25000

# punto b)
if letra >= "A" and letra <= "L":
    monto += 25000
elif letra >= "M" and letra <= "Z" and letra != "U":
    monto += 40000
elif letra == "U":
    monto += 100000

# Determinar capítulo
num = int(codigo[1:3])

# Aplicar porcentaje
monto_final = monto + (monto * porcentaje / 100)
# mitad_base = monto * 50 / 100

if letra == "A" or letra == "B":
    capitulo = "Capitulo I Ciertas enfermedades infecciosas y parasitarias"
elif letra == "C" or (letra == "D" and num <= 48):
    capitulo = "Capitulo II Tumores [neoplasias]"
elif letra == "D" and num >= 50:
    capitulo = "Capitulo III Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad "
elif letra == "E":
    capitulo = "Capitulo IV  Enfermedades endocrinas, nutricionales y metabólicas"
    if num > 5:
        mitad_base = base * 50 / 100
        monto_descuento = (monto_final * 37 / 100)
        if monto_descuento > mitad_base:
            monto_final = monto_final - monto_descuento

elif letra == "F":
    capitulo = "Capitulo V Trastornos mentales y del comportamiento"
    if num % 2 != 0:
        mitad_base = base * 50 / 100
        monto_descuento = (monto_final * 45 / 100)
        if monto_descuento > mitad_base:
            monto_final = monto_final - monto_descuento

elif letra == "G":
    capitulo = "Capitulo VI Enfermedades del sistema nervioso"
elif letra == "H" and num <= 59:
    capitulo = "Capitulo VII Enfermedades del ojo y sus anexos "
elif letra == "H" and num >= 60:
    capitulo = "Capitulo VIII Enfermedades del oído y de la apófisis mastoides"
elif letra == "I":
    capitulo = "Capitulo IX Enfermedades del sistema circulatorio"
elif letra == "J":
    capitulo = "Capitulo X Enfermedades del sistema respiratorio"
elif letra == "K":
    capitulo = "Capitulo XI Enfermedades del sistema digestivo"
elif letra == "L":
    capitulo = "Capitulo XII Enfermedades de la piel y del tejido subcutáneo"
elif letra == "M":
    capitulo = "Capitulo XIII Enfermedades del sistema osteomuscular y del tejido conjuntivo"
elif letra == "N":
    capitulo = "Capitulo XIV Enfermedades del sistema genitourinario"
elif letra == "O":
    capitulo = "Capitulo XV Embarazo, parto y puerperio"
elif letra == "P":
    capitulo = "Capitulo XVI Ciertas afecciones originadas en el período perinatal"
elif letra == "Q":
    capitulo = "Capitulo XVII Malformaciones congénitas, deformidades y anomalías cromosómicas"
elif letra == "R":
    capitulo = "Capitulo XVIII  Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"
elif letra == "S" or letra == "T":
    capitulo = "Capitulo XIX Traumatismos, envenenamientos y algunas otras consecuencias de causas externas "
elif letra == "V" or letra == "W" or letra == "X" or letra == "Y":
    capitulo = "Capitulo XX Causas externas de morbilidad y de mortalidad"
elif letra == "Z":
    capitulo = "Capitulo XXI Factores que influyen en el estado de salud y contacto con los servicios de salud"
elif letra == "U":
    capitulo = "Capitulo XXII Códigos para propósitos especiales"

# Salida EXACTA
print("Beneficiario:", beneficiario)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", monto_final)

