l=int(input('¿Cuántos números quiere ingresar? '))
p=[]
for i in range(l):
    o=int(input('Ingrese número: '))
    p.append(o)
    if p[i]%2==0:
        print(f'{p[i]} es múltiplo de dos.')
print(f'Su lista de números es \n {p}')