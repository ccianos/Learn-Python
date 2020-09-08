###############################
## Variables and Collections ##
###############################

# print function
print("Hello, beautiful Python!") # => Hello, beautiful Python! 

# Use optional end argument with print to toggle new line
print("Hello there", end="! ") # => Hello, beautiful Python! 

# Simple way to get data from console
input_string_var = input("Please enter some data: ")

# No declarations, only assignments.
# Convention is to use lowercase_with_underscore
some_var = 5
some_var # => 5

# Accessing an unassigned variable is an exception
# some_unkown_var # =>  Raises a NameError

# if can be used as an ternary-like expression 
"Woo!" if 0 > 1 else "Arrr!" # => 'Arrr!'

# Lists store sequences and can be prefilled during assigment
li = []
other_li = [4, 5, 6]

# Add to the list via the append method
li.append(1) # => li is now [1]
li.append(2) # => li is now [1, 2]
li.append(4) # => li is now [1, 2, 4]
li.append(3) # => li is now [1, 2, 4, 3]
# Remove an element from the list's end with pop by default,
# or at specified index.
li.pop() # => li is now [1, 2, 4]
li.append(3) # append 3 back
li # => [1, 2, 4, 3]

# Access a value of the list by index
li[0] # => 1
# Negative index reverses order of list traversal
li[-1] # => 3

# Out of bound lookup raises an IndexError
# li[4] # => IndexError: list index out of range

# Slice syntax is available to capture a range.
# Start index included while end is not
# li[start:end:step]
li[1:3] # => [2, 4]
li[2:] # [4, 3]
li[:3] # => [1, 2, 4]
li[::2] # => [1, 4]
li[::-1] # => [3, 4, 2, 1]

# Use slices to make a copy of a list 
li2 = li[:] # => [1, 2, 4, 3]. { li2 is li } results in false.

# del removes arbitray elements from the list 
del li[2] 
li # => [1, 2, 3]

# Remove first occurance of value
li.remove(2)
# li.remove(2) # => ValueError: list.remove(x): x not in list
li # => [1, 3]

# Insert a value at a specific element.
li.insert(1, 2)
li # => [1, 2, 3]

# Retrieve index of first occurance matching argument
li.index(2) # => 1
# li.index(4) # => ValueError: 4 is not in list

# We can add lists togeather.
# Values for li and other_li will not be modified
li + other_li # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with the method extend(),
# by appending elements from the iterable.
li.extend(other_li) 
li # => [1, 2, 3, 4, 5, 6]

# Check for the existence of a value
1 in li # => True
-1 in li # => False

# Examine length with len()
len(li) # => 6

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0] # => 1
#  tup[0] = 12 => TypeError: 'tuple' object does not support item assignment

# Single element length tuples must be followed by an appended comma
type((10,))  # => <class 'tuple'>
type((10, 9)) # => <class 'tuple'>
type((0))  # => () <class 'int'>
type(())  # => () <class 'tuple'>
type((10))  # => () <class 'int'>

# Most list operations can be called on tuples
len(tup) # => 3
tup + (4, 5, 12) # => (1, 2, 3, 4, 5, 6) 
tup[:2] # => (1, 2)
2 in tup[:2] # => True

# Unpack tuples and lists into variables
a, b, c = (3, 2, 1)
( a + b) ** (c / 2) # => 2.23606797749979
# Extended unpacking
a, *b, c = (1, 2, 3, 5, 4)
a # => a
b # => [2, 3, 5]
c # => 4
# Tuples are the default if a sequence is without parens or brackets
d, e, f = 4, 5, 6
# d => 4 
# e => 5
# f => 6
d, e = e, d # Swap d => 4, and e => 5  so d == 5 and e == 4 is True

# Dicitonaries mappning key and value pairs
empty_dictionary = {}
