variable="contraseña"
ingreso=input("¿Cuál es su contraseña? ")
ingresocorregido=ingreso.lower()
if variable==ingresocorregido:
    print("La contraseña introducida coincide correctamente con la contraseña guardada.")
else:
    print("La contraseña introducida no coincide con la contraseña guardada")