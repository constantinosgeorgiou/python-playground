## Basic operators <!-- omit in toc -->

Types of operator:

- [Arithmetic Operators](#arithmetic-operators)
- [Comparison (Relational) Operators](#comparison-relational-operators)
- [Assignment Operators](#assignment-operators)
- [Bitwise Operators](#bitwise-operators)
- [Logical Operators](#logical-operators)
- [Membership Operators](#membership-operators)
- [Identity Operators](#identity-operators)
- [Operators Precedence](#operators-precedence)

### Arithmetic Operators

| Operator          | Description                                                                                                                                                                                                                                 | Example                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| + Addition        | Adds values on either side of the operator.                                                                                                                                                                                                 | a + b = 31                                                |
| - Subtraction     | Subtracts right hand operand from left hand operand.                                                                                                                                                                                        | a – b = -11                                               |
| * Multiplication  | Multiplies values on either side of the operator                                                                                                                                                                                            | a * b = 210                                               |
| / Division        | Divides left hand operand by right hand operand                                                                                                                                                                                             | b / a = 2.1                                               |
| % Modulus         | Divides left hand operand by right hand operand and returns remainder                                                                                                                                                                       | b % a = 1                                                 |
| ** Exponent       | Performs exponential (power) calculation on operators                                                                                                                                                                                       | a**b =10 to the power 20                                  |
| // Floor Division | The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity): | 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0 |


### Comparison (Relational) Operators

| Operator | Description                                                                                                       | Example               |
| -------- | ----------------------------------------------------------------------------------------------------------------- | --------------------- |
| ==       | If the values of two operands are equal, then the condition becomes true.                                         | (a == b) is not true. |
| !=       | If values of two operands are not equal, then condition becomes true.                                             | (a!= b) is true.      |
| >        | If the value of left operand is greater than the value of right operand, then condition becomes true.             | (a > b) is not true.  |
| <        | If the value of left operand is less than the value of right operand, then condition becomes true.                | (a < b) is true.      |
| >=       | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. | (a >= b) is not true. |  |
| <=       | If the value of left operand is less than or equal to the value of right operand, then condition becomes true.    | (a <= b) is true.     |


### Assignment Operators

| Operator           | Description                                                                                | Example                                 |
| ------------------ | ------------------------------------------------------------------------------------------ | --------------------------------------- |
| =                  | Assigns values from right side operands to left side operand                               | c = a + b assigns value of a + b into c |
| += Add AND         | It adds right operand to the left operand and assign the result to left operand            | c += a is equivalent to c = c + a       |
| -= Subtract AND    | It subtracts right operand from the left operand and assign the result to left operand     | c -= a is equivalent to c = c - a       |
| *= Multiply AND    | It multiplies right operand with the left operand and assign the result to left operand    | c *= a is equivalent to c = c * a       |
| /= Divide AND      | It divides left operand with the right operand and assign the result to left operand       | c /= a is equivalent to c = c / a       |
| %= Modulus AND     | It takes modulus using two operands and assign the result to left operand                  | c %= a is equivalent to c = c % a       |
| **= Exponent AND   | Performs exponential (power) calculation on operators and assign value to the left operand | c **= a is equivalent to c = c ** a     |
| //= Floor Division | It performs floor division on operators and assign value to the left operand               | c //= a is equivalent to c = c // a     |

### Bitwise Operators

| Operator                 | Description                                                                                   | Example                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| & Binary AND             | Operator copies a bit, to the result, if it exists in both operands                           | (a & b) (means 0000 1100)                                                                                       |
| \| Binary OR             | It copies a bit, if it exists in either operand.                                              | (a                                                                                 \| b) = 61 (means 0011 1101) |
| ^ Binary XOR             | It copies the bit, if it is set in one operand but not both.                                  | (a ^ b) = 49 (means 0011 0001)                                                                                  |
| ~ Binary Ones Complement | It is unary and has the effect of 'flipping' bits.                                            | (~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.                              |
| << Binary Left Shift     | The left operand's value is moved left by the number of bits specified by the right operand.  | a << 2 = 240 (means 1111 0000)                                                                                  |
| >> Binary Right Shift    | The left operand's value is moved right by the number of bits specified by the right operand. | a >> 2 = 15 (means 0000 1111)                                                                                   |

### Logical Operators

| Operator        | Description                                                          | Example               |
| --------------- | -------------------------------------------------------------------- | --------------------- |
| and Logical AND | If both the operands are true then condition becomes true.           | (a and b) is False.   |
| or Logical OR   | If any of the two operands are non-zero then condition becomes true. | (a or b) is True.     |
| not Logical NOT | Used to reverse the logical state of its operand.                    | Not(a and b) is True. |

### Membership Operators

| Operator | Description                                                                                      | Example                                                                    |
| -------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| in       | Evaluates to true if it finds a variable in the specified sequence and false otherwise.          | x in y, here in results in a 1 if x is a member of sequence y.             |
| not in   | Evaluates to true if it does not finds a variable in the specified sequence and false otherwise. | x not in y, here not in results in a 1 if x is not a member of sequence y. |

### Identity Operators

| Operator | Description                                                                                                     | Example                                                              |
| -------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| is       | Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. | x is y, here is results in 1 if id(x) equals id(y).                  |
| is not   | Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. | x is not y, here is not results in 1 if id(x) is not equal to id(y). |

### Operators Precedence

| Precedence | Operator | Description                         |
| :--------: | :------: | ----------------------------------- |
|     1      |    **    | Exponentiation (raise to the power) |
|     2      |    ~     | Complement                          |
|     2      |    +     | Unary plus     (+@)                 |
|     2      |    -     | Unary minus    (-@)                 |
|     3      |    *     | Multiply                            |
|     3      |    /     | Divide                              |
|     3      |    %     | Modulo                              |
|     3      |    //    | Floor division                      |
|     4      |    +     | Addition                            |
|     4      |    -     | Subtraction                         |
|     5      |    >>    | Right bitwise shift                 |
|     5      |    <<    | Left bitwise shift                  |
|     6      |    &     | Bitwise 'AND'                       |
|     7      |    ^     | Bitwise exclusive 'OR'              |
|     7      |    \|    | Regular 'OR'                        |
|     8      |    <=    | Less than or equal to               |
|     8      |    <     | Less than                           |
|     8      |    >     | More than                           |
|     8      |    >=    | More than or equal to               |
|     9      |    ==    | Equal to                            |
|     9      |    !=    | Not equal to                        |
|     10     |    =     | Assignment                          |
|     10     |    %=    | Modulus AND                         |
|     10     |    /=    | Divide AND                          |
|     10     |   //=    | Floor division AND                  |
|     10     |    -=    | Subtract AND                        |
|     10     |    +=    | Add AND                             |
|     10     |    *=    | Multiply AND                        |
|     10     |   **=    | Exponent AND                        |
|     11     |    is    | is                                  |
|     11     |  is not  | is not                              |
|     12     |    in    | in                                  |
|     12     |  not in  | not in                              |
|     13     |   not    | not                                 |
|     13     |    or    | or                                  |
|     13     |   and    | and                                 |