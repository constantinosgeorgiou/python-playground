## [Python 3 Tutorial tutorialspoint](https://www.tutorialspoint.com/python3/index.htm)

Switched from [tutorialspoint Python Tutorial](https://www.tutorialspoint.com/python/index.htm) to this one due to the fact that I'll be using python3

- [Python 3 Tutorial tutorialspoint](#python-3-tutorial-tutorialspoint)
  - [Basics](#basics)
  - [Standard Data Types](#standard-data-types)
  - [Basic operators](#basic-operators)
  - [Decisions](#decisions)
  - [Loops](#loops)

### Basics

Quotes

```python
word = 'single'

sentence = "using double quotes"

paragraph = """This is an example of triple
code spanning multiple lines"""
```

Comments

```python
# This is a comment
application = "python" # this is also a comment

# No multiline
# commenting
# feature :(
```

### Standard Data Types

- Numbers
- String
- List
- Tuple
- Dictionary

Data Type Conversion

| Function              | Description                                                             |
| --------------------- | ----------------------------------------------------------------------- |
| int(x [,base])        | Converts x to an integer. The base specifies the base if x is a string. |
| float(x)              | Converts x to a floating-point number.                                  |
| complex(real [,imag]) | Creates a complex number.                                               |
| str(x)                | Converts object x to a string representation.                           |
| repr(x)               | Converts object x to an expression string.                              |
| eval(str)             | Evaluates a string and returns an object.                               |
| tuple(s)              | Converts s to a tuple.                                                  |
| list(s)               | Converts s to a list.                                                   |
| set(s)                | Converts s to a set.                                                    |
| dict(d)               | Creates a dictionary. d must be a sequence of (key,value) tuples.       |
| frozenset(s)          | Converts s to a frozen set.                                             |
| chr(x)                | Converts an integer to a character.                                     |
| unichr(x)             | Converts an integer to a Unicode character.                             |
| ord(x)                | Converts a single character to its integer value.                       |
| hex(x)                | Converts an integer to a hexadecimal string.                            |
| oct(x)                | Converts an integer to an octal string.                                 |

### Basic operators

View a list of [basic operators](./basic-operators.md) here.

### Decisions

```python
number = 100

if (number === 100): print("Number is 100")
print("Byeeeee")

```

### Loops

| Control Statement  | Description                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| break statement    | Terminates the loop statement and transfers execution to the statement immediately following the loop.                              |
| continue statement | Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.                        |
| pass statement     | The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute. |