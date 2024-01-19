#!/usr/bin/env python
# coding: utf-8

# In[37]:


import random

# We could generate a random integer between 0 and 9 (inclusive) for the first and second number
# using a = random.randint(0, 9)
# However for this example we can start from the chain given in the question 


a=1
b=5

# Create a list to store the chain in
bracelet = [a, b]

# Set to store unique unit pairs encountered in the chain
unique_unit_pairs = set()


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
print("Bracelet length", len(bracelet)-2)

# Iterate through the bracelet and create pairs of adjacent elements
adjacent_pairs = [(bracelet[i], bracelet[i+1]) for i in range(len(bracelet)-1)]


# Check for missing pairs (0, 0) to (9, 9)
for i in range(10):
    for j in range(10):
        pair_to_check = (i, j)
        if pair_to_check not in adjacent_pairs:
            
            # set the first two integers of the new bracelet to be from the missing pair from the previous one
            a = i
            b = j
            
            # Run the code again by reinitializing the first two integers
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
            print("Bracelet length", len(bracelet) - 2)
            
            # Extend the existing list of adjacent_pairs with the new pairs
            adjacent_pairs.extend([(bracelet[i], bracelet[i+1]) for i in range(len(bracelet)-1)])


# In[ ]:




