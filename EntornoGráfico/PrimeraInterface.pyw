from tkinter import *
#Para no mostrar la ventana de la consola al ejecutar una ventana hay que cambiar la extensión del archivo a pyw


raiz = Tk() #Se crea un objeto t

raiz.title("Ventana de prueba")
raiz.resizable(True,True)
raiz.iconbitmap("icono.ico")
raiz.geometry("1000x700") #anchoxalto
raiz.config(bg="cyan") #Pone el color de fondo azul

raiz.mainloop() #el método hace que se ejecute constantemente