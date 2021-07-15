string = input("Enter a string : ")
word = input("Enter a word : ")

def ans(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

print(ans(string, word))