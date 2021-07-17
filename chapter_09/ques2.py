def game():
    return 667678

score = game()

with open('hiScore.txt') as f:
    oldScore = int(f.read())

if score>oldScore :
    with open('hiScore.txt', 'w') as f:
        hiScore = f.write(str(score))