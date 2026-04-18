# Day 13 - Debugging
# Techniques: describe the problem, reproduce the bug,
# play computer, fix errors, use print, use a debugger


# ----------------------------------------------------------
# 1. Describe the Problem
# Bug: the loop should print odd numbers from 1 to 10
# ----------------------------------------------------------

print("=== Odd Numbers ===")

for number in range(1, 11):
    if number % 2 != 0:
        print(number)


# ----------------------------------------------------------
# 2. Reproduce the Bug
# Bug: age check was using assignment (=) instead of (==)
# ----------------------------------------------------------

print("\n=== Age Check ===")

age = 18

if age == 18:
    print("You are 18 years old.")


# ----------------------------------------------------------
# 3. Play Computer (trace through logic manually)
# Bug: total was never reset between rounds
# ----------------------------------------------------------

print("\n=== Score Tracker ===")

scores = [10, 20, 30]
total = 0

for score in scores:
    total += score

print(f"Total score: {total}")


# ----------------------------------------------------------
# 4. Fix the Errors
# Bug: function was called before it was defined
# ----------------------------------------------------------

print("\n=== Area Calculator ===")


def calculate_area(width, height):
    """Returns the area of a rectangle."""
    return width * height


area = calculate_area(5, 3)
print(f"Area: {area}")


# ----------------------------------------------------------
# 5. Use Print to Debug
# Technique: add print statements to trace variable values
# ----------------------------------------------------------

print("\n=== FizzBuzz Debug ===")

for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ----------------------------------------------------------
# 6. Use a Debugger
# Tip: In production code, use breakpoint() or an IDE debugger
# Here we simulate a careful step-through using print tracing
# ----------------------------------------------------------

print("\n=== Debugger Simulation ===")


def get_largest(numbers):
    """Returns the largest number in a list."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


sample = [4, 8, 2, 15, 7]
result = get_largest(sample)
print(f"Largest number: {result}")
