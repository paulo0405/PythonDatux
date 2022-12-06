class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    def __str__(self):
        return 'El producto es {} y cuesta {}'.format(self.nombre, self.precio)

class Catalogo:
    listaProducto=[]
    def __init__(self,nombre):
        self.nombre=nombre
    def __str__(self) :
        return 'Está viendo el catalogo de {}'.format(self.nombre)
    def agregar(self,p):
        self.listaProducto.append(p)
    def mostrar(self):
        for i in self.listaProducto:
            print(i)

c1=Catalogo('Vehiculos')
print(c1)
p1=Producto('Mustang',30000)
print(p1)
p2=Producto('Toyota',40000)
p3=Producto('Mitsubishi',25000)
c1.agregar(p1)
c1.agregar(p2)
c1.agregar(p3)
c1.mostrar()