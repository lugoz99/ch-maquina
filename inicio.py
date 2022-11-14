"""
* from controller.chmaquina import *
import controller.chmaquina as ctrl
img = PhotoImage(file="img/procesador.png")
Label(root, image=img).pack()
"""
# TODO : pueden existir espacios entre lineas por lo tanto hay eliminar esos
# TODO esos espacios o buscar en que linea existen elementos en la linea
from tkinter.filedialog import askopenfilenames
import glob
import time

global ACUMULADOR
programaPrincipal = {}
posicionVariables = []
import controller.chmaquina as ctrl
import controller.operaciones as op
from pathlib import Path
import controller.ejecucion as ejecucion
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import ttk
import os
from tkinter import messagebox
from tkinter import font

nueva = ""
kernel = 10
lista01 = []
diccionarioMemoeriaPrincipal = {}
root = Tk()
memoriaInicial = IntVar()
contador = 11
numeroPrograma = 0
diccionarioVariables = {}
diccionarioEtiquetas = {}
root.option_add("*Font", 'FiraCode 12 bold')
wd = root.winfo_screenwidth()
wh = root.winfo_screenheight()
root.geometry("%dx%d" % (wd, wh))
root.title("ch-maquina")
# *----------------- MENU BAR -------------------------------------
menuBar = Menu(root)
archivoMenu = Menu(menuBar, tearoff=0)
archivoMenu.add_command(label="Open", command=lambda: select_file1(), font=('Cascadia Mono', 12))
menuBar.add_cascade(label="file", menu=archivoMenu)

ejecute = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Ejecute", command=lambda: logicaChMaquina())

muestre = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Muestre", command=lambda: mostrarMapa())

pasoxpaso = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="PasoxPaso")

salir = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Salir", command=lambda: exitProg())
root.config(menu=menuBar)
menuBar.config(background="blue")


def exitProg():
    root.quit()


# ********************** GENERAR KERNEL **********************************************************
def generarKernel():
    pass


# * --------------------AREA DEL PROCESADOR ------------------------------
frameProceador = Frame(root, bd=5, width=350, height=90)
frameProceador.grid(row=0, column=0, sticky="ne")

imagProcesador = Image.open("img/procesador.png")
newsize = (80, 80)
imagProcesador = imagProcesador.resize(newsize)
imagenContainer = ImageTk.PhotoImage(imagProcesador)
food = LabelFrame(frameProceador, relief=RAISED, bd=0)
Label(food, image=imagenContainer).grid(row=0, column=0)
food.grid(row=0, column=0, sticky="w")
frameProceador.grid_propagate(False)
# *---------------LABEL MEMORIA-KERNEL---------------
textMemeroria = IntVar()
textMemeroria.set(100)

labelMemroia = LabelFrame(frameProceador, width=250, height=50, relief=SUNKEN)
labelMemroia.grid(row=0, column=1, sticky="ns")
labelMemroia.grid_propagate(False)
labeM = Label(labelMemroia, text="Memoria", width=10)
labeM.grid(row=0, column=0, pady=5)
labeK = Label(labelMemroia, text="Kernel", width=10)
labeK.grid(row=1, column=0, pady=10)
frameProceador.grid_propagate(False)
# * Memoria
spM = Spinbox(labelMemroia, from_=0, to=999, width=10, wrap=True, textvariable=textMemeroria)
spM.grid(row=0, column=1, padx=4)
# * Kernel
textFinal = IntVar()  # * SE USA PARA VALIDAR QUE NO SE CAMBIE EL KERNE CUANDO SE CARGE PROGRAMA
textFinal.set(10)
spK = Spinbox(labelMemroia, from_=10, to=20, width=10, wrap=True, command=lambda: cambios(), textvariable=textFinal)
spK.grid(row=1, column=1, padx=4)


# ? no cambiar kernel cuando se abre area de trabjo o ejecion
def cambios():
    if tamListaPrograma():
        spK.configure(state='disabled')
        textFinal.set(int(spK.get()) - 1)


# *-------------LABEL FIN -------------------------
# *----------------------ACOMULADOR------------------------
frameAcumulador = Frame(root, width=250, height=95, borderwidth=2, border=2, relief=RIDGE)
frameAcumulador.grid(row=0, column=1, sticky="ne")

