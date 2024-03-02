import random
# 1. Name:
#      Luke Marshall
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      It is meant to take an integer from the user and creat an array and pick a random number which the user will guess to get.
# 4. What was the hardest part? Be as specific as possible.
#      The Hardest part about this assignment was having to create the Guesses array. I didnt know how to do that. I had to search and look into python code to figure out how to append the information into it.
# 5. How long did it take for you to complete the assignment?
#      4 hours total

#do the initial printing
print ('\nThis is the "guess a number game".\nYou try to guess a random number in the smallest number of attempts.')

#collect all information needed
Number = int(input("\nPlease input a positive integer: "))

Number_array = [i for i in range(1, Number + 1)]

#make random selection
secret_num = random.choice (Number_array)

guesses = []
num_guesses = 0

while True:
    Guess = int(input(f"\nPlease guess a number from 1 to {Number}: "))
    guesses.append(Guess)  # Add the guess to the array
    num_guesses += 1  # Increment the number of guesses
       
    if Guess == secret_num:
        print (f"\nCongratulations you have guessed the number!\n it took you {num_guesses} guesses to beat the game")
        break
    elif Guess > secret_num:
        print ("\n\tToo High!")
    elif Guess < secret_num:
        print("\n\t Too Low!")
    else:
        print("\nInvalid option try again")
