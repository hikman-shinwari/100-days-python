# List Indexing Practice

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island",
    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
    "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
    "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
    "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington",
    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
    "Arizona", "Alaska", "Hawaii"
]

# Last state using negative index (professional way)
print("Last state:", states_of_america[-1])

# Number of states
print("Total states:", len(states_of_america))


# Nested List Example
fruits = ["Strawberries", "Nectarines", "Apples"]
vegetables = ["Spinach", "Kale", "Tomatoes"]

dirty_dozen = [fruits, vegetables]

print("Nested list:", dirty_dozen)
print("First fruit:", dirty_dozen[0][0])
