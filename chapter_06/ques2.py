a = float(input("Enter no. 1 : "))
b = float(input("Enter no. 2 : "))
c = float(input("Enter no. 3 : "))

perc = (a+b+c/300)*100
ap = (a/100)*100
bp = (b/100)*100
cp = (c/100)*100

if(perc>=40.0 and ap>33 and bp>33 and cp>33 ):
    print("pass")
else:
    print("fail")