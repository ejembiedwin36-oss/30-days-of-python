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


# 1. Strings cannot be edited in place
text = "Hello"

# 2. Lists can be edited freely
my_list = [10, 20, 30]
my_list.append(40) 
my_list[0] = 99    

# 3. Tuples are locked lists
my_tuple = (10, 20, 30)
# my_tuple.append(40) <-- This will cause an ERROR!

# 4. Sets remove duplicates and don't care about order
my_set = {1, 2, 2, 3, 3, 3}
print(my_set) 


sentence = "I am a teacher and I love to inspire and teach people."
clean_sentence = sentence.replace(".", "").lower()
word_list = clean_sentence.split()

uniqu_word_set = set(word_list)
print(f"Oraginal word list (Length {len(word_list)}):")
print(word_list)

print(f"\nUnique word set (Length {len(uniqu_word_set)}):")
print(uniqu_word_set)