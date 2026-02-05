"""
Day 01 - Python Basics (Beginner Notes)

What you practice here:
- print(): show text on the screen
- input(): ask the user and wait for typing
- len(): count characters in a string
- variables: store values in names like name, username
- swapping: exchange values between two variables
- mini project: Band Name Generator
"""


def main() -> None:
    # input(...) pauses the program and waits for the user to type something.
    # That typed text becomes a string value.
    user_name = input("What is your name? ")

    # "Hello " + user_name + "!" joins (concatenates) strings together.
    print("Hello " + user_name + "!")

    # Ask again (practice). The result is stored in variable 'name'.
    name = input("Enter your name: ")

    # len(name) counts how many characters are in the string (letters, spaces, symbols).
    print(len(name))

    # Variables can be reassigned (changed). Now name becomes "Hikman".
    name = "Hikman"
    print(name)  # prints the current value of name

    # Reassign again: now name becomes "Mahnoor".
    name = "Mahnoor"
    print(name)

    # Store input in 'username' so we can reuse it later.
    username = input("What is your name? ")

    # Calculate the length and store it in a variable (clean + readable).
    length = len(username)
    print(length)

    # Swapping exercise: we want to exchange the values in glass1 and glass2.
    glass1 = "milk"
    glass2 = "juice"

    # We need a temporary variable so we don't lose the first value.
    temp = glass1      # save "milk" in temp
    glass1 = glass2    # glass1 becomes "juice"
    glass2 = temp      # glass2 becomes the saved "milk"

    # Print results so you can confirm the swap worked.
    print("glass1:", glass1)
    print("glass2:", glass2)

    # len() also works on a fixed string (no input needed).
    name = "Hikman"
    print(len(name))

    # -------------------------
    # Final Project: Band Name Generator
    # -------------------------
    print("\n--- Welcome to the Band Name Generator ---\n")

    # Ask user for two words.
    city_name = input("What's the name of the city you grew up in? ")
    pet_name = input("What's your pet's name? ")

    # Combine them with a space in between.
    band_name = city_name + " " + pet_name

    # Print the final result.
    print("Your band name could be:", band_name)


# This line means: only run main() when we run this file directly.
# (It won't run automatically if this file is imported somewhere else.)
if __name__ == "__main__":
    main()
