# if else statements

# if [condition]:
#   - what executes if the condition is true
#
# elif [condition]:
#   - what executes if the second condition is true
#
# else:
#   - what executes if none of the conditions are true
#
# more code

x = 90

if x > 4:
    print("Variable x is greater than 4")

elif x < 4:
    print("Variable x is less than 4")

else:
    print("Variable x is 4")


# Write a block of code that uses if/elif/else -
# check if the number of characters in y is greater than 10.
# if it is > 10, then print a message that says so.
# otherwise, if it is > 5, then print a different message.
# otherwise, then print another message.

y = "999997676454776"
print(len(y))


if len(y) > 10:
    print("Length of y is greater than 10")

elif len(y) > 5:
    print("Length of y is greater than 5, less than 10")

else:
    print("Length of y <= 5")

# Write block of code 
testList = [1, 2, 3, 46, 54477, 8, True, "auywerga"]
testString = "suerygue"

# if/elif/else statements to check the length of list vs length of string
# if length of list > length of string, print message
# if they are same length, different msg
# if length of list < length of string, print msg

# = -> variable assignment
# == -> comparisons

if len(testList) > len(testString):
    print("List length > String length")

elif len(testList) == len(testString):
    print("List same length as string")

else:
    print("List length < String length")


print(len(testList))

