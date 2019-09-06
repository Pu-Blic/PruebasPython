def ComprobarEmailCorrecto(direccion):
    j=0

    for i in direccion:
        if i=="@" or i==".":
            j=j+1
            if j==2:
                break;
    else:
        return False

    return True

    #if j==2:            
    #    return True
    #else:
    #    return False


correo=input("Introduce tu correo electrónico: ")
if (ComprobarEmailCorrecto(correo))==True:
    print("El correo es correcto.")
else:
    print("La dirección de correo no es correcta")

# Voy por aquí en el curso https://www.youtube.com/watch?v=TLVnoqXGWpY&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=19
