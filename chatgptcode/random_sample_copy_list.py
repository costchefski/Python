import random

# Step 1: Create a list of 10 names
names = [
    "John", "William", "James", "Benjamin", "Michael",
    "Olivia", "Emma", "Sophia", "Isabella", "Mia"
]

# Step 2: Create a second list with 4 random names from the first list
second_list = random.sample(names, 4)

# Step 3: Print the whole first list
print("First List:")
print(names)

# Step 4: Print the whole second list
print("Second List:")
print(second_list)
