import random
randomNum = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randomNum):
    userGuess = int(input("Enter a number : "))
    guesses += 1
    if(userGuess == randomNum):
        print("Yay! You guessed it right!")
    else:
        if(userGuess>randomNum):
            print("Enter a smaller number")
        else:
            print("Enter a larger number")

print(f"You guessed the correct answer in {guesses} times")