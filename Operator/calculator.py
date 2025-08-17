# Quantities and Prices
apple_qty = 3          # kg
apple_price = 200      # per kg

banana_qty = 2         # dozen
banana_price = 50      # per dozen

mango_qty = 5          # kg
mango_price = 150      # per kg

# Calculate cost for each fruit
apple_cost = apple_qty * apple_price
banana_cost = banana_qty * banana_price
mango_cost = mango_qty * mango_price

# Calculate total bill
total_bill = apple_cost + banana_cost + mango_cost

# Print results
print("Apples cost:", apple_cost)
print("Bananas cost:", banana_cost)
print("Mangoes cost:", mango_cost)
print("-" * 20)
print("Total Bill:", total_bill)
