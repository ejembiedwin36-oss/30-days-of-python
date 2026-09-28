# --- Creating Abbreviations ---
# Splits the string into words, takes the first letter of each word, and joins them together.
my_variable = "Python For Everyone"
print("".join(w[0] for w in my_variable.split()))  # Output: PFE

# Splits the string and takes the first letter of each word to make an abbreviation.
abb_name = "Coding For All"
print("".join(w[0] for w in abb_name.split()))  # Output: CFA


# --- Finding Character Positions (Index) ---
# Finds the index (position) of the first occurrence of 'C'.
var = "Coding For All"
print(var.index('C'))  # Output: 0

# Finds the index (position) of the first occurrence of 'F'.
my_var = "Coding For All"
print(my_var.index('F'))  # Output: 7

# rfind searches from right to left and finds the last position of 'l'.
text = "Coding For All People"
print(text.rfind('l'))  # Output: 19

# find searches from left to right and finds the position of the first 'because'.
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))  # Output: 31


# --- Advanced Substring Searching & Counting ---
sentence = "You cannot end a sentence with because because because is a conjunction"
# rfind finds the start position of the very last "because" in the string.
print("Last position:", sentence.rfind("because"))

# count counts how many times the word "because" appears in the string.
print("Total count:", sentence.count("because"))

# rindex works like rfind to find the last position of "because", but raises an error if not found.
char = "You cannot end a sentence with because because because is a conjunction"
print(char.rindex("because"))


# --- Slicing Strings ---
# Extracts a specific section (substring) from index 31 up to (but not including) index 54.
phrase = "You cannot end a sentence with because because because is a conjunction"
my_phrase = phrase[31:54]
print(my_phrase)  # Output: "because because because"


# --- Checking String Content ---
# Checks if the string starts with the word "Coding" (returns True or False).
box = "Coding For All"
print(box.startswith("Coding"))

# Checks if the string ends with the word "coding" (returns False because Python is case-sensitive).
res = "coding for all"
print(res.endswith("coding"))

# strip removes any leading (front) and trailing (back) spaces from the string.
remove_space = " Coding For All "
print(remove_space.strip())


# --- Variable Name Validation ---
# Checks if "30DaysOfPython" is a valid variable name (False, because it starts with a number).
print("30DaysOfPython".isidentifier())

# Checks if "thirty_days_of_python" is a valid variable name (True, letters and underscores are valid).
print("thirty_days_of_python".isidentifier())


# --- Joining Lists into Strings ---
# Combines elements of a list into a single string, separated by a comma and a space.
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
result = ", ".join(libraries)
print(result)


# --- Escape Characters ---
# \n creates a new line break in the text.
sequence = "I am enjoying this challenge\nI just wonder what is next"
print(sequence)

# \t creates a tab space to align text nicely like a table.
escape_sequence = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(escape_sequence)


# --- F-String Formatting & Math Operations ---
# Calculates circle area and uses an f-string to turn the float answer into a whole integer.
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# Mathematical calculations formatted cleanly inside f-strings.
a = 8
b = 6
print(f"{a} + {b} = {a + b}")    # Addition
print(f"{a} - {b} = {a - b}")    # Subtraction
print(f"{a} * {b} = {a * b}")    # Multiplication
print(f"{a} / {b} = {a / b:.2f}") # Division (formatted to show 2 decimal places)
print(f"{a} % {b} = {a % b}")    # Modulus (returns the remainder of division)
print(f"{a} // {b} = {a // b}")  # Floor Division (divides and rounds down to whole number)
print(f"{a} ** {b} = {a ** b}")  # Exponentiation (8 to the power of 6)
