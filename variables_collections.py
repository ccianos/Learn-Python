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