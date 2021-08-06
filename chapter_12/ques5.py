n = int(input("Enter a number : "))

l = [n*i for i in range(1,11)]
print(l)

with open("tables.py", 'a') as f:
    f.write(str(l))
    f.write("\n")