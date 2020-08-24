# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ("Apples", "Oranges", "Grapes")
# print(fruits)

# Using a constructor
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))
# print(fruits2)

# Single value needs a trailing comma
fruits2 = ("Apples",)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = "Pears"

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
print("\n\nSets")
# Create set
fruits_set = {"Apples", "Oranges", "Grapes"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Mangos")

# Remove from set
fruits_set.remove("Mangos")

# Add duplicate
fruits_set.add("Apples")

# Clear set
fruits_set.clear()

# Delete
del fruits_set

# print(fruits_set)
