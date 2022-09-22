# TODO: posiblemete se maneje el paso a paso que se debe generar
ids = []

from tkinter import filedialog as fd


def formatoIdentificacion():
    for _ in range(0, 999 + 1):
        ids.append(_)

    format01 = list(map(lambda x: str(x).zfill(4), ids))
    return format01


def tablaBloque(idso,programa, instrucciones, rb, rlc, rlp):
    for i in zip(idso,programa, instrucciones, rb, rlc, rlp):
        return i



def ejecutar(intruccion):
    pass
