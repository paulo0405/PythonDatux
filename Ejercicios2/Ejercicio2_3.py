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