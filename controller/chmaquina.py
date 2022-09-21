listErrores = []
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

cuenta = -1
import controller.operaciones as Ctrloperacion

cantidad = 0


# TODO : VALIDAR QUE NOMBRE DE VARIABLE NO SE ACOMULADOR-acumulador

def validarVariables(variable):
    #
    if tamVariable(variable):
        if not validarEspacios(variable):
            return not (variable[0].isdigit())


def tamVariable(varibale):
    return 0 <= len(varibale) <= 255


def validarEspacios(variable):
    for i in range(len(variable)):
        if " " in variable:
            listErrores.append("La variable tiene espacios")
            return True

    return False


def obtenerNombreArchivo(archivo):
    return archivo


def leerPrograma2errr(archivo=""):
    # file = open("../archives/factorialvar.ch")
    file = open(archivo)
    lineas = file.readlines()
    nueva = ""
    # print(lineas[0].startswith("//"))
    for ln in range(len(lineas)):
        if not lineas[ln].startswith("//"):
            nueva += lineas[ln]

    nueva = nueva.strip()
    lineas = nueva.split("\n")
    return lineas


def leerPrograma(archivo):
    global cantidad
    # file = open("../archives/factorialvar.ch")
    file = open(archivo, "r")
    if file != " ":
        lineas = file.readlines()
        nueva = ""
        for ln in range(len(lineas)):
            if not lineas[ln].startswith("//"):
                nueva += lineas[ln]

        nueva = nueva.strip()
        nueva = nueva.split("\n")
        file.close()
        cantidad += 1
        return nueva


def programasCantidad():
    return cantidad


def checkeoSintaxis(lista, index):
    global cuenta
    final = lista
    print(final)
    contadorDeerrores = 0
    for index, i in enumerate(final):
        # * e quita espacios
        e = " ".join(i.split())
        programa = e.split(" ")
        if programa[0] == 'nueva':
            if tamParametros(programa[0], index):
                print("EROR EN VARIABLES")
                listErrores.append([{"error": "001", "msg": "Error de declarion variable"}])
                contadorDeerrores += 1
            else:
                variables = Ctrloperacion.crearVaribale(programa, index)
        elif programa[0] == 'cargue':
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) > 3:
                    listErrores.append({"error": "003", "msg": "parametros insuficientes o excedidos"})
        elif programa[0] == 'lea':
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})
        elif programa[0] == 'almacene':
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})
        elif programa[0] == 'reste':
            print("quinta")
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})

            if Ctrloperacion.buscarVariableDato(programa[1], programa) != "I" or Ctrloperacion.buscarVariableDato(
                    programa[1], programa) != "R":
                listErrores.append({"error": "005", "msg": "El dato especificado no se puede resta"})

        elif programa[0] == 'sume':
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})

            if Ctrloperacion.buscarVariableDato(programa[1], programa) != "I" or Ctrloperacion.buscarVariableDato(
                    programa[1], programa) != "R":
                listErrores.append({"error": "005", "msg": "El dato especificado no se puede resta"})

        elif programa[0] == 'divida':
            print("octava", 'etiqueta', programa[1])
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})

            if Ctrloperacion.buscarVariableDato(programa[1], programa) != "I" or Ctrloperacion.buscarVariableDato(
                    programa[1], programa) != "R":
                listErrores.append({"error": "005", "msg": "El dato especificado no se puede resta"})

        elif programa[0] == 'multiplique':
            print("novena")
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})

            if Ctrloperacion.buscarVariableDato(programa[1], programa) != "I" or Ctrloperacion.buscarVariableDato(
                    programa[1], programa) != "R":
                listErrores.append({"error": "005", "msg": "El dato especificado no se puede resta"})

        elif programa[0] == 'divida':
            print("quinta")
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})

            if Ctrloperacion.buscarVariableDato(programa[1], programa) != "I" or Ctrloperacion.buscarVariableDato(
                    programa[1], programa) != "R":
                listErrores.append({"error": "005", "msg": "El dato especificado no se puede resta"})
        elif programa[0] == 'potencia':
            print("quinta")
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})

            if Ctrloperacion.buscarVariableDato(programa[1], programa) != "I" or Ctrloperacion.buscarVariableDato(
                    programa[1], programa) != "R":
                listErrores.append({"error": "005", "msg": "El dato especificado no se puede resta"})

        elif programa[0] in 'modulo':
            print("operacion logica or")
            if Ctrloperacion.buscarVariable(programa[1], index) is False:
                listErrores.append([{"error": "002", "msg": "la variable indicada no existe", "lineal": index}])
            if tamParametros(programa, index):
                if len(programa) <= 2 or len(programa) >= 3:
                    listErrores.append({"error": "004", "msg": "parametros insuficientes o excedidos"})

            if Ctrloperacion.buscarVariableDato(programa[1], programa) != "I" or Ctrloperacion.buscarVariableDato(
                    programa[1], programa) != "R":
                listErrores.append({"error": "005", "msg": "El dato especificado no se puede resta"})

        elif programa[0] in 'concatene':
            print("operacion logica or")

        elif programa[0] in 'elimine':
            print("operacion logica or")

        elif programa[0] in 'extraiga':
            print('operacion logica or')

        elif programa[0] == 'Y':
            print("operacion logica and")

        elif programa[0] == 'O':
            print("operacion logica and")

        elif programa[0] == 'NO':
            print("operacion logica nor")

        elif programa[0] == 'muestre':
            print('muestre operacion')

        elif programa[0] == 'imprima':
            print('muestre operacion')

        elif programa[0] == 'retorne':
            print('muestre operacion')

        elif programa[0] == 'vaya*':
            print('muestre operacion')

        elif programa[0] == 'vaya si':
            print('muestre operacion')

        elif programa[0] == 'etiqueta':
            print('muestre operacion')

        elif programa[0] == 'miOperacion':
            print('mi operacion')

        cuenta += 1


def buscarVariables(programa):
    for i in programa:
        pass


def tamParametros(programa, linea):
    if 2 < len(programa) or len(programa) > 4:
        listErrores.append([{"error": "Minimo de parametros incorrectos", "lineal": linea}])


def buscarEtiquetas(programa):
    pass


def mostrarErroes() -> list:
    return listErrores
