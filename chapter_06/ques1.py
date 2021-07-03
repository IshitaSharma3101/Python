a = int(input("Enter no. 1 : "))
b = int(input("Enter no. 2 : "))
c = int(input("Enter no. 3 : "))
d = int(input("Enter no. 4 : "))

if(a>b and a>c):
    print("a is the greatest")
elif(b>a and b>c):
    print("b is the greatest")
elif(c>a and c>b):
    print("c is the greatest")
else:
    print("d is the greatest")