# Functions for math operations
# return -> how a function can give back an answer


def addTwo(x, y):
    return x+y

def mulTwo(x, y):
    return x*y

def mysteryOp(x, y, z):
    a = x + y
    a = a * z
    return a


z = addTwo(4, 5)
z = 20
print(z)

y = mysteryOp(5, 6, 8)
print(y)



a = 6
b = 2
c = 13

a = b * c
b = b - c
c = a * b
b = a - c

print(a, b, c)

# Q: what is a, b, c?
# a = 26, b = 2, c = 13
# a = 26, b = -11, c = 13
# a = 26, b = -11, c = -286
# a = 26, b = 312, c = -286

a = 2
b = 3
c = 4

a += 20
b *= 11
c = max(a, b)
c = a + b + c

# what is a, b, c?
# a = 22, b = 3, c = 4
# a = 22, b = 33, c = 4
# a = 22, b = 33, c = 33
# a = 22, b = 33, c = 88

a = 3
b = 3
c = 5

a += c
b *= b
c = min(a, c)
b = max(b, c)
a = a * (b - c)

# what is a, b, c?
# a = 8, b = 3, c = 5
# a = 8, b = 9, c = 5
# a = 8, b = 9, c = 5
# a = 8, b = 9, c = 5
# a = 32, b = 9, c = 5

print(a, b, c)

# HW exercise:

a = 7
b = 13
c = 15

a = b - c
b = b * a
c = max(a, b, c)
b = min(a, b, c)
a = a * b * c

# what is a, b, c?
# a = -2, b = 13, c = 15
# a = -2, b = -26, c = 15
# a = -2, b = -26, c = 15
# a = -2, b = -26, c = 15
# a = 780, b = -26, c = 15

