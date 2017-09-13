guess = -1
count = 0
x = 72
while guess != x :
    count += 1
    guess = int(input())
    if not 0<=guess<=100:
        print("Sorry, your guess is out of range.")
    elif guess<x:
        print("Sorry, your guess is too low.")
    elif guess>x:
        print("Sorry, your guess is too high.")
    else:
        print("Congratulations, your guess is correct. Total number of guesses is {}.".format(count))
