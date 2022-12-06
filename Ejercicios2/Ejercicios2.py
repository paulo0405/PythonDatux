#Ejercicio 1
l=int(input('¿Cuántos números quiere ingresar? '))
p=[]
for i in range(l):
    o=int(input('Ingrese número: '))
    p.append(o)
    if p[i]%2==0:
        print(f'{p[i]} es múltiplo de dos.')
print(f'Su lista de números es \n {p}')

#Ejercicio 2
f=int(input('¿De cuántos asteríscos de lado quiere su cuadrado? '))
for i in range(f):
    if i==0 or i==f-1:
        for j in range(f):
            print('*',end='')
        print('\n',end='')
    else:
        print('*',end='')
        for j in range(f-2):
            print(' ',end='')
        print('*\n',end='')

#Ejercicio 3
f=int(input('¿De cuántos asteríscos de base quiere su triángulo? '))
t=round(f/2+0.1)
k=t
for i in range(t):
    if i==t-1:
        for j in range(f):
            print('*',end='')
        print('\n',end='')
    else:
        if f%2==0:
            for j in range(f):
                if j==k-1:
                    print('*',end='')
                elif j==f-k:
                    print('*',end='')
                else:
                    print(' ', end='')
        else:
            for j in range(f):
                if j==k-1:
                    print('*',end='')
                elif j==f-k:
                    print('*',end='')
                else:
                    print(' ', end='')
        print('\n', end='')
    k-=1