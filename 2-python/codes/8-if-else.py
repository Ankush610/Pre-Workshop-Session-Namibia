# Making decisions
temperature = 34

if temperature > 30:
    print("It's hot, drink water")
else:
    print("Nice weather")

# More than two choices with elif
if temperature > 38:
    print("Stay inside")
elif temperature > 25:
    print("Wear a hat")
else:
    print("Take a jacket")

# = stores a value, == compares
print(temperature == 34)

print(temperature != 34)
