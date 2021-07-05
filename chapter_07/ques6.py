n = int(input("Enter a number : "))
fac = 1

for i in range(1 , n+1):
    fac = i * fac
    i= i+1

print(fac)