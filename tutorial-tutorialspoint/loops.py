import sys

letter_list = ["A", "B", "C", "D", "E", "F", "G"]

iterator = iter(letter_list)  # This builds an iterator object

# Note: Iterators is an object which allows the programmer
#       to traverse through all the elements of a collection

print("Print next available element in iterator: ", next(iterator))
print("\n")

for i in iterator:
    print(i, end=" ")
print("\n")

iterator = iter(letter_list)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("Reached end of letter list")
        break
