# Loop over a list
animals = ["lion", "elephant", "giraffe"]
for animal in animals:
    print("I saw a", animal)

# Repeat a number of times (starts at 0, stops before 5)
for i in range(5):
    print("Step", i)

# Add up all prices with a loop
prices = [20, 45, 15]
total = 0
for price in prices:
    total = total + price
print("Total:", total)