textAcumulador = IntVar()
etiqueta1 = Label(frameAcumulador, text="Acumulador")
etiqueta1.place(x=5, y=5)
acumulador = ttk.Entry(frameAcumulador, justify=CENTER, width=15, state="readonly", textvariable=textAcumulador)
acumulador.place(x=104, y=5)

etiqueta2 = Label(frameAcumulador, text="PC")
etiqueta2.place(x=5, y=65)
ins = StringVar()
pc = ttk.Entry(frameAcumulador, justify=CENTER, width=22, state="readonly", textvariable=ins)
pc.place(x=40, y=65, anchor=NW)

textPrograma = StringVar()
programa = ttk.Entry(frameAcumulador, justify=CENTER, width=26, state="readonly", textvariable=textPrograma)
style = ttk.Style()
style.configure("Custom.TLabel", foreground="white",
                background="#3baea0",
                padding=[1, 1, 1, 1]
                )

programa.configure(style="Custom.TLabel")
programa.place(x=5, y=35, anchor=NW)
frameAcumulador.grid_propagate(False)
# *----------------------FINACOMULADOR------------------------
# *--------------------------- AREAS DE TRABAJO --------------------
frameTb = Frame(root, width=600, height=427)
frameTb.grid(row=1, column=0, padx=50, pady=10)
# frameTb.config(height=400, width=200)
listaPrograma = Listbox(frameTb, width=30, height=20, activestyle='none', selectbackground='#69bbf1',
                        selectmode="EXPAND")
listaPrograma.grid(row=0, column=0)
# * --------------------- SCROLL ---------------------------------------------
scroll_one = Scrollbar(frameTb, command=listaPrograma.yview, orient='vertical')
scroll_one.grid(column=1, row=0, sticky='NS')
# * --------------------- FINSCROLL---------------------------------------------
listaPrograma.configure(yscrollcommand=scroll_one.set)
listaPrograma.grid_propagate(False)
frameTb.grid_propagate(False)
# *------------------------- AREA DE VARIABLES Y ETIQUETAS --------------------------
frameAreaVT = Frame(frameTb)
frameAreaVT.grid(row=0, column=2)
frameLb = LabelFrame(frameAreaVT, text="Variables")
listaVariables = Listbox(frameLb, background="#acdcee", width=30, height=9, activestyle='none')
listaVariables.pack(side=TOP, fill=X, expand=False)
frameLb1 = LabelFrame(frameAreaVT, text="Etiquetas")
listaEtiquetas = Listbox(frameLb1, background="#ff8585", width=30, height=9, activestyle='none')
listaEtiquetas.pack(side=TOP, fill=X, expand=False)
listaVariables.insert(0, " Pos    Variables")
listaEtiquetas.insert(0, "Pos   Etiquetas")

frameLb.grid(row=0, column=0, sticky="S")
frameLb1.grid(row=1, column=0)
frameAreaVT.grid_propagate(True)

# *------------------------------AREA DEL PC-IMPRESORA ----------------------------------------

framePCImpresora = Frame(root, width=350, height=630, relief=RIDGE)
framePCImpresora.place(x=650, y=100)
newsize = (380, 240)
newsize1 = (300, 200)
imgPc = Image.open("img/computer-modified(4)(2).png")
imgPc = imgPc.resize(newsize)
tkpic = ImageTk.PhotoImage(imgPc)
canvas = Canvas(framePCImpresora, height=290)
labelT = Label(canvas, image=tkpic)
labelT.grid(row=0, column=0)
canvas.grid(row=0, column=0)
canvas.grid_propagate(False)

# *-------------------------------PANTALLA -----------------------------------------------
listp = Listbox(canvas, width=25, height=6, activestyle='none', selectmode="browse")
listp.place(in_=labelT, x=-3, relx=0.5, rely=0.4, y=4, anchor=CENTER)

# *-------------------------------PANTALLA -----------------------------------------------

framePCImpresora.grid_propagate(False)
imgPr = Image.open("img/printer-146481_640(5).png")
imgPr = imgPr.resize(newsize1)
tkpic2 = ImageTk.PhotoImage(imgPr)
label1 = Label(framePCImpresora, image=tkpic2)
label1.grid(row=1, column=0)
framePCImpresora.grid_propagate(False)
imprimir = ttk.Button(framePCImpresora, text="Imprimir", cursor="hand2")
imprimir.place(x=45, y=280)

