#Ejercicio 1
nombre=input("¿Cuál es su nombre? ")
sexo=input("¿Es hombre o mujer? ")
direccion=input("¿Dónde vive? ")
telefono=input("Ingrese su número telefónico: ")
correo=input("Ingrese su Correo electrónico: ")
print("\nMuchas gracias por indicar sus datos\n" f"Usted {nombre}, es {sexo} y reside en {direccion}.\nCualquier comunicacion con usted lo contactaremos a su número {telefono} o le escribiremos a su correo {correo}.")

#Ejercicio 2
radio=float(input("Ingrese el radio de su círculo en cm: "))
print(f"El área de su círculo es {3.14*(radio**2)} cm2.")

#Ejercicio 3
a=float(input("Ingrese su primer valor: "))
b=float(input("Ahora su segundo valor: "))
c=float(input("Y finalmente su tercer valor: "))
print(f"\nEl resultado de la suma es: {a+b+c}.",f"\nEl resultado de la resta es: {a-b-c}",f"\nEl resultado de la multiplicación es: {a*b*c}")

#Ejercicio 4
valor=int(input("Ingrese su variable: "))
print(type(valor))

#Ejercicio 5
import sys
variable =sys.argv[0]
print(f"{variable}")

#Ejercicio 6
maximo=int(input("Ingrese hasta que número desea sumar: "))
suma=0
for i in range(maximo+1):
    suma+=i
print("La suma consecutiva resulta ser:",f"{suma}")

#Ejercicio 7
a=int(input("Ingre tu primer número: "))
b=int(input("Ahora el segundo: "))
if a==b:
    print("Los números son iguales.")
else:
    print("Los números son diferentes.")
if a>b:
    print("Y el primer número es mayor que el segundo.")
else:
    print("Y el segundo número es mayor o igual que el primero")

#Ejercicio 8
variable="contraseña"
ingreso=input("¿Cuál es su contraseña? ")
ingresocorregido=ingreso.lower()
if variable==ingresocorregido:
    print("La contraseña introducida coincide correctamente con la contraseña guardada.")
else:
    print("La contraseña introducida no coincide con la contraseña guardada")

#Ejercicio 9
num=int(input("Ingrese su número: "))
if num%2==0:
    print("El número ingresado es par.")
else:
    print("El número ingesado es impar.")

#Ejercicio 10
deuda=float(input("Ingresar su deuda a pagar: "))
días=int(input("¿Cuántos días está tardando en pagar? "))
if 1<=días<=10:
    print(f"Entonces deberá pagar extra de penalidad {round(deuda*0.05,2)}")
elif 10<días<=30:
    print(f"Entonces deberá pagar extra de penalidad {round(deuda*0.08,2)}")
elif 30<días:
    print(f"Entonces deberá pagar extra de penalidad {round(deuda*0.1,2)}")
else:
    print("Entonces no está atrasado en su deuda")

#Ejercicio 11
a=int(input("Ingrese su primer número: "))
b=int(input("Ahora ingrese su segundo número: "))
i=0
while i==0:
    i=i+1
    oper=input("¿Qué operación desea realizar: sumar, restar o multiplicar?  ")
    oper_c=oper.lower()
    if oper_c=="sumar":
        print(f"El resultado de la suma es {a+b}")
    elif oper_c=="restar":
        print(f"El resultado de la resta es {a-b}")
    elif oper_c=="multiplicar":
        print(f"El resultado de la multiplicación es {a*b}")
    else:
        i=i-1
        print("Ingreso una operacion invalida. Asegurese escribir correctamente las palabras clave tal y como estan en la pregunta.")

#Ejercicio 12
letra=input("Ingrese su caracter: ")
l=len(letra)
if l==1:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print("El caracter ingresado es una vocal.")
    else:
        print("Lo que ingreso no es una vocal.")
else:
    print("Solamente debe ingresar un caracter. No se puede procesar la cadena ingresada.")

#Ejercicio 13
estudiantes=["ab","bc","cd","de","ef"]
lugar={1:"primer",2:"segundo",3:"tercer",4:"cuarto",5:"quinto"}
for i in range(5):
    estudiantes[i]=input(f"Ingrese el {lugar[i+1]} estudiante: ")
print(f"La lista tiene {len(estudiantes)} elementos.")
print(f"Su último elemento es {estudiantes[len(estudiantes)-1]}")
estudiantes.reverse()
print(f"Al invertir el orden de estudiantes tenemos:\n {estudiantes} ")

#Ejercicio 14
okaloka={"rojo":"congelado","azul":"saltar","verde":"correr","amarillo":"estirarse"}
print(okaloka)
okaloka["amarillo"]=input("¿Qué acción quieres que sea amarillo? ")
print(okaloka)