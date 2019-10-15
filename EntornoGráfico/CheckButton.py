from tkinter import *

root=Tk()

playa = IntVar()
montaña=IntVar()
luna=IntVar()
OpcionEscogida=StringVar()


def OpcionesViaje():
    global OpcionEscogida

    OpcionEscogida.set("")

    if playa.get()==1:
        OpcionEscogida.set(OpcionEscogida.get() + " playa")

    if montaña.get()==1:
        OpcionEscogida.set(OpcionEscogida.get() + " montaña")

    if luna.get()==1:
        OpcionEscogida.set(OpcionEscogida.get() + " luna")
    

Label(root,text="Elige el destino")

chkPlaya = Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=lambda:OpcionesViaje()).pack()
chkMontaña = Checkbutton(root, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=lambda:OpcionesViaje()).pack()
chkLuna = Checkbutton(root, text="Luna", variable=luna, onvalue=1, offvalue=0, command=lambda:OpcionesViaje()).pack()

lblResultado=Label(root, textvariable=OpcionEscogida).pack()

root.mainloop()
