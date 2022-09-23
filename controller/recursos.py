"""import tkinter as tk
import random


def actualizar_etiqueta():
    numero_aleatorio = random.randint(1, 100)
    etiqueta1.config(text=f"Número aleatorio: {numero_aleatorio}")


ventana = tk.Tk()
ventana.title("Ejemplo after() en Tk")
ventana.config(width=400, height=300)
etiqueta1 = tk.Label(text="¡Hola mundo!")
etiqueta1.place(x=100, y=70)
ventana.after(2000, actualizar_etiqueta)


ventana.mainloop()"""

lista = [1, 2, 3, 4, 5, 6, 8, 8, 10]
i = 0
for i, index in enumerate(lista, i):
    if i == 3:
        i = 5
    print(i)
    i += 1

for i in range(len(lista)):
    if i == 3:
        i = 2
    print(lista[i])
