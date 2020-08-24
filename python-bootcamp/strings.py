# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
print("Hello, my name is " + name + " and I am " + str(age))

# String Formatting
# Arguments by position
print("My name is {name} and I am {age}".format(name=name, age=age))
print("My name is {} and I am {}".format(name, age))
print("My name is {1} and I am {0}\n".format(age, name))

# F-Strings
print(f"Helio, my name is {name} and I am {age}")
