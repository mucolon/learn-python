# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears", "Blueberries"]

# Use a constructor
# number2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])
print(numbers[3])

# Get length
print(len(fruits))

# Append to list
fruits.append("Mangos")

# Remove entry from list
fruits.remove("Apples")
numbers.remove(2)

# Insert into postion
fruits.insert(0, "Apples")
numbers.insert(1, 2)

# Change value
# fruits[0] = "Blueberries"

# Remove index position with pop
# fruits.pop(0)
# numbers.pop(4)
print(numbers)

# Reverse list
fruits.reverse()
numbers.reverse()

# Sort list
# strings are ordered alphabetically
# numbers are ordered from least to greatest
fruits.sort()
numbers.sort()

# Reverse sort
fruits.sort(reverse=True)
numbers.sort(reverse=True)
