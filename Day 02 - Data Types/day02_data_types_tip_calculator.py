# Day 02 - Data Types + Tip Calculator (Beginner Version)

# 1) Subscripting (index starts at 0)
print("Hello"[0])  # H

# 2) String vs Number
print("123" + "345")  # joins text -> 123345
print(123 + 345)      # adds numbers -> 468

# 3) Large numbers (underscore is just for readability)
print(123_456_789)

# 4) Float (decimal) and Boolean (True/False)
print(3.14159)
print(True)
print(False)

# 5) Type checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# 6) Type conversion example (len needs a string)
name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_name))

# -------------------------
# Final Project: Tip Calculator
# -------------------------
print("\nWelcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15: "))
people = int(input("How many people to split the bill? "))

# Prevent divide-by-zero (people cannot be 0)
if people == 0:
    print("People cannot be 0. Please run again and enter at least 1 person.")
else:
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people

    final_amount = round(bill_per_person, 2)
    print(f"Each person should pay: ${final_amount:.2f}")

