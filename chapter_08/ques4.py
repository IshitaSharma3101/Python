n = int(input("Enter a number : "))
s=0

def sum (n) :
    if(n<=1):
        return n
    else:
        s = n + sum(n-1)
        return s

print(sum(n))