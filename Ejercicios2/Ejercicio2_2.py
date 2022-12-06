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