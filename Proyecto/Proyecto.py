from tkinter import *
from Consulta import *

mywindow=Tk()
mywindow.geometry("700x620")
mywindow.title("Formulario de Consultas Médicas")
mywindow.resizable (False,False)
mywindow.config(background="#213141")
main_title=Label(text="Consultas médicas", font=("Arial",14), bg="#56CD63", fg="white", width="620", height="2")
main_title.pack()

cuadrodenombres=Label(text="Nombres", bg="#FFEEDD")
cuadrodenombres.place(x=24, y=74)
cuadrodeapeliidos=Label(text="Apellidos", bg="#FFEEDD")
cuadrodeapeliidos.place(x=24, y=104)
cuadrodeDNI=Label(text="DNI", bg="#FFEEDD")
cuadrodeDNI.place(x=24, y=134)
cuadrodeedad=Label(text="Edad", bg="#FFEEDD")
cuadrodeedad.place(x=24, y=164)
cuadrodecelular=Label(text="Celular", bg="#FFEEDD")
cuadrodecelular.place(x=24, y=194)
cuadrodecorreo=Label(text="Correo", bg="#FFEEDD")
cuadrodecorreo.place(x=24, y=224)
cuadroderazón=Label(text="Razón de la Consulta", bg="#FFEEDD")
cuadroderazón.place(x=24, y=274)


nombres=StringVar()
apellidos=StringVar()
DNI=IntVar()
edad=IntVar()
celular=IntVar()
correo=StringVar()
razón=StringVar()
texto=StringVar()

entradadenombres = Entry(textvariable=nombres, width="22")
entradadeapellidos = Entry(textvariable=apellidos, width="22")
entradadeDNI = Entry(textvariable=DNI, width="22")
entradadeedad = Entry(textvariable=edad, width="22")
entradadecelular = Entry(textvariable=celular, width="22")
entradadecorreo = Entry(textvariable=correo, width="22")
entradaderazón = Entry(textvariable=razón, width="40")

entradadenombres.place(x=144,y=74)
entradadeapellidos.place(x=144,y=104)
entradadeDNI.place(x=144,y=134)
entradadeedad.place(x=144,y=164)
entradadecelular.place(x=144,y=194)
entradadecorreo.place(x=144,y=224)
entradaderazón.place(x=24,y=304)
listadeconsultas=[]
def guardar():
    n=nombres.get()
    a=apellidos.get()
    d=DNI.get()
    e=edad.get()
    c=celular.get()
    co=correo.get()
    r=razón.get()
    p=consulta(n,a,d,e,c,co,r)
    texto.set(p)
    listadeconsultas.append(p)
    print(p)
cuadrodeguardado=Label(textvariable=texto, bg="#FFEEDD", width=50)
cuadrodeguardado.place(x=324, y=74)
def borrar():
    del listadeconsultas[:]
    print("Se borró la lista de consultas guardadas")
botonGuardar=Button(mywindow,text="Guardar",command=guardar, width="20", height="2", bg="#00CD63")
botonBorrar=Button(mywindow,text="Hacer nueva lista",command=borrar, width="20", height="2", bg="#00CD63")
botonGuardar.place(x=24, y=344)
botonBorrar.place(x=202, y=344)

mywindow.mainloop()