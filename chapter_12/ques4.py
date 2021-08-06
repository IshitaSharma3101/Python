a = int(input("Enter a : "))
b = int(input("Enter b : "))

try:
    print(f"{a}/{b} = {a/b}")
except ZeroDivisionError:
    print("Infinite")