labelTop = Label(framePCImpresora, text="Modo", width=6)
labelTop.place(x=45, y=240)

combo = StringVar()
combo.set("Kernel")
comboExample = ttk.Combobox(framePCImpresora, textvariable=combo,
                            values=[
                                "User",
                                "Kernel"], state="read", width=10)
comboExample.place(x=120, y=240)
comboExample.configure(state="readonly")
# *-------------------------------TEXTO IMPRESORA--------------------------
printerText = Listbox(framePCImpresora, width=20, height=18)
printerText.place(y=450, x=100)

# ***************************************************************************
# *------------------------------BLOQUE DE PROGRAMAS ------------

tablaBloque = ttk.Treeview(root)
tablaBloque['columns'] = ("ID", "PROGRAMA", '#INS', "RB", "RLC", "RLP")
tablaBloque.column('#0', width=0, stretch=NO)
tablaBloque.column('ID', anchor=CENTER, width=80)
tablaBloque.column('PROGRAMA', anchor=CENTER, width=150)
tablaBloque.column('#INS', anchor=CENTER, width=80)
tablaBloque.column('RB', anchor=CENTER, width=80)
tablaBloque.column('RLC', anchor=CENTER, width=80)
tablaBloque.column('RLP', anchor=CENTER, width=80)

tablaBloque.heading("ID", text='ID', anchor=CENTER)
tablaBloque.heading("PROGRAMA", text='PROGRAMA', anchor=CENTER)
tablaBloque.heading("#INS", text='#INS', anchor=CENTER)
tablaBloque.heading("RB", text='RB', anchor=CENTER)
tablaBloque.heading("RLC", text='RLC', anchor=CENTER)
tablaBloque.heading("RLP", text='RLP', anchor=CENTER)

tablaBloque.grid(row=3, column=0)

# *********************************************************************
# *-------------------- MAPA DE MEMORIA----------------------------------------
tablaMemoria = ttk.Treeview(root, selectmode=BROWSE, height=35)


def tamListaPrograma():
    return listaPrograma.size() > 0


def nroProgamasCargados(nro):
    if nro < 10:
        return '000' + str(nro)
    elif nro > 9 and nro < 100:
        return '00' + str(nro)
    elif nro > 99 and nro < 100:
        return '0' + str(nro)


filename = ""


def select_file1():
    global nueva
    global numeroprograma
    global contador
    global filename
    try:
        filetypes = (
            ('text files', '*.ch'),
            ("all files", "*.*")
        )
        numeroprograma = 0
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/ch-maquina',
            filetypes=filetypes,
        )
        numeroprograma += 1
        # crearBloquetabla(filename)
        file = open(filename, "r")
        lineas = file.readlines()
        # * Establesco el nombre del programa
        # ? Que debe pasar cuando se abren varios programas
        textPrograma.set(os.path.basename(filename))
        nueva = ""
        for ln in range(len(lineas)):
            if not lineas[ln].startswith("//"):
                nueva += lineas[ln]

        nueva = nueva.strip()
        nueva = nueva.split("\n")

        ctrl.agregar_variables(nueva)
        ctrl.checkeoSintaxis(nueva)
        print(ctrl.listErrores)
        areaDetrabajo()
        if len(ctrl.listErrores) == 0:
            messagebox.showinfo("Compilacion", "Programa sin errores listo para ser cargado")
        else:
            messagebox.showerror("Compilacion", "Programa Contiene errores")
        file.close()
    except:
        messagebox.showerror("Error de sintaxis", "Programa contiene errores")


