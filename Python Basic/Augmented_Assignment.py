Start with count = 0. Perform the following updates in order, printing count after each step:

count += 5
count -= 2
count *= 4
ans:
count = 0
print("Start:", count)      # 0

count += 5
print("After += 5:", count) # 5

count -= 2
print("After -= 2:", count) # 3

count *= 4
print("After *= 4:", count) # 12

count /= 2
print("After /= 2:", count) # 6.0

print("Final type:", type(count))  # <class 'float'>
