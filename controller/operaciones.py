operacion = [
    "carge",
    "almacene",
    "nueva",
    "lea",
    "sume",
    "reste",
    "multiplique",
    "divida",
    "potencia",
    "modulo",
    "concatene",
    "elimine",
    "extriga"
    "Y",
    "O",
    "NOT",
    "muestre",
    "imprima",
    "retorno",
    "vaya",
    "vaya si",

]
tiposAceptados = ["I", "C", "R", "L"]

estructura = {}

# ? ESTRATEGIA USO DE DICCIONARIO o no -> ejm {nombre : 'unidad','tipodato':'I','Valor'}
# ? INSTRUCCION -> [ codigoPrograma: 0000, {linea : None , Intruccion : [ nueva, unidad, 2 , dato]]
estructurVariable = {}


# * EstructuraVariable = {operando,nombre tipoDato:,dato: None}
def crearVaribale(lista, linea):
    tipoDato = lista[2]
    nombre = lista[1]
    tamLista = len(lista)
    print("Linea instruccion ", linea)
    # TODO : validar varibale size , inicio
    if tamLista == 3:
        # * entero
        if tipoDato == 'I':
            estructurVariable["nombre"] = nombre
            estructurVariable["tipoDato"] = tipoDato
            estructurVariable["dato"] = 0
        # * cadena

        elif tipoDato == 'C':
            estructurVariable["nombre"] = nombre
            estructurVariable["tipoDato"] = tipoDato
            estructurVariable["dato"] = " "
        # * real

        elif tipoDato == 'R':
            estructurVariable["nombre"] = nombre
            estructurVariable["tipoDato"] = tipoDato
            estructurVariable["dato"] = float(0)
        # * logico

        elif tipoDato == 'L':
            estructurVariable["nombre"] = nombre
            estructurVariable["tipoDato"] = tipoDato
            estructurVariable["dato"] = 0
        return estructurVariable

    elif tamLista == 4:
        estructurVariable["nombre"] = nombre
        estructurVariable["tipoDato"] = tipoDato
        estructurVariable["dato"] = lista[3]
        return estructurVariable


def buscarVariable(variable, linea, listPrograma):
    return variable == listPrograma["nombre"]

def sume():
    pass


def almacener():
    pass
