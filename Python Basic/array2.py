# 🧩 Problem Statement:

# A shop owner is tracking the daily number of customers using a Python array. The data for the first 5 days is:

# [120, 135, 150, 110, 145]


# You need to:

# Display the original data.

# Add the customer count 160 for the 6th day.

# Insert the count 125 as the data for a missing 3rd day (shift current 3rd and onward).

# Remove the day with 110 customers (it was entered incorrectly).

# Find the total and average number of customers.

# Display the data in reverse order.

import array

# Step 1: Original data
customers = array.array('i', [120, 135, 150, 110, 145])
print("Original customer data:", customers)

# Step 2: Add 6th day data (160)
customers.append(160)
print("\nAfter appending 160:", customers)

# Step 3: Insert missing 3rd day data (125)
customers.insert(2, 125)
print("\nAfter inserting 125 at index 2:", customers)

# Step 4: Remove incorrect entry (110)
customers.remove(110)
print("\nAfter removing 110:", customers)

# Step 5: Total and average
total = sum(customers)
average = total / len(customers)
print("\nTotal customers:", total)
print("Average customers per day:", average)

# Step 6: Reverse order
reversed_data = customers[::-1]
print("Customer data in reverse:", reversed_data)
