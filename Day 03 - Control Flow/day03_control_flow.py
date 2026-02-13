# Day 03 - Control Flow (Beginner Version)
# Topics: if/else, modulo, elif, nesting, logical operators
# Mini projects: Python Pizza + Treasure Island

# -------------------------
# 1) If / Else (basic)
# -------------------------
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")

# -------------------------
# 2) Modulo % (even / odd)
# -------------------------
number = int(input("\nEnter a number: "))
if number % 2 == 0:
    print("Even number ✅")
else:
    print("Odd number ✅")

# -------------------------
# 3) Python Pizza Project
# -------------------------
print("\nWelcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size. Please run again.")

if bill > 0:
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}.")

# -------------------------
# 4) Logical Operators (and / or / not)
# -------------------------
print("\nLogical operators example:")

height = int(input("Enter your height in cm: "))
ticket = 0

if height >= 120:
    print("You can ride!")
    age2 = int(input("Enter your age: "))

    if age2 < 12:
        ticket = 5
    elif age2 <= 18:
        ticket = 7
    else:
        ticket = 12

    wants_photo = input("Do you want a photo? Y or N: ").upper()
    if wants_photo == "Y":
        ticket += 3

    print(f"Your final ticket price is: ${ticket}")
else:
    print("Sorry, you can't ride.")

# -------------------------
# 5) Treasure Island Project
# -------------------------
print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Left or right? ").lower()

if choice1 == "left":
    choice2 = input("Swim or wait? ").lower()

    if choice2 == "wait":
        choice3 = input("Which door? red, blue, or yellow: ").lower()

        if choice3 == "yellow":
            print("You Win! 🏆")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
