print(1 + 5)
print(7 * 2.5)
print(8 / 5)

# mod/modulus/remainder
# a % b - gives you the remainder when a is divided by b
print(46 % 5)

a = 7

# Check if a is even number

if a % 2 == 0:
    print("Even!")

else:
    print("Odd!")

# Check if a is divisible by 3 or 5
if a % 3 == 0 or a % 5 == 0:
    print("Divisible by 3 or 5")

else:
    print("Not divisible by 3 or 5")

# Create new variable to keep track of sum, set it to 0
# For loop, iterate through the numbers 1-999
# For each number, if it is divisible by 3 or 5, add it to sum
# After finishing the loop, print sum