x=int(input('Введите чило: '))
n=int(input('Введите степень числа: '))

def req(x,n):
    if n>1:
        return x*req(x,n-1)
    elif n<-1:
        return 1/x*req(x,n+1)
    elif n==-1:
        return 1/x
    elif n==0:
        return 1
    else:
        return x

print(req(x,n))
