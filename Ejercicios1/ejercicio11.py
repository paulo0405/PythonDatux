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
