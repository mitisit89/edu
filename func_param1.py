x=int(input('Введите целое число :'));y=int(input('Введите целое число :'))
def printMax(a,b):
    if a>b:
        print(a,'max')
    elif a==b:
        print(a,'равно ',b)
    else:
        print(b,'Max')

printMax(x,y)
