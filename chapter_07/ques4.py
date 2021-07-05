n = int(input("Enter a number : "))
prime=True

for i in range(2, n):
    if(n%i==0):
        prime = False
        break

if prime:
    print("It is prime")
else:
    print("Its is not prime")