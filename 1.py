def perevod(a, ss):
    n=''
    while a>0:
        n= str(a%ss)+ n
        a//=ss
    return n

def drob(b, ss):
    while b>1:
        b/=10
    n=''

    for i in range(23):
        b*=ss
        n+= str(int(b))
        if int(b)>0:
            b-=int(b)
    return '.'+n
    
    
a= (input('Введите число: '))
ss= int(input('Введите целевую систему счисления: '))
if '.' in a or ',' in a:
    cel, ost= a.split('.')
    celoe=perevod(int(cel), ss)
    drobnoe=drob(int(ost), ss)
    n=celoe+ drobnoe
    print('Вывод:', a, '->',n)
else:
    n=perevod(int(a),ss)
    print('Вывод:', a, '->',n)