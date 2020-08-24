# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print("Hello {}".format(name))


sayHello("Sam")


# Return vales
def getSum(num1, num2):
    total = num1 + num2
    return total


number = getSum(2, 4)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
def getSum2(num1, num2): return num1 + num2


number2 = getSum2(3, 4)
