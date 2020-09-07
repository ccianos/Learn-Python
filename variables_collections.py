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
li[0]

# Negative index reverses order of list traversal
li[-1]