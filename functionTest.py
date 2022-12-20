# Modular code
# Analogy
# Define

def myfunc():
    print("Hello world!")
    print("Hi Henry")

myfunc()

#ARGUMENTS
myInt = 7
# local variables
def add(a, b):
    print(a+b)


# 3 + 4
add(3, 4)
# 1000 + 23
add(1000, 23)

# Write a function that multiplies 2 numbers a and b and prints the answer to terminal.
# Test the function with a few different numbers

def mul(num1, num2):
    print(num1 * num2)


mul(5, 6)
mul(-7, 9)

# Bonus: function takes a number and squares it, print to terminal

def square(num):
    print(num * num)
    #print(num ** 3)


square(3)
square(12)
square(100)
square(11)
square(111)
square(1111)
square(11111)

# Challenge: function take 3 numbers, (a, b, c), print (a * b)^2 - c

# a = 3, b = 4, c = 5

# a * b = 12
# 12 ^ 2 = 144
# 144 - 5  = 139

# a = 2, b = 5, c = 10

# a * b = 10
# 10 ^ 2 = 100
# 100 - 10 = 90

def challenge_solver(a, b, c):
    print((a * b)**2 - c)

challenge_solver(3, 4, 5)
challenge_solver(2, 5, 10)

