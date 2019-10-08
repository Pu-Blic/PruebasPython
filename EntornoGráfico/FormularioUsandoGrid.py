from tkinter import *

root=Tk()
root.title="Ventana Uno"

miNombre=StringVar()   #Creo una variable de tipo string. Será asociada al Entry txtNombre


miFrame=Frame(root, width="600", height="400")
miFrame.pack()

Label(miFrame, text="Nombre:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
Label(miFrame, text="Apellidos:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
Label(miFrame, text="Password:").grid(row=2, column=0, padx=5, pady=2, sticky="w")
Label(miFrame, text="Edad:").grid(row=3, column=0, padx=5, pady=2, sticky="w")

txtNombre=Entry(miFrame, textvariable=miNombre).grid(row=0, column=1, padx=5, pady=2, sticky="w")
txtApellidos =Entry(miFrame).grid(row=1, column=1, padx=5, pady=2, sticky="w")
txtPassword=Entry(miFrame, fg="red", show="*").grid(row=2, column=1, padx=5, pady=2, sticky="w")
txtEdad=Entry(miFrame).grid(row=3, column=1, padx=5, pady=2, sticky="w")

Label(miFrame, text="Observaciones:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
txtObsrvaciones=Text(miFrame, width=15, height=5).grid(row=4, column=1, padx=5, pady=5, sticky="w")

def CodigoBoton():
    miNombre.set("Public")
    

cmdAceptar=Button(miFrame, width=10, text="Aceptar", command=CodigoBoton).grid(row=5,column=1, padx=5, pady =5)






root.mainloop()