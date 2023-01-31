# Exercises to practice programming fundamentals

# Write a program that will compute the area of a circle, given r (radius)
# Print the area
# float = floating-point number = numbers with a decimal point
# Constant = a variable that don't change in code

r = 7.8
pi = 3.14 # A constant

area = r * r * pi # float
print("The area of the circle = " + str(area))

# Part 2: now compute the circumference of the circle and print it out like before.
circumference = 2 * pi * r
print("The circumference of the circle is " + str(circumference))

# Tutorial: how to iterate through elements in a list
list_nums = [2, 45, 35, 3, 0, 1]
#print(list_nums[2])
#list_nums[0]
#list_nums[1]
#list_nums[2] ... bad style! We can use a for loop for this!

list_size = len(list_nums)

for i in range(list_size): # 0..number of items-1
    print(list_nums[i])

# Exercise: get the sum of all numbers in a list, print it out as usual.
# Do not list_nums[0] + list_nums[1] + ... 



