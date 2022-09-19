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


def operacion(lista, index):
    global cuenta
    final = lista
    print(final)
    contadorDeerrores = 0
    for index, i in enumerate(final):
        # * e quita espacios
        e = " ".join(i.split())
        programa = e.split(" ")
        if programa[0] == 'nueva':
            variable = Ctrloperacion.crearVaribale(programa, index)
            if len(programa) < 3 or len(programa) > 4:
                contadorDeerrores += 1
                print("errores: ", listErrores.append([{"error": "001", "msg": "Error de declarion variable"}]))
            else:
                print("tam ", len(programa), " variable devuelta : ", variable)
        elif programa[0] == 'cargue':
            print("segunda")
        elif programa[0] == 'lea':
            print("tercera")
        elif programa[0] == 'almacene':
            print("cuarta")
        elif programa[0] == 'reste':
            print("quinta")

        elif programa[0] == 'multiplique':
            print("sexta")

        elif programa[0] == 'vaya si':
            print("septima")

        elif programa[0] == 'etiqueta':
            print("octava", 'etiqueta', programa[1])

        elif programa[0] == 'muestre':
            print("novena")

        elif programa[0] == 'reste':
            print("quinta")

        elif programa[0] == 'reste':
            print("quinta")

        elif programa[0] in 'O':
            print("operacion logica or")

        elif programa[0] == 'Y':
            print("operacion logica and")

        elif programa[0] == 'NO':
            print("operacion logica nor")

        elif programa[0] == 'muestre':
            print('muestre operacion')

        cuenta += 1


def buscarVariables(programa):
    for i in programa:
        pass


def buscarEtiquetas(programa):
    pass


def mostrarErroes() -> list:
    return listErrores
