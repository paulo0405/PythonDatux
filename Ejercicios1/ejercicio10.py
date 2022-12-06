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