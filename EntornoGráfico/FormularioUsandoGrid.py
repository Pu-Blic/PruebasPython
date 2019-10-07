from tkinter import *

root=Tk()
root.title="Ventana Uno"

miFrame=Frame(root, width="600", height="400")
miFrame.pack()

Label(miFrame, text="Nombre:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
Label(miFrame, text="Apellidos:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
Label(miFrame, text="Password:").grid(row=2, column=0, padx=5, pady=2, sticky="w")
Label(miFrame, text="Edad:").grid(row=3, column=0, padx=5, pady=2, sticky="w")

txtNombre=Entry(miFrame).grid(row=0, column=1, padx=5, pady=2, sticky="w")
txtApellidos =Entry(miFrame).grid(row=1, column=1, padx=5, pady=2, sticky="w")
txtPassword=Entry(miFrame, fg="red", show="*").grid(row=2, column=1, padx=5, pady=2, sticky="w")
txtEdad=Entry(miFrame).grid(row=3, column=1, padx=5, pady=2, sticky="w")

Label(miFrame, text="Observaciones:").grid(row=4, column=0, padx=5, pady=5, sticky="w")

miScrollY= Scrollbar(miFrame)
miScrollY.grid(row=4, column=1, pady=5, sticky="nsew")
txtObservaciones=Text(miFrame, width=15, height=5, yscrollcommand=miScrollY.set).grid(row=4, column=1, padx=5, pady=5, sticky="w") #Text es un Entry, pero de más capacidad.
txtObservaciones.config(command=txtObservaciones.yview)

#scrollbar = Scrollbar(miFrame)
#scrollbar.grid(row=4, column=1, pady=5, sticky="nse")
#txtObservaciones = Text(miFrame, yscrollcommand = scrollbar.set)
#txtObservaciones.grid(row=4, column=0).grid(row=4, column=1, padx=5, pady=5, sticky="w")
#scrollbar.config( command = txtObservaciones.yview )

Minuto 11 del víeo

root.mainloop()