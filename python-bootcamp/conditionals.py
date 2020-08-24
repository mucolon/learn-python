# If/ Else conditions are used to decide to do something based on something being true or false

x = 21
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
print("Simple if")
if x > y:
    print(f"{x} is greater than {y}")

# If/else
print("\nif/else")
if x >= y:
    print("if")
    print(f"{x} is greater than {y}")
else:
    print("else")
    print(f"{y} is greater than {x}")

# If/elif/else
print("\nif/elif/else")
if x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{y} is great than {x}")

# x = 10
# Nested if
if x > 2:
    if x <= 10:
        print(f"\n{x} is greater than 2 and less than or equal to 10")

# Logical operators (and, or, not) - Used to combine conditional statements


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
