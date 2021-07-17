import random

you = input("Your turn : Snake(s) or Water(w) or Gun(g) : ")

randomNo = random.randint(1,3)
if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'

def winner(comp, you):
    if comp == you :
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

result = winner(comp, you)

if result == None:
    print("It's a tie.")
elif result:
    print("You win.")
else:
    print("You lose.")
