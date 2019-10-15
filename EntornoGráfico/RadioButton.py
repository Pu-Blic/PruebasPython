from tkinter import *

root=Tk()

varOpcion = IntVar()

def Imprimir():
    if varOpcion.get()==1:
        lblResultado.config(text="Femenino")
    else:
        lblResultado.config(text="Masculino")
        

Radiobutton(root,text="Femenino", variable=varOpcion, value = 1, command=lambda:Imprimir()).pack()
Radiobutton(root,text="Masculino", variable=varOpcion, value = 2, command=lambda:Imprimir()).pack()

lblResultado=Label(root)
lblResultado.pack()

root.mainloop()