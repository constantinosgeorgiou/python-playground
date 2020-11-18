import numpy

# Create a rank 1 array
a = numpy.array([1, 2, 3])

print("a shape: ", a.shape)
print("a elements\n", "a[0]: ", a[0], "a[1]: ", a[1], "a[2]: ", a[2])

# Change value of a[0]
a[0] = 5
print("New value of a[0]: ", a[0])


# Create a rank 2 array
#   1     2     3
#   4     5     6
b = numpy.array([[1, 2, 3], [4, 5, 6]])
print("b: ", b)

print("b shape: ", b.shape)
print("b[0, 0]: ", b[0, 0], "b[0, 1]: ", b[0, 1], "b[1, 0]:", b[1, 0])

# Create a 2 column x 2 row array of zeros
zeros = numpy.zeros((2, 2))

# Create a 1 column x 2 row array of ones
ones = numpy.ones((1, 2))

print("zeros: ", zeros)
print("ones: ", ones)

# Create a 2 column x 1 row array of ones
row = numpy.ones((2,))

# Create a 2 x 2 constant array of 7s
#   7     7
#   7     7
constant = numpy.full((2, 2), 7)
print("constant: ", constant)

# Create a 2x2 identity matrix
identity = numpy.eye(2)
print("identity: ", identity)

# Construct an array from 0 to 10 with step 0.1
aranged = numpy.arange(0, 10, 0.1)
print("aranged: ", aranged)

# Create a 2x2 array with random values
random2d = numpy.random.randint(0, 100, size=(2, 2))
print("random2d: ", random2d)

#   1      2      3      4
#   5      6      7      8
#   9     10     11     12
fourbyfour = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#   2      3
#   6      7
sliced = fourbyfour[:2, 1:3]
# Note:  fourbyfour[columns, rows]
print("fourbyfour: ", fourbyfour)
print("sliced: ", sliced)

x = numpy.array([[1, 2], [3, 4]], dtype=numpy.float64)
y = numpy.array([[5, 6], [7, 8]], dtype=numpy.float64)
c = x + y
c = numpy.add(x, y)

c = x - y
c = numpy.subtract(x, y)

c = x * y
c = numpy.multiply(x, y)

c = x / y
c = numpy.divide(x, y)

c = numpy.sqrt(x)  # element-wise square root of x

v = numpy.array([9, 10])
w = numpy.array([2, 1])
print(numpy.dot(v, w))

x = numpy.array([[1, 2], [3, 4]])
w = numpy.array([2, 1])
print(numpy.dot(x, w))
print(x.dot(w))
p = x.dot(w)
print(p.shape)

x = numpy.array([[1, 2], [3, 4]])
y = numpy.array([[2, 1], [0, 1]])
print(numpy.dot(x, y))
print(x.dot(w))
p = x.dot(w)
print(p.shape)


x = numpy.array([[1, 2], [3, 4]])
y = x.T
print(y)
