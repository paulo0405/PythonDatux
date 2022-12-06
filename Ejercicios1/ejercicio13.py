estudiantes=["ab","bc","cd","de","ef"]
lugar={1:"primer",2:"segundo",3:"tercer",4:"cuarto",5:"quinto"}
for i in range(5):
    estudiantes[i]=input(f"Ingrese el {lugar[i+1]} estudiante: ")
print(f"La lista tiene {len(estudiantes)} elementos.")
print(f"Su último elemento es {estudiantes[len(estudiantes)-1]}")
estudiantes.reverse()
print(f"Al invertir el orden de estudiantes tenemos:\n {estudiantes} ")