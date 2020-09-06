# A single line comment

"""
Multiline comments
can be had with a pair of
triple double quotes. 
"""

# Numbers
3 # => 3

# Basic arithimetic
1 + 1 # => 2
8 - 1 # => 7
10 * 2 # => 20
35 / 5 # => 7

# Integer division rounds down for positive and negative numbers
5 // 3 # => 1
-5 // 3 # => -2
5.0 // 3.0 # => 1.0
-5.0 // 3.0 # => -2.0

# Division always results in a float
10 / 3 # => 3.3333333333333335 

# Modulo
7 % 3 # => 1

# Exponents
2 ** 3 # => 8

# Specify precedence with parens
1 + 3 * 2 # => 7
(1 + 3) * 2 # => 8

# Boolean values are primitives
True # => True
False #  => False

# Negation with not keyword
not True # => False
not False # => True

# Boolean operations
True and True # => True
False and True # => False
False and False # => False
True and False # => False

True or True # => True
True or False # => True
False or False # => False
False or True # => True

# True and False are essentially keywords for 1 and 0 respectively
True + True # => 2
True * 8 # => 8
False - 5 # -5

# Numerical value of True and False utilized by comparison operators during evaluation
0 == False # => True
1 == True # => True
2 == True # => False
-5 != True # => True

# Use of boolean logical operators with ints cast ints as boolean during eval but returns orignal non-cast value
bool(0) # => False
bool(4) # => True
bool(-6) # => True
0 and 2 # => 0
-5 or 0 # => -5

# Equality
1 == 1 # => True
2 == 1 # => False

# Inequality
1 != 1 # => False
2 != 1 # => True

# Additional comparisons
1 < 10 # => True
1 > 10 # => False
2 <= 2 # => True
2 >= 2 # True

# Test for a value within a range
1 < 2 and 2 < 3 # => True
2 < 3 and 3 < 2 # => False

# Test for a value within a range with chaining
1 < 2 < 3 # => True
2 < 3 < 2 # => False

# is checks if two vars are referencing the identical object, vs
# == which tests if objects have equality of value.
a = [1, 2, 3, 4] # => declare var a as reference to new list
b = a # =>  declar var b and point it to same object a references
b is a # => True
b == a # => True
b = [1, 2, 3, 4] # => assign b as reference to new list object
b is a # => False, different objects referenced
b == a # => True, object have same value

# Strings
"Double quote string." # => 'Double quote string.'
'Single quote string.' # => 'Single quote string.'

# Concatenate strings with the + operator should be avoided
"Hello " + "Python!" # => 'Hello Python!'
# non-variable based string literals can be concatenated via juxposition
"Hello " "Python!" # => 'Hello Python!'

# We can reference a char at the index of string
"This is a sequence of chars"[10] # => 's'

# Query length of string
len("This is a sequence of chars") # => 27

# Format using f-strings for formatted string literals
name = "Charlie"