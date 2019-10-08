from tkinter import *

root=Tk()
root.title="Calculadora"
#root.resizable(False, False)

miFrame=Frame(root)  #, width="600", height="400")
miFrame.pack()

NumeroPantalla=StringVar()

Operador1=0
Operador2=0
Operacion=""

#Pantalla de resultado
#columnspan hace que el widget ocupe tantas columnas como se le indica
txtResultado=Entry(miFrame, text="0", textvariable=NumeroPantalla, width="7", font=("Courier New",20), background="black", fg="#03f943", justify="right")
txtResultado.grid(row=1, column=1, padx=5, pady=5, sticky="e", columnspan=4)

def AñadirNumero(valor):
    NumeroPantalla.set(NumeroPantalla.get() + str(valor))

def DefinirOperacion(valor):
    global Operacion #Esto sirve para decir que tenga en cuenta que utilice la variable global del mismo nombre
    global Operador1 #Esto sirve para decir que tenga en cuenta que utilice la variable global del mismo nombre

    if valor=="+":
        Operacion = "sumar"
        Operador1=NumeroPantalla.get()
        NumeroPantalla.set("")
    elif valor=="-":
        Operacion = "restar"
        Operador1=NumeroPantalla.get()
        NumeroPantalla.set("")
    elif valor=="x":
        Operacion = "multiplicar"
        Operador1=NumeroPantalla.get()
        NumeroPantalla.set("")
    elif valor=="/":
        Operacion = "dividir"
        Operador1=NumeroPantalla.get()
        NumeroPantalla.set("")

def CalcularResultado(operacion):
    global Operacion #Esto sirve para decir que tenga en cuenta que utilice la variable global del mismo nombre
    global Operador1 #Esto sirve para decir que tenga en cuenta que utilice la variable global del mismo nombre
    global Operador2 #Esto sirve para decir que tenga en cuenta que utilice la variable global del mismo nombre

    Operador2=NumeroPantalla.get()
    if Operacion=="sumar":
        NumeroPantalla.set(float(Operador1)+float(Operador2))
    if Operacion=="restar":
        NumeroPantalla.set(float(Operador1)-float(Operador2))
    if Operacion=="multiplicar":
        NumeroPantalla.set(float(Operador1)*float(Operador2))
    if Operacion=="dividir":
        NumeroPantalla.set(float(Operador1)/float(Operador2))

#lambda hace que no se ejecute la llamada a la función hasta que se pulse el botón. Sio no se pone, automáticamente, se ejecuta la función y almacena el 
#resultado, con lo que al pulsar, no funciona y, además, pone el valor del botón en pantalla

#Botones de la fila 1
cmdBoton7=Button(miFrame, text="7", command=lambda:AñadirNumero("7"), width=3).grid(row=2, column=1)
cmdBoton8=Button(miFrame, text="8", command=lambda:AñadirNumero("8"), width=3).grid(row=2, column=2)
cmdBoton9=Button(miFrame, text="9", command=lambda:AñadirNumero("9"), width=3).grid(row=2, column=3)
cmdBotonDividir=Button(miFrame, text="/", command=lambda:DefinirOperacion("/"), width=3).grid(row=2, column=4)

#Botones de la fila 2
cmdBoton4=Button(miFrame, text="4", command=lambda:AñadirNumero("4"), width=3).grid(row=3, column=1)
cmdBoton5=Button(miFrame, text="5", command=lambda:AñadirNumero("5"), width=3).grid(row=3, column=2)
cmdBoton6=Button(miFrame, text="6", command=lambda:AñadirNumero("6"), width=3).grid(row=3, column=3)
cmdBotonMultiplicar=Button(miFrame, text="x", command=lambda:DefinirOperacion("x"), width=3).grid(row=3, column=4)


#Botones de la fila 3
cmdBoton1=Button(miFrame, text="1", command=lambda:AñadirNumero("1"), width=3).grid(row=4, column=1)
cmdBoton2=Button(miFrame, text="2", command=lambda:AñadirNumero("2"), width=3).grid(row=4, column=2)
cmdBoton3=Button(miFrame, text="3", command=lambda:AñadirNumero("3"), width=3).grid(row=4, column=3)
cmdBotonRestar=Button(miFrame, text="-", command=lambda:DefinirOperacion("-"), width=3).grid(row=4, column=4)

#Botones de la fila 4
cmdBoton0=Button(miFrame, text="0", command=lambda:AñadirNumero("0"), width=3).grid(row=5, column=1)
cmdBotonComa=Button(miFrame, text=",", width=3).grid(row=5, column=2)
cmdBotonResultado=Button(miFrame, text="=", command=lambda:CalcularResultado(Operacion), width=3).grid(row=5, column=3)
cmdBotonSumar=Button(miFrame, text="+", command=lambda:DefinirOperacion("+"), width=3).grid(row=5, column=4)





root.mainloop()
