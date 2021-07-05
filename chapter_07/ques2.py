l1 = ["Harry", "Soham", "Sachin", "Rahul"]

name = input('Enter name : ')

for name in l1:
    if name.startswith("S"):
        print('Hey, good morning ' + name)
    else:
        print("Name doesn't starts with S")