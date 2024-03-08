def all_elements_true(t):
    return all(t)

# Input a sequence of values separated by spaces
input_string = input("Enter a sequence of values separated by spaces: ")

# Split the input string into a list of strings
values_list = input_string.split()

# Convert each string to a boolean value and create a tuple
boolean_values = [bool(value) for value in values_list]
user_tuple = tuple(boolean_values)

# Call the function to check if all elements of the tuple are true
result = all_elements_true(user_tuple)

print("All elements of the tuple are True:", result)