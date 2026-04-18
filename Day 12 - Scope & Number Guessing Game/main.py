# Day 12 - Scope & Number Guessing Game
# Topics: namespaces, scope, block scope, global vars, local constants


# ----------------------------------------------------------
# 1. Local Scope
# Variables defined inside a function are local to that function
# ----------------------------------------------------------

def drink_potion():
    """Demonstrates local scope."""
    potion_strength = 2
    print(f"Potion strength (local): {potion_strength}")


drink_potion()
# print(potion_strength)  # NameError: not defined outside function


# ----------------------------------------------------------
# 2. Global Scope
# Variables defined at the top level are accessible everywhere
# ----------------------------------------------------------

player_health = 10


def drink_health_potion():
    """Access global variable inside function."""
    print(f"Player health (global): {player_health}")


drink_health_potion()


# ----------------------------------------------------------
# 3. Modifying Global Variables
# Use 'global' keyword to modify a global variable inside a function
# ----------------------------------------------------------

enemies = 3


def defeat_enemy():
    """Modify global variable using 'global' keyword."""
    global enemies
    enemies -= 1
    print(f"Enemy defeated! Enemies remaining: {enemies}")


defeat_enemy()
defeat_enemy()


# ----------------------------------------------------------
# 4. Block Scope (Python doesn't have block scope like other languages)
# Variables in if/for/while are accessible outside the block
# ----------------------------------------------------------

game_level = 5

if game_level > 3:
    difficulty = "hard"

print(f"Difficulty: {difficulty}")  # Still accessible outside if-block


# ----------------------------------------------------------
# 5. Constants (conventionally written in UPPERCASE)
# ----------------------------------------------------------

PI = 3.14159
MAX_SCORE = 100


def show_constants():
    """Display constant values."""
    print(f"PI: {PI}")
    print(f"Max score: {MAX_SCORE}")


show_constants()


# ----------------------------------------------------------
# Mini Project: Number Guessing Game
# ----------------------------------------------------------

print("\n=== Number Guessing Game ===")

import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = EASY_ATTEMPTS
else:
    attempts = HARD_ATTEMPTS

answer = random.randint(1, 100)

print(f"You have {attempts} attempts to guess the number.")


def check_answer(guess, answer, attempts):
    """Check the user's guess and return remaining attempts."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0


while attempts > 0:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))
    
    attempts = check_answer(guess, answer, attempts)
    
    if attempts == 0 and guess != answer:
        print(f"You've run out of guesses. The answer was {answer}.")
        break
    elif guess == answer:
        break
