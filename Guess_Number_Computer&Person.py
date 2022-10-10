import random

def user_guess(x):
    #This is the guessing game where you chose the computers number
    #x = input("You are now playing the guessing game. Select a number from 1 to ... that the computer will chose from and you will have to guess.")
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between one and {x}: '))
        if guess < random_number:
            print('Sorry, that was too low. Guess again.')
        elif guess > random_number:
            print("Sorry, that was too high. Guess again.")

    print("Congrats, you have guessed the computer's number {random_number} correctly!")

# user_guess(100)


# in this Rendition we will have the computer guess our Number

def computer_guess(x):
    low = 1
    high = x
    User_Feedback = ''
    while User_Feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high since low can equal high
        User_Feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)? ').lower()
        if User_Feedback == 'h':
            high = guess - 1
        elif User_Feedback == 'l':
            low = guess + 1
    print(f'Wow! The computer guessed your number, {guess}, correctly!')

computer_guess(1000)