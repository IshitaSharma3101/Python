letter = '''Dear <|NAME|>,
You are selected.
<|DATE|>
'''

name = input("Enter name : ")
date = input("Enter date : ")

letter = letter.replace('<|NAME|>', name)
letter = letter.replace('<|DATE|>', date)

print(letter)