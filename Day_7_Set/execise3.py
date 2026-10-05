ages_list = [25, 30, 40, 25, 30, 18, 40]

ages_set = set(ages_list)

list_length = len(ages_list)
set_length = len(ages_set)

print(f"Original List: {ages_list} (Length: {list_length})")
print(f"Unique Set:  {ages_set} (Length: {set_length})\n")


if list_length > set_length:
    print(f"The LIST is bigger by {list_length - set_length} item(s) because there were duplicate ages.")
else:
    print(f"Both are the SAME size because all ages in the list were already unique.")


# String is a text. it is a sequence of character locked inside quotation marks.
# example: name = "python"

# List is an odered collection of items inside square brackets. 
# example : my_list = ['apple', 'banana', 'orange']

# Tuple is similar to list but uses parentheses.
# example: my_location = (40.7128, -74.0060)

# Set is an unordered collection of items inside curly braces.
# example: unique_ids = {101, 102, 103}
