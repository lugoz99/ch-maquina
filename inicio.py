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
import controller.chmaquina as ctrl
from pathlib import Path
import controller.ejecucion as ejecucion
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import ttk
import os
from tkinter import font

nueva = ""

root = Tk()
memoriaInicial = IntVar()
contador = 0
numeroPrograma = 0
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
menuBar.add_cascade(label="Ejecute", menu=ejecute)

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
labelMemroia = LabelFrame(frameProceador, width=250, height=50, relief=SUNKEN)
labelMemroia.grid(row=0, column=1, sticky="ns")
labelMemroia.grid_propagate(False)
labeM = Label(labelMemroia, text="Memoria", width=10)
labeM.grid(row=0, column=0, pady=5)
labeK = Label(labelMemroia, text="Kernel", width=10)
labeK.grid(row=1, column=0, pady=10)
frameProceador.grid_propagate(False)
# * Memoria

spM = Spinbox(labelMemroia, from_=0, to=50, width=10, wrap=True)
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

etiqueta1 = Label(frameAcumulador, text="Acumulador")
etiqueta1.place(x=5, y=5)
acumulador = ttk.Entry(frameAcumulador, justify=CENTER, width=15, state="readonly")
acumulador.place(x=104, y=5)

etiqueta2 = Label(frameAcumulador, text="PC")
etiqueta2.place(x=5, y=65)
pc = ttk.Entry(frameAcumulador, justify=CENTER, width=22, state="readonly")
pc.place(x=40, y=65, anchor=NW)

programa = ttk.Entry(frameAcumulador, justify=CENTER, width=26, state="readonly")
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
listp.insert(1, "1")
listp.insert(2, "2")
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

comboExample = ttk.Combobox(framePCImpresora,
                            values=[
                                "User",
                                "Kernel"], state="read", width=10)
comboExample.place(x=120, y=240)
# *-------------------------------TEXTO IMPRESORA--------------------------
printerText = Text(framePCImpresora, width=20, height=20)
printerText.place(y=450, x=100)
printerText.insert('1.0', 'This is a Text widget demo')

printerText.configure(state="disabled")
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


def mostrarMapa():
    vsb = ttk.Scrollbar(root, orient="vertical", command=tablaMemoria.yview)
    vsb.place(x=1380, y=30, height=700)
    memoriaInicial.set(ctrl.capacidadDefecto)
    tablaMemoria['columns'] = 'contenido'
    tablaMemoria.column("#0", width=120, anchor=CENTER)
    tablaMemoria.column("contenido", width=180, anchor=CENTER)

    tablaMemoria.heading("#0", text="Direcciona Memoria", anchor=CENTER, )
    tablaMemoria.heading("contenido", text="Contenido", anchor=CENTER)
    tablaMemoria.place(x=1100, y=20)
    for i in range(0, 999):
        var = f"{i:04d}"
        if i == 0:
            tablaMemoria.insert("", END, text="0000", values=[5])
        if i >= 1 and i < 10:
            print("se cumple")
            tablaMemoria.insert("", END, text=var, values=["CHMAQUINA2022"])
        if i >= 10:
            print(var)
            print("se cumple esta")
            tablaMemoria.insert("", END, text=var, values=("sin contenido", ""))
    # height=800
    tablaMemoria.configure(yscrollcommand=vsb.set)


def tamListaPrograma():
    return listaPrograma.size() > 0


# root.resizable(width=False, height=False)
def select_file():
    global nueva
    filetypes = (
        ('text files', '*.ch'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/ch-maquina',
        filetypes=filetypes,
    )

    # nueva = nueva.split("\n")
    nueva = ctrl.leerPrograma(filename)
    index = None
    c = -1
    for i, p in enumerate(nueva, 11):
        index = f"{i:04d}"
        listaPrograma.insert(END, f"{index}  {p}")
        # ? validacion pertinentes para cargar a memoria principal

    ctrl.operacion(nueva, index)
    p = os.path.basename(filename)
    v = str(p)
    limite = registroLoc(nueva) + 1
    print("cantidad : ", ctrl.programasCantidad())
    vl = ejecucion.tablaBloque([v], [101], [102], [limite], [24])
    tablaBloque.insert('', 'end', iid=None,
                       values=(f"{c:04d}", vl[1], "INS", "RB", vl[4], "S"))


def nroProgamasCargados(nro):
    if nro < 10:
        return ('000' + str(nro))
    elif nro > 9 and nro < 100:
        return '00' + str(nro)
    elif (nro > 99 and nro < 100):
        return '0' + str(nro)


def select_file1():
    global nueva
    global numeroprograma
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
    print("aqui se llama a numero de programama si  o no", numeroPrograma)
    # crearBloquetabla(filename)
    file = open(filename, "r")
    lineas = file.readlines()

    nueva = ""
    for ln in range(len(lineas)):
        if not lineas[ln].startswith("//"):
            nueva += lineas[ln]

    nueva = nueva.strip()
    nueva = nueva.split("\n")
    rglc = registroLoc(nueva)
    crearBloquetabla(filename, rglc)
    file.close()
    kernel = textFinal.get() + 1
    programas = 11
    for i, pr in enumerate(nueva, programas + listaPrograma.size()):
        e = " ".join(pr.split())
        index = f"{i:04d}"
        listaPrograma.insert(END, f"{index}  {e}")
        programas = programas + 1
    # print("ejecucion : ", ejecucion.formatoIdentificacion(getContador()))


def crearBloquetabla(filename, regLc, regBase=""):
    global archivos, numeroPrograma
    total = totalInstrucciones(filename)
    p = os.path.basename(filename)
    v = str(p)
    # vl = ejecucion.tablaBloque([v], [101], [102], [limite], [24])
    print("numero de programa", numeroPrograma)
    numero = nroProgamasCargados(numeroPrograma)
    print("Numero", numero)
    tablaBloque.insert('', 'end', iid=None,
                       values=(numero, v, total, "RB", regLc, "RLP"))

    numeroPrograma += 1


def registroLoc(n):
    for index, i in enumerate(n, textFinal.get() + 1):
        p = i.split(" ")
        if p[0] == 'retorne':
            return index


def totalInstrucciones(archivo):
    # ? total de instruccione = + las variables que se deben crear
    num_lines = sum(1 for line in open(archivo))
    return num_lines


print(tablaBloque.size())
root.mainloop()
