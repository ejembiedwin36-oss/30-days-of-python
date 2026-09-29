"""empty_list = []  # list()
lst = ['melon', 'applle', 'mango', 'orange', 'banana', 'pawpaw', 'lime']
find_lst = len(lst)
print(find_lst)

get = lst[0], lst[3], lst[6]
print(get, '\n')

mixed_list = ['Edwin', 35, 9.65, 'single', 'housa quaters zaria street 9']
print
(mixed_list)


companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(len(companies))
print(companies[0])
print(companies[4])
print(companies[6])


companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies[3] = 'Amasco'
print(companies)

companies.append('IT')
print(companies)

companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

companies.insert(4, 'IT')
print(companies)

company_plural = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
company_plural[4] = company_plural[4].upper()
print(company_plural)


company_plural = '#; '.join(company_plural)
print(company_plural)
company = 'Google'
if company in company_plural:
    print(f'Yes {company} exist in the companies list')
else:
    print(f'No {company} do not exist in the companies list.')


name_of_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
name_of_companies.sort()
print(name_of_companies)

arrange = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
arrange.sort(reverse=True)
print(arrange)


slising  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(slising)
print(slising[:3])
print(slising[4:7])
print(slising[3])
slising.remove('Facebook')
print(slising)
slising.remove('Apple')
print(slising)
slising.remove('Amazon')
print(slising)
slising.clear()
print(slising)"""



# destroying a list
#scater_list = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#print(scater_list)
#del scater_list
#print(scater_list)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Method 1: Using the + operator (Creates a brand new list)
full_stack = front_end + back_end

print(full_stack)
# Output: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']




front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# 1. Join the lists first
joined_list = front_end + back_end

# 2. Copy the joined list safely and assign it to full_stack
full_stack = joined_list.copy()

# 3. Find where 'Redux' is, so we know where to insert our new languages
# 'Redux' is at index 4, so we want the next items at index 5 and 6
redux_index = full_stack.index('Redux')

# 4. Insert 'Python' right after Redux (at index 5)
full_stack.insert(redux_index + 1, 'Python')

# 5. Insert 'SQL' right after Python (at index 6)
full_stack.insert(redux_index + 2, 'SQL')

# Print the final result
print(full_stack)



# use ai to comment them.

# --- 1. Working with Fruit Lists ---
# Declaring an empty list using square brackets or the list() constructor function
empty_list = []  

# Creating a list of fruit strings
lst = ['melon', 'applle', 'mango', 'orange', 'banana', 'pawpaw', 'lime']

# Counts the number of items inside 'lst' and prints the length (7)
find_lst = len(lst)
print(find_lst)

# Grabs items at indexes 0, 3, and 6 to create a Tuple, then prints it with a newline break
get = lst[0], lst[3], lst[6]
print(get, '\n')


# --- 2. Mixed Data Types ---
# Declaring a list containing a String, Integer, Float, and your address text
mixed_list = ['Edwin', 35, 9.65, 'single', 'housa quaters zaria street 9']
print(mixed_list)


# --- 3. Indexing & Counting Companies ---
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(len(companies))    # Prints the total number of companies (7)
print(companies[0])      # Prints the 1st company at index 0 (Facebook)
print(companies[4])      # Prints the 5th company at index 4 (IBM)
print(companies[6])      # Prints the 7th company at index 6 (Amazon)


# --- 4. Modifying and Appending Items ---
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies[3] = 'Amasco'  # Modifies index 3 by replacing 'Apple' with 'Amasco'
print(companies)

companies.append('IT')   # Adds the item 'IT' to the absolute end of the list
print(companies)


# --- 5. Inserting at Specific Positions ---
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies.insert(4, 'IT') # Injects 'IT' directly into index position 4, shifting others right
print(companies)


# --- 6. Formatting Strings & Searching ---
company_plural = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
company_plural[4] = company_plural[4].upper() # Uppercases only the item at index 4 ('IBM')
print(company_plural)

# Glues all items in the list together into one single string separated by '#; '
company_plural = '#; '.join(company_plural)
print(company_plural)

company = 'Google'
# Checks if the word 'Google' can be found anywhere inside the joined text string
if company in company_plural:
    print(f'Yes {company} exist in the companies list')
else:
    print(f'No {company} do not exist in the companies list.')


# --- 7. Sorting Lists Alphabetically ---
name_of_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
name_of_companies.sort() # Rearranges the items permanently in alphabetical order (A to Z)
print(name_of_companies)

arrange = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
arrange.sort(reverse=True) # Rearranges the items permanently in reverse alphabetical order (Z to A)
print(arrange)


# --- 8. Slicing and Deleting Specific Items ---
slising = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(slising)
print(slising[:3])   # Slices out the first 3 items from index 0 up to (but excluding) 3
print(slising[4:7])  # Slices items starting from index 4 up to index 6
print(slising[3])    # Prints the single item sitting precisely at index 3 ('Apple')

slising.remove('Facebook') # Searches for 'Facebook' and deletes it from the list
print(slising)
slising.remove('Apple')    # Searches for 'Apple' and deletes it from the list
print(slising)
slising.remove('Amazon')   # Searches for 'Amazon' and deletes it from the list
print(slising)

slising.clear()      # Wipes out all remaining items, leaving the list completely empty ([])
print(slising)


# --- 9. Joining Basic Lists ---
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Uses the '+' operator to combine both lists into a single brand-new list
full_stack = front_end + back_end
print(full_stack)


# --- 10. Copying Lists and Selective Insertion ---
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Joins front_end and back_end into a temporary list variable
joined_list = front_end + back_end

# Creates a safe, independent copy clone of the list and saves it as full_stack
full_stack = joined_list.copy()

# Locates the exact position number of 'Redux' in the list (index 4)
redux_index = full_stack.index('Redux')

# Injects 'Python' right after 'Redux' by targeting index position 5
full_stack.insert(redux_index + 1, 'Python')

# Injects 'SQL' right after 'Python' by targeting index position 6
full_stack.insert(redux_index + 2, 'SQL')

# Prints the completely assembled full-stack developer portfolio list
print(full_stack)
