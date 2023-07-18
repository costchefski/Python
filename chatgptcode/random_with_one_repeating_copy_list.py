import random

# Step 1: Create a list of 10 names
names = [
    "John", "William", "James", "Benjamin", "Michael",
    "Olivia", "Emma", "Sophia", "Isabella", "Mia"
]

# Step 2: Create a second list with 3 random names and "John" from the first list
names_without_john = names.copy()
names_without_john.remove("John")
second_list = random.sample(names_without_john, 3)
second_list.append("John")
random.shuffle(second_list)  # Randomize the order of the second list

# Step 3: Print the whole first list
print("First List:")
print(names)

# Step 4: Print the whole second list
print("Second List:")
print(second_list)
