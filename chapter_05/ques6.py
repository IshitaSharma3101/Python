d = {}
jhalak = input("Enter a language jhalak : ")
hardik = input("Enter a language hardik : ")
shrishti = input("Enter a language shrishti : ")
tushar = input("Enter a language tushar : ")

newD = {
    "jhalak":jhalak,
    "hardik":hardik,
    "shrishti":shrishti,
    "tushar":tushar
}

# d.update({"jhalak":jhalak})
# d.update({"hardik":hardik})
# d.update({"shrishti":shrishti})
# d.update({"tushar":tushar})

d.update(newD)


print(d)
