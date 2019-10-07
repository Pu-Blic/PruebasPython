from tkinter import *
#Para no mostrar la ventana de la consola al ejecutar una ventana hay que cambiar la extensión del archivo a pyw

raiz = Tk() #Se crea un objeto ventana

raiz.title("Ventana de prueba")
raiz.resizable(True,True)
raiz.iconbitmap("icono.ico")
#raiz.geometry("1000x700") #anchoxalto. No se pone porque el raiz se adapta al tamaño del frame.
raiz.config(bg="cyan") #Pone el color de fondo azul

miFrame=Frame()
miFrame.pack(fill="both", expand="True") #Llena la ventana con el frame y permite su redimensionado
miFrame.config(bg="red", width="600", height="300") #Se pone el color de fondo y el ancho y alto. El raiz se adaptará al tamaño del frame
miFrame.config(cursor="hand2")
raiz.config(cursor="pirate")




raiz.mainloop() #el método hace que se ejecute constantemente