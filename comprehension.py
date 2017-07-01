# It's a guessing-game, in which the computer "think" of a number between 1 and 20, and the player has 5 round to guess it.
import random  # import random module

guessesTaken = 0  # assign 0 to integer type variable named guessesTaken

print('Hello! What is your name?')  # print out the string inside parentheses to console
myName = input()  # Prompt the user for input and assign it to myName variable (which type will be string)

number = random.randint(1, 20)  # assign a pseudo random integer between 1 and 20 (inclusive) to number variable using the randint function of random module

print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # print the text in parentheses to console, including myName variable

while guessesTaken < 6:  # repeat the indented code below while the guessesTaken variable is lower than 6
    print('Take a guess.')  # print the string in parentheses to console
    guess = input()  # prompt the user for input and assign it to the guess variable
    guess = int(guess)  # cast(convert) the value of guess variable to integer

    guessesTaken += 1  # increase the value of guessesTaken by 1

    if guess < number:  # execute the indented code below if guess variable is lower than number variable
        print('Your guess is too low.')  # print out the string inside the parentheses to console

    if guess > number:  # execute the indented code below if guess variable is higher than number variable
        print('Your guess is too high.')  # print out the string inside the parentheses to console

    if guess == number:  # execute the indented code below if guess variable is equal to number variable
        break  # terminate the while loop

if guess == number:  # execute the indented code below if guess variable is equal to number variable
    guessesTaken = str(guessesTaken)  # reassign the guessesTaken variable with its string-type equivalent
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # print the string in parentheses, including myName and guessesTaken variable to console

if guess != number:  # execute the indented code below if guess variable is not equal to number variable
    number = str(number)  # reassign the number variable with its string-type equivalent
    print('Nope. The number I was thinking of was ' + number)  # print the string in parentheses including number variable to console
