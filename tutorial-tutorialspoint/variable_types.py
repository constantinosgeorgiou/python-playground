print("\n")

# +-----------------------+
# |  Multiple assignment  |
# +-----------------------+

print("+-----------------------+\n|  Multiple assignment  |\n+-----------------------+\n")

a = b = c = 1
# Note: All three variables assigned to the same memory location

print("a: ", a)
print("b: ", b)
print("c: ", c)

# Multiple objects to multiple variables
d, e, f = 1, 2, "Alan"

print("d: ", d)
print("e: ", e)
print("f: ", f)

print("\n\n+----------------------+\n| Standard Data Types  |\n+----------------------+")

print("\nNumbers\n-------")

var1 = 1
var2 = 10
var3 = 100
print("var1: %d, var2: %d, var3: %d" % (var1, var2, var3))

# delete var1
del var1
# print("Deleted var1 with value", var1)  # NameError: name 'var1' is not defined

# delete var2 and var3
del var2, var3

signed_integer = 10
floating_point = 20.20
complex_number = 3.14j
# Note: A complex number consists of
#       an ordered pair of real floating-point numbers
#       denoted by x + yj, where x and y are real numbers
#       and j is the imaginary unit.

print("int: %d, float: %d, complex:" %
      (signed_integer, floating_point), complex_number)

print("\nStrings\n-------")

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Print complete string: ", string)
print("Print first character of string: ", string[0])
print("Print last character of string: ", string[-1])
print("Print second to last character of string: ", string[-2])
print("Print characters starting from 3rd to 5th: ", string[2:10])
print("Print string starting from 3rd character: ", string[2:])
print("Print concatenated string: ", string + "01234")
print("Print repeat string 2 times: ", string*2)


print("\nLists\n-----\n")

random_list = ["abcd", 786, 2.23, "Alan", 70.2]

del random_list

letter_list = ["A", "B", "C", "D", "E"]
number_list = [1, 2, 3, 4, 5]

print("number list: ", number_list)
print("letter list: ", letter_list)
print("Print first element of letter list: ", letter_list[0])
print("Print last element of letter list: ", letter_list[-1])
print("Print second to last element of letter list: ", letter_list[-2])
print("Print elements starting from 2nd till 3rd: ", letter_list[1:3])
print("Print elements starting from 3rd: ", letter_list[2:])
print("Print number list 2 times: ", number_list * 2)
print("Print concatenated lists: ", letter_list+number_list)

print("\nTuples\n------\n")

random_tuple = ('abcd', 786, 2.23, 'Alan', 70.2)
tiny_tuple = (123, 'Turing')

print("Print random tuple: ", random_tuple)
print("Print tiny tuple: ", tiny_tuple)
print("Print first element of random tuple: ", random_tuple[0])
print("Print last element of random tuple: ", random_tuple[-1])
print("Print second to last element of random tuple: ", random_tuple[-2])
print("Print elements starting from 2nd till 3rd: ", random_tuple[1:3])
print("Print elements starting from 3rd: ", random_tuple[2:])
print("Print tiny tuple 2 times: ", tiny_tuple * 2)
print("Print concatenated tuples: ", random_tuple+tiny_tuple)

# Note: You can NOT update a tuple or list directly


print("\nDictionaries\n------------\n")
# Hash-table-ish

random_dictionary = {}

random_dictionary["one"] = "This is one"
random_dictionary[2] = "This is two"

tiny_dictionary = {
    "name": "Alan",
    "code": 6734,
    "department": "Mathematics"
}

print("Print value of \"one\" key: ", random_dictionary["one"])
print("Print value of 2 key: ", random_dictionary[2])
print("Print complete dictionary: ", tiny_dictionary)
print("Print all the keys: ", tiny_dictionary.keys())
print("Print all the values: ", tiny_dictionary.values())
# Note: The elements in a dictionary are unordered


print("\n+------------------------+\n|  Data Type Conversion  |\n+------------------------+\n")

print("int(x[, base]): Converts x to an integer. The base specifies the base if x is a string.")

print("float(x): Converts x to a floating-point number.")

print("complex(real[, imag]): Creates a complex number.")

print("str(x): Converts object x to a string representation.")

print("repr(x): Converts object x to an expression string.")

print("eval(str): Evaluates a string and returns an object.")

print("tuple(s): Converts s to a tuple.")

print("list(s): Converts s to a list.")

print("set(s): Converts s to a set.")

print("dict(d): Creates a dictionary. d must be a sequence of(key, value) tuples.")

print("frozenset(s): Converts s to a frozen set.")

print("chr(x): Converts an integer to a character.")

print("unichr(x): Converts an integer to a Unicode character.")

print("ord(x): Converts a single character to its integer value.")

print("hex(x): Converts an integer to a hexadecimal string.")

print("oct(x): Converts an integer to an octal string.")
