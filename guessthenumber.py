#!/usr/bin/env python3

# The random module is the one used to generate random numbers, useful inforation can be found at https://www.w3schools.com/python/module_random.asp
import random

# This variable stores the random number, the range is 1 to 10
number = random.randint(1, 10)


print("Guess the number game")
print("*********************")


player = input("Type the player name: ")

#This variable will count how many attempts the player took to guess the correct number
guess_number = 0
print("Hello " + player + " I am gessing a numer between 1 and 10")
print("There are 5 attempts to get it right or you lose")

while guess_number < 5:
    guess = int(input("Type the number you think is the correct: "))
    guess_number += 1
    if guess < number:
        print("Incorrect, your guess is too low")
    if guess > number:
        print("Incorrect, your guess is too high")
    if guess == number:
        print("Amazing, you know your path")
        break

if guess == number:
    print("Your guess is correct and it took you only " + str(guess_number) + " attempts to get it right")
else:
    print("You failed in guessing the number " + str(number))
    print("Good luck next one")

