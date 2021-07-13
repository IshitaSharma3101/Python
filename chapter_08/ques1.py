n1 = int(input('Enter no.1 : '))
n2 = int(input('Enter no.2 : '))
n3 = int(input('Enter no.3 : '))

def greatest(a, b, c):
    if(a>b and a>c):
        print(f'{a} is the greatest number.')
    if(b>a and b>c):
        print(f'{b} is the greatest number.')
    else:
        print(f'{c} is the greatest number.')


greatest(n1, n2, n3)