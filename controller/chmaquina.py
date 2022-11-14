listErrores = []
listaProgramaMemoriaPrincipal = {}
# * Ultimo digito de la cedula
z = 0
# * La capacidad por defecto se asume que es de z * 0 + 50 pos
# * procesador y memoria principal vector
capacidadMaxima = 1000 * z + 100
capacidadDefecto = z * 10 + 50
memoriaPrincipal = []
ACOMULADOR = 0
kernel = 10 * z + 9
# * tipos de variable : entero , cadena , real , logico
tiposAceptados = ["I", "C", "R", "L"]

contenido2 = []
listVariables = {}
guardarVariables = []
cuenta = -1
import controller.operaciones as Ctrloperacion

cantidad = 0


def validarVariables(variable):
    if lenvariable(variable) and not (Ctrloperacion.palabrasReservadas(variable)):
        if not validarEspacios(variable):
            return not (variable[0].isdigit())


def lenvariable(varibale):
    return 0 <= len(varibale) <= 255


def validarEspacios(variable):
    for i in range(len(variable)):
        if " " in variable:
            listErrores.append([{"error": "la variable tiene espacios", "variable": variable}])
            return True

    return False


def obtenerNombreArchivo(archivo):
    return archivo


def checkeoSintaxis(lista):
    global cuenta
    global listVariables
    final = lista
    contadorDeerrores = 0
    for index, i in enumerate(final):
        # * e quita espacios
        e = " ".join(i.split())
        programa = e.split(" ")
        print("sintaxis-> ", len(programa), " -> tamaño", tamParametros2(programa, index), "instrucciones->", programa)
        if programa[0] == 'nueva':
            print("len de variable", len(programa))
            tamParametrosVariables(programa, index)
            Ctrloperacion.verificarVariables(programa, listErrores, tiposAceptados)
            if validarVariables(programa[1]) is False or validarVariables(programa[1]) is None:
                listErrores.append([{"msg": "esta haciendo uso palabras reservadas", "msg2": "Error de sintaxis"}])

        elif programa[0] == 'cargue':
            valExisteVariable(programa)
            tamParametros2(programa, index)
        elif programa[0] == 'lea':
            tamParametros2(programa, index)
        elif programa[0] == 'almacene':
            valExisteVariable(programa)
            tamParametros2(programa, index)
        elif programa[0] == 'reste':
            tamParametros2(programa, index)
            operacionesSumaRestaDivision(programa)
        elif programa[0] == 'sume':
            tamParametros2(programa, index)
            operacionesSumaRestaDivision(programa)
        elif programa[0] == 'divida':
            tamParametros2(programa, index)
            operacionesSumaRestaDivision(programa)
        elif programa[0] == 'multiplique':
            tamParametros2(programa, index)
            operacionesSumaRestaDivision(programa)
        elif programa[0] == 'divida':
            tamParametros2(programa, index)
        elif programa[0] == 'potencia':
            tamParametros2(programa, index)
        elif programa[0] in 'modulo':
            tamParametros2(programa, index)

        elif programa[0] in 'concatene':
            tamParametros2(programa, index)

        elif programa[0] in 'elimine':
            tamParametros2(programa, index)

        elif programa[0] in 'extraiga':
            tamParametros2(programa, index)

        elif programa[0] == 'Y':
            funcion_error_y_o_no(programa)
        elif programa[0] == 'O':
            funcion_error_y_o_no(programa)
        elif programa[0] == 'NO':
            funcion_error_y_o_no(programa)
        elif programa[0] == 'muestre':
            tamParametros2(programa, index)

        elif programa[0] == 'imprima':
            tamParametros2(programa, index)
        elif programa[0] == 'retorne':
            pass
        elif programa[0] == 'vaya*':
            pass
        elif programa[0] == 'vaya si':
            pass
        elif programa[0] == 'etiqueta':
            if tamParametrosEtiqueta(programa, index) is False:
                listErrores.append([{"msg": "error parametros excedidos o insuficientes"}])
        elif programa[0] == 'miOperacion':
            pass


def agregar_variables(instrucciones_archivo):
    for instruccion_interna in instrucciones_archivo:

        e = " ".join(instruccion_interna.split()).strip()
        e = e.strip(" ")
        instrucciones = e.split(" ")
        llave = instrucciones[1]
        llave = llave.strip()
        # agregamos el valor por defecto de cada uno de los tipos de variables
        if instrucciones[0].lower() == "nueva":
            if len(instrucciones) == 3:
                if instrucciones[2] == "I":
                    instrucciones.append(f"{int(0)}")
                elif instrucciones[2] == "L":
                    instrucciones.append(f"{int(0)}")
                elif instrucciones[2] == "R":
                    instrucciones.append(f"{float(0)}")
                elif instrucciones[2] == "C":
                    instrucciones.append(" ")
            listVariables[llave] = {'tipo': instrucciones[2], 'valor': instrucciones[3]}


def ejecucionxacumulador():
    pass


def valExisteVariable(opr):
    if opr[1] not in listVariables:
        listErrores.append("Error, la variable " + opr[1] + " no ha sido asignada")


def operacionesSumaRestaDivision(opr):
    if (listVariables[opr[1]]['tipo'] == "L") or (listVariables[opr[1]]['tipo'] == "C"):
        listErrores.append("Error, la variable " + opr[1] + " no se puede ejecutar en la operacion " + opr[
            0] + " porque su tipo de dato es " + listVariables[opr[1]]['tipo'])


def funcion_error_y_o_no(palabra):
    if len(palabra) > 4:
        listErrores.append("Error, se estan utilizando mas de 4 operandos en la operacion " + palabra[0])
    elif palabra[1] not in listVariables:
        listErrores.append("Error, la variable " + palabra[1] + " no ha sido asignada")
    elif listVariables[palabra[1]]['tipo'] != "L":
        listErrores.append("Error, la variable " + palabra[1] + " no se puede ejecutar en la operacion " + palabra[
            0] + " porque su tipo de dato es " + listVariables[palabra[1]]['tipo'])


def tamParametrosVariables(programa, linea):
    print(len(programa))
    if len(programa) < 2 or len(programa) > 4:
        listErrores.append(
            [{"error Variable": "Error de sintaxis parametros mas o menos de los requeridos", "linea": linea}])


def tamParametros2(programa, linea):
    if len(programa) < 2:
        listErrores.append(
            [{"operacion": programa[0], "msg": "Error de sintaxis parametros mas o menos de dos", "linea": linea}])


def tamParametrosEtiqueta(programa, linea):
    if len(programa) == 3:
        return True
    else:
        return False


def mostrarErroes() -> list:
    return listErrores
