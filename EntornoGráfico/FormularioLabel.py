from tkinter import *

root=Tk()
miFrame=Frame(root, width="600", height="400")
miFrame.pack()

miLabel=Label()
miLabel.place(x=5,y=5) #Se una place en lugar de pack para que no redimensione el Frame y la ventana al tamaño del Label
miLabel.config(text="Nombre: ")
txtNombre = Entry(miFrame) #Entry es como se llaman a los cuadrod de texto en Python
txtNombre.place(x=60, y=5)


#Otra forma de crear una etiqueta
Label(miFrame, text="Apellidos: ", fg="blue", bg="yellow", font=("Comic Sans MS",14)).place(x=5, y=30)
txtApellidos=Entry(miFrame)
txtApellidos.place(x=100,y=30)


Label(miFrame, text="Edad: ", fg="red", bg="black").place(x=5, y=70)
txtEdad=Entry(miFrame)
txtEdad.place(x=50,y=70)
#txtEdad.grid(row=2, column=2)



imagen=PhotoImage(file="gracias.gif")
miLabel=Label(miFrame, image=imagen). place(x=5, y=100)

root.mainloop()