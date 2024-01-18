#!/usr/bin/env python
# coding: utf-8

# In[39]:


import random

# Generate a random integer between 0 and 9 (inclusive) for the first number
a = random.randint(0, 9)

# Generate a second random integer between 0 and 9 (inclusive) for the second number
b = random.randint(0, 9)

a=0
b=2

# Create a list to store the chain in
bracelet = [a, b]

# Set to store unique unit pairs encountered in the chain
unique_unit_pairs = set()

# Update the loop range to iterate from 2 to 5 (to get 5 elements in total)
while True:
    # Get the last two elements in the list
    last_two_elements = bracelet[-2:]
    
    # Calculate the sum of the last two elements and get the units digit
    units = sum(last_two_elements) % 10
    
    # Check for repetition of pairs
    unit_pair = tuple(last_two_elements + [units])
    if unit_pair in unique_unit_pairs:
        print("Repetition of pairs detected. Chain is cut off.")
        break
    
    # Append the units digit to the list
    bracelet.append(units)
    
    # Add the unit pair to the set of unique unit pairs
    unique_unit_pairs.add(unit_pair)

print("Bracelet:", bracelet)
len(bracelet)-2


# In[51]:


import random

# Generate a random integer between 0 and 9 (inclusive) for the first number
a = random.randint(0, 9)

# Generate a second random integer between 0 and 9 (inclusive) for the second number
b = random.randint(0, 9)

a=1
b=5

# Create a list to store the chain in
bracelet = [a, b]

# Set to store unique unit pairs encountered in the chain
unique_unit_pairs = set()

# Update the loop range to iterate from 2 to 5 (to get 5 elements in total)
while True:
    # Get the last two elements in the list
    last_two_elements = bracelet[-2:]
    
    # Calculate the sum of the last two elements and get the units digit
    units = sum(last_two_elements) % 10
    
    # Check for repetition of pairs
    unit_pair = tuple(last_two_elements + [units])
    if unit_pair in unique_unit_pairs:
        print("Repetition of pairs detected. Chain is cut off.")
        break
    
    # Append the units digit to the list
    bracelet.append(units)
    
    # Add the unit pair to the set of unique unit pairs
    unique_unit_pairs.add(unit_pair)

print("Bracelet:", bracelet)
len(bracelet)-2


# In[41]:


import random

# Generate a random integer between 0 and 9 (inclusive) for the first number
a = random.randint(0, 9)

# Generate a second random integer between 0 and 9 (inclusive) for the second number
b = random.randint(0, 9)

a=0
b=5

# Create a list to store the chain in
bracelet = [a, b]

# Set to store unique unit pairs encountered in the chain
unique_unit_pairs = set()

# Update the loop range to iterate from 2 to 5 (to get 5 elements in total)
while True:
    # Get the last two elements in the list
    last_two_elements = bracelet[-2:]
    
    # Calculate the sum of the last two elements and get the units digit
    units = sum(last_two_elements) % 10
    
    # Check for repetition of pairs
    unit_pair = tuple(last_two_elements + [units])
    if unit_pair in unique_unit_pairs:
        print("Repetition of pairs detected. Chain is cut off.")
        break
    
    # Append the units digit to the list
    bracelet.append(units)
    
    # Add the unit pair to the set of unique unit pairs
    unique_unit_pairs.add(unit_pair)

print("Bracelet:", bracelet)
len(bracelet)-2


# In[42]:


import random

# Generate a random integer between 0 and 9 (inclusive) for the first number
a = random.randint(0, 9)

# Generate a second random integer between 0 and 9 (inclusive) for the second number
b = random.randint(0, 9)

a=0
b=0

# Create a list to store the chain in
bracelet = [a, b]

# Set to store unique unit pairs encountered in the chain
unique_unit_pairs = set()

# Update the loop range to iterate from 2 to 5 (to get 5 elements in total)
while True:
    # Get the last two elements in the list
    last_two_elements = bracelet[-2:]
    
    # Calculate the sum of the last two elements and get the units digit
    units = sum(last_two_elements) % 10
    
    # Check for repetition of pairs
    unit_pair = tuple(last_two_elements + [units])
    if unit_pair in unique_unit_pairs:
        print("Repetition of pairs detected. Chain is cut off.")
        break
    
    # Append the units digit to the list
    bracelet.append(units)
    
    # Add the unit pair to the set of unique unit pairs
    unique_unit_pairs.add(unit_pair)

print("Bracelet:", bracelet)
len(bracelet)-2


# In[44]:


import random

# Generate a random integer between 0 and 9 (inclusive) for the first number
a = random.randint(0, 9)

# Generate a second random integer between 0 and 9 (inclusive) for the second number
b = random.randint(0, 9)

a=1
b=3

# Create a list to store the chain in
bracelet = [a, b]

# Set to store unique unit pairs encountered in the chain
unique_unit_pairs = set()

# Update the loop range to iterate from 2 to 5 (to get 5 elements in total)
while True:
    # Get the last two elements in the list
    last_two_elements = bracelet[-2:]
    
    # Calculate the sum of the last two elements and get the units digit
    units = sum(last_two_elements) % 10
    
    # Check for repetition of pairs
    unit_pair = tuple(last_two_elements + [units])
    if unit_pair in unique_unit_pairs:
        print("Repetition of pairs detected. Chain is cut off.")
        break
    
    # Append the units digit to the list
    bracelet.append(units)
    
    # Add the unit pair to the set of unique unit pairs
    unique_unit_pairs.add(unit_pair)

print("Bracelet:", bracelet)
len(bracelet)-2


# In[47]:


import random

# Generate a random integer between 0 and 9 (inclusive) for the first number
a = random.randint(0, 9)

# Generate a second random integer between 0 and 9 (inclusive) for the second number
b = random.randint(0, 9)

a=2
b=6

# Create a list to store the chain in
bracelet = [a, b]

# Set to store unique unit pairs encountered in the chain
unique_unit_pairs = set()

# Update the loop range to iterate from 2 to 5 (to get 5 elements in total)
while True:
    # Get the last two elements in the list
    last_two_elements = bracelet[-2:]
    
    # Calculate the sum of the last two elements and get the units digit
    units = sum(last_two_elements) % 10
    
    # Check for repetition of pairs
    unit_pair = tuple(last_two_elements + [units])
    if unit_pair in unique_unit_pairs:
        print("Repetition of pairs detected. Chain is cut off.")
        break
    
    # Append the units digit to the list
    bracelet.append(units)
    
    # Add the unit pair to the set of unique unit pairs
    unique_unit_pairs.add(unit_pair)

print("Bracelet:", bracelet)
len(bracelet)-2


# In[ ]:




