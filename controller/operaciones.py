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
    "acomulador"

]


def palabrasReservadas(variable):
    return variable in operacion


tiposAceptados = ["I", "C", "R", "L"]
global estructuraVariables
estructura = {}
global listaGeneral
# ? ESTRATEGIA USO DE DICCIONARIO o no -> ejm {nombre : 'unidad','tipodato':'I','Valor'}
# ? INSTRUCCION -> [ codigoPrograma: 0000, {linea : None , Intruccion : [ nueva, unidad, 2 , dato]]
estructurVariables = {}


# * EstructuraVariable = {operando,nombre tipoDato:,dato: None}
def verificarVariables(variable, listaErr, tipoDatos):
    if len(variable) == 3:
        if variable[2] == "I":
            variable.append(0)
        elif variable[2] == "L":
            variable.append("0")
        elif variable[2] == "R":
            # pasarlo a float cuando se este operando con el
            variable.append('0')
        elif variable[2] == "C":
            variable.append(" ")

    # * analizar parametros 2 y 3
    if variable[2] == "I" and variable[3].isdigit() is False:
        listaErr.append([{"msg": f"La inializacion no es correcta con el tipo de datos {variable[2] != variable[3]}"}])

    if variable[2] == "R" and variable[3].isDecimal() is False:
        listaErr.append([{"msg": f"La inializacion no es correcta con el tipo de datos {variable[2] != variable[3]}"}])

    if variable[2] == "C" and not (variable[3].isalpha() is True or variable[3].isascii() is True):
        listaErr.append([{"msg": f"La inializacion no es correcta con el tipo de datos {variable[2] != variable[3]}"}])

    if variable[2] == "L" and not (variable[3] == "0" or variable[3] == "1"):
        listaErr.append([{"msg": f"La inializacion no es correcta con el tipo de datos {variable[2] != variable[3]}"}])
    if variable[2] not in tipoDatos:
        listaErr.append([{"msg": f"La inializacion no es correcta con el tipo de datos {variable[2] != variable[3]}"}])






