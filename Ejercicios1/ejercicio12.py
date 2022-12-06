letra=input("Ingrese su caracter: ")
l=len(letra)
if l==1:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print("El caracter ingresado es una vocal.")
    else:
        print("Lo que ingreso no es una vocal.")
else:
    print("Solamente debe ingresar un caracter. No se puede procesar la cadena ingresada.")