import array

# Step 1: Original scores
scores = array.array('i', [65, 70, 50, 90, 60])
print("Original scores:", scores)

# Step 2: Add score 85
scores.append(85)
print("\nAfter appending 85:", scores)

# Step 3: Insert score 75 at index 2
scores.insert(2, 75)
print("\nAfter inserting 75 at index 2:", scores)

# Step 4: Remove score 50
scores.remove(50)
print("\nAfter removing score 50:", scores)

# Step 5: Calculate average score
average = sum(scores) / len(scores)
print("\nAverage score:", average)

# Step 6: Highest and lowest scores
highest = max(scores)
lowest = min(scores)
print("Highest score:", highest)
print("Lowest score:", lowest)