def logicaChMaquina():
    global ACUMULADOR, e, result, instrucciones
    e = ''
    i = 0
    combo.set("User")
    while i < len(nueva):
        instrucciones = nueva[i].split(" ")
        while "" in instrucciones:
            instrucciones.remove("")
        print(f"linela {i} -> instruccion {instrucciones}")
        if instrucciones[0] == 'nueva':
            i += 1


        elif instrucciones[0] == 'cargue':
            llave = instrucciones[1]
            print(ctrl.listVariables.get(llave), "Tipo->", type(ctrl.listVariables.get(llave)['valor']))
            v = int(buscarVariable(instrucciones[1]))
            print("cargue variable en acumulaodr ", v)
            ACUMULADOR = v
            print("LE CARGO AL ACUMULADOR ", ACUMULADOR)
            i += 1


        elif instrucciones[0] == 'almacene':
            llave = instrucciones[1]
            print("llave", llave)
            ctrl.listVariables[llave]['valor'] = ACUMULADOR
            print(ctrl.listVariables[llave]['valor'])
            print(llave, f"->ALMACENE EN POS VARIABLE LO QUE HAY EN ACUMULADOR {ACUMULADOR} ",
                  ctrl.listVariables[llave]['valor'])

            print("Lista de variables", ctrl.listVariables)
            i += 1

        elif instrucciones[0] == 'reste':
            v = int(buscarVariable(instrucciones[1]))
            ACUMULADOR = ACUMULADOR - v
            print("RESTE->", ACUMULADOR)
            i += 1

        elif instrucciones[0] == 'sume':
            v = int(buscarVariable(instrucciones[1]))
            ACUMULADOR = ACUMULADOR + v
            print("AHORA SUME AC->", ACUMULADOR)
            i += 1

        elif instrucciones[0] == 'multiplique':
            v = int(buscarVariable(instrucciones[1]))
            ACUMULADOR = ACUMULADOR * v
            i += 1

        elif instrucciones[0] == 'muestre':
            v = buscarVariable(instrucciones[1])
            print("Salida por consola", v)
            listp.insert(1, v)
            i += 1


        elif instrucciones[0] == 'imprima':
            v = buscarVariable(instrucciones[1])
            print("Imprima Resultado", v)
            printerText.insert(1, f"{v}")
            i += 1
            ins.set(nueva[i])


        elif instrucciones[0] == 'vayasi':
            if ACUMULADOR > 0:
                print(ACUMULADOR, "> 0")
                i = int(asignarPosicionEtiquetas(contador)[0]) - 1
                print("i de 1", i)
            elif ACUMULADOR < 0:
                print(ACUMULADOR, "< 0")
                i = int(asignarPosicionEtiquetas(contador)[1]) - 1
                print("i de 2", i)
            else:
                i += 1
                ins.set(nueva[i])

        elif instrucciones[0] == 'etiqueta':
            i += 1

        elif instrucciones[0] == 'retorne':
            i += 1

        else:
            print("ENTRAMOS A ULTIMO ELSE")
            i += 1

        #instrucciones.clear()


# * Mapa que muestra la memeria principal del programa
# ! Faltan validaciones importantes
def mostrarMapa():
    global contador, ACUMULADOR
    vsb = ttk.Scrollbar(root, orient="vertical", command=tablaMemoria.yview)
    vsb.place(x=1380, y=30, height=700)
    memoriaInicial.set(ctrl.capacidadDefecto)
    tablaMemoria['columns'] = 'contenido'
    tablaMemoria.column("#0", width=120, anchor=CENTER)
    tablaMemoria.column("contenido", width=180, anchor=CENTER)

    tablaMemoria.heading("#0", text="Direcciona Memoria", anchor=CENTER, )
    tablaMemoria.heading("contenido", text="Contenido", anchor=CENTER)
    tablaMemoria.place(x=1100, y=20)
    tablaMemoria.configure(yscrollcommand=vsb.set)
    var = variables(nueva)
    d = ([i.split(",") for i in nueva])
    tablaMemoria.insert("", index=0, text="0000", values=["ACUMULADOR"])
    for j in range(1, 11):
        tablaMemoria.insert("", index=j, text=f"{j:04d}", values=["ch-maquina-2022"])
    for i, index in enumerate(d):
        tablaMemoria.insert("", index=11 + i, text=f"{i + 11:04d}", values=tuple(index))
    for m in range(len(listaDatosVariables())):
        print(listaDatosVariables()[m])
        tablaMemoria.insert("", index=contador - var + m, text=f"{contador - var + m:04d}",
                            values=listaDatosVariables()[m])
    contador += encontrarRetorno() + var


