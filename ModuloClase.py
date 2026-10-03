# PENDIENTERS
# [ ] falta "control de ejecución mediante la variable __name__" ¿En este módulo que contiene clases?




class Tratamiento:
    # Constructor: inicializa los atributos del objeto al crearlo.
    def __init__(self, id, dni, nombre, apellido, icd10, monto, complejidad, id_alg):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.icd10 = icd10
        self.monto = monto
        self.complejidad = complejidad
        self.id_alg = id_alg



    # Metodo especial __str__: devuelve una cadena legible para imprimir el objeto.
    def __str__(self):
        r = ""
        r += "\nid: " + str(self.id)
        r += "\ndni: "+ str(self.dni)
        r += "\nnombre: " + self.nombre
        r += "\napellido: " + self.apellido
        r += "\nicd10: " + self.icd10
        r += "\nmonto: "+ self.monto
        r += "\ncomplejidad: " + self.complejidad
        r += "\nid_alg: " + self.id_alg
        return r

    def conttratamacomplejidad(self):
        if self.complejidad == "A":
            return True
        else:
            return False



