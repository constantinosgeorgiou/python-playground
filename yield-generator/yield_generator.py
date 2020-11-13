# Tutorial
# https://www.guru99.com/python-yield-return-generator.html

def testyield():
    yield "I am currenlty testing the yield method"


output = testyield()  # Returns generator object
print(output)

for i in output:
    print(i)

# +--------------+
# |  Generators  |
# +--------------+


def generator():
    yield "T"
    yield "H"
    yield "I"
    yield "S"
    yield ""
    yield "I"
    yield "S"
    yield ""
    yield "C"
    yield "O"
    yield "O"
    yield "L"


test = generator()

for i in test:
    print(i)

print(next(testyield()))


# Read values from the generator
# ------------------------------

def even_numbers(n):
    for x in range(n):
        if (x % 2 == 0):
            yield x


# Using a list method conversion
num = even_numbers(10)
print(list(num))

# Using for loop
num = even_numbers(20)
for i in num:
    print(i)

# Using next method
num = even_numbers(3)
print(next(num))
print(next(num))


# Generators are one-time use
print(list(num))

# To use again, make the call to function again
num = even_numbers(3)
print(list(num))

# Calling function with yield
# ---------------------------


def test(n):
    return n * n


def get_square(n):
    for i in range(n):
        yield test(i)


square = get_square(10)

for i in square:
    print(i)
