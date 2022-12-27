# for loops

# for i in range(number):
#   do code

# for i in range(start, stop):
#   do code

# The second block starts at [start], and ends at [stop-1]
# If we only have 1 argument, then we automatically start at 

# The above code repeats the code inside the for loop [number] times
# Local variable vs Global variable
# A global variable is a variable that can be used anywhere after we have defined it
# i = local variable
# local variables should only be used inside their container

# How to print out all the numbers from 5 to 55 (inclusive)?
# 5 6 7 ... 55

for i in range(5, 56):
    print(i)



# Add up all the numbers from 1 to 100
# 1 + 2 + 3 ... + 100 = ?

# Algorithm = a bunch of steps/commands we/computer takes to solve a problem

total = 0

for i in range(1, 101): # i = 1; i = 2; ... i = 100
    total += i # total = total + i

print(total)


# write a for loop that prints out all the EVEN numbers from 1 to 50
# 2 4 6 ... 50 
# HINT: use a conditional inside of the for loop
# HINT 2: a % b gives you the remainder when I divide a by b
#         eg. 20 % 3 = 2
# TIP: be careful of proper indenting!

# for loop:
#   if statement:
#       code inside of the if statement
#
#   code outside of the if statement BUT inside of the for loop
