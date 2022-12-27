import time

# a library is a bunch of functions(commands) that we can import so that we can use these functions
# some libraries are in built in python, which means that anyone can import them
# other libraries need to be downloaded from the internet before we can import them

# for loops/while loops - repeated execution of code

# while [condition (boolean)]: (check condition every time we want to run the code inside the while loop)
#   do some code


# while True:
#     print("Hello")


counter = 1 # represent the number of seconds that have passed

while counter < 10:
    #time.sleep(1)
    counter = counter + 1
    print(counter)


test = 0

# write a while loop that will:
# check if test is a positive number
# if it is, then:
# subtract 3 from it
# print the value of test

while test > 0:
    test -= 3   # test = test - 3 (subtract 3 from test)
    print(test)
