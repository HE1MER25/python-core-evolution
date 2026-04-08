# Lists in Python

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# Modifying elements
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Adding elements
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(3)
print(my_list)  # Output: [10, 2, 4, 5, 6]

# Looping through a list
for item in my_list:
    print(item)  

# While loop with list
i = 0   
while i < len(my_list):
    print(my_list[i])
    i += 1 # Output: 10, 2, 4, 5, 6

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 2 # Output: 10, 4, 6

# Loop Comprehension
fruits = ["apple", "banana", "cherry"]
newFruits = []

for x in fruits:
    if "a" in x:
        newFruits.append(x)
print(newFruits) # Output: ['apple', 'banana']