def listaDatosVariables():
    lista = []
    for i in ctrl.listVariables:
        val = (ctrl.listVariables[i]['valor'])
        lista.append(val)
    return lista


def buscarVariable(variable):
    for i in ctrl.listVariables:
        if variable in ctrl.listVariables.keys():
            return ctrl.listVariables[variable]['valor']


def areaDetrabajo():
    global contador
    var = variables(nueva)
    for i, pr in enumerate(nueva, contador):
        e = " ".join(pr.split())
        listaPrograma.insert(END, f"{i:04d} " f"{e}")

    registoBase = contador
    crearTablaEtiquetas(contador, encontrarEtiquetas(contador), asignarPosicionEtiquetas(contador))
    contador += encontrarRetorno() + var
    asignarPosiciones(contador)
    registroLc = contador - var - 1
    registroLimiteP = registroLc + var
    crearBloquetabla(filename, registroLc, registoBase, registroLimiteP)


def variables(p):
    global programa
    cantidad = 0
    for index, i in enumerate(p):
        # * e quita espacios
        e = " ".join(i.split())
        programa = e.split(" ")
        if programa[0].lower() == 'nueva':
            cantidad += 1
    return cantidad


def crearBloquetabla(filename, regLc, regBase, regLimteP):
    global numeroPrograma
    totalIns = totalInstrucciones(filename) + variables(nueva) - 1
    registroBs = regBase
    p = os.path.basename(filename)
    v = str(p)
    numero = nroProgamasCargados(numeroPrograma)
    tablaBloque.insert('', 'end', iid=None,
                       values=(numero, v, totalIns, registroBs, regLc, regLimteP))

    numeroPrograma += 1


def totalInstrucciones(archivo):
    # ? total de instruccione = + las variables que se deben crear
    return sum(1 for line in open(archivo))


def encontrarVariables():
    v = []
    for index, i in enumerate(nueva):
        global programa
        # * e quita espacios
        e = " ".join(i.split())
        programa = e.split(" ")
        if programa[0].lower() == 'nueva':
            v.append((programa[1]))
    return v


def getlistaVariables():
    v = []
    for index, i in enumerate(nueva):
        global programa
        e = " ".join(i.split())
        programa = e.split(" ")
        if programa[0].lower() == 'nueva':
            v.append((programa[1]))
    return v


def encontrarEtiquetas(c):
    etiquetas = []
    for index, i in enumerate(nueva, c):
        global programa
        e = " ".join(i.split())
        programa = e.split(" ")
        if programa[0].lower() == 'etiqueta':
            etiquetas.append(programa[1])

    return etiquetas


def asignarPosicionEtiquetas(c):
    etiquetas = []
    for index, i in enumerate(nueva, c):
        global programa
        e = " ".join(i.split())
        programa = e.split(" ")
        if programa[0].lower() == 'etiqueta':
            etiquetas.append(programa[2])

    return etiquetas


def crearTablaEtiquetas(c, etiquetas, nums):
    global numeroPrograma
    for i in range(len(etiquetas)):
        index = int(nums[i])
        listaEtiquetas.insert(END, f"{c + index - 1:04d}  "  f"{numeroPrograma:04d}" + f"{etiquetas[i]}")


def encontrarRetorno():
    for index, i in enumerate(nueva):
        global programa
        # * e quita espacios
        e = " ".join(i.split())
        programa = e.split(" ")
        if programa[0].lower() == 'retorne':
            return index + 1


def asignarPosiciones(c):
    lista01 = []
    final = c  # 34 # 57
    inicial = c - variables(nueva)  # 34 - 4 = 30 57 - 4 =
    while inicial < final:
        lista01.append(inicial)
        inicial += 1

    for d in zip(lista01, encontrarVariables()):
        listaVariables.insert(END, f" {d[0]:04d}   "   f"{numeroPrograma:04d}" + f"{d[1]}")


def asignarPosicionesMe(c):
    global lista01, posicionVariables
    lista01 = []
    final = c  # 34 # 57
    inicial = c - variables(nueva)  # 34 - 4 = 30 57 - 4 =
    while inicial < final:
        lista01.append(inicial)
        posicionVariables.append(inicial)
        inicial += 1
    return lista01


root.mainloop()
