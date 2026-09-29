# ==========================================
# PART 1: SORTING A LIST
# ==========================================

# Create an initial list of student ages
age = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# .sort() arranges the list items in ascending order (smallest to largest) permanently
age.sort()

# Print the sorted list, followed by an extra newline character ('\n') for spacing
print(age, '\n')


# ==========================================
# PART 2: FINDING & APPENDING MIN/MAX VALUES
# ==========================================

# Resetting the base list to work with
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# min() finds the smallest number in the list (19)
min_age = min(ages)

# max() finds the largest number in the list (26)
max_age = max(ages)

# .append() adds the minimum age (19) to the very end of the list
ages.append(min_age)

# .append() adds the maximum age (26) to the very end of the list
ages.append(max_age)

# Print the new 12-item list: [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]
print(ages)


# ==========================================
# PART 3: CALCULATING THE MEDIAN (MIDDLE VALUE)
# ==========================================

# Sort the updated 12-item list so we can accurately find the middle items
ages.sort()

# len() counts the total number of items currently in the list (now 12)
n = len(ages)

# The % (modulo) operator checks for a remainder when dividing by 2
if n % 2 == 1:
    # If the remainder is 1, the list length is ODD.
    # // is floor division; it finds the exact single middle index
    median = ages[n // 2]
else:
    # If the remainder is 0, the list length is EVEN.
    # We must find the two middle items and calculate their average.
    # Example for 12 items: index 5 (6th item) and index 6 (7th item)
    middle1 = ages[(n // 2) - 1]
    middle2 = ages[n // 2]
    median = (middle1 + middle2) / 2

# Print the sorted 12-item list and the resulting median value
print(f"Sorted ages: {ages}")
print(f"The median age is: {median}")


# ==========================================
# PART 4: AVERAGE & RANGE
# ==========================================

# sum() adds all numbers together. Dividing by len() calculates the mean (average)
average_age = sum(ages) / len(ages)
print(average_age)

# Range is calculated by subtracting the smallest number from the largest number
age_range = max(ages) - min(ages)
print(f"The range of the ages is: {age_range}")


# ==========================================
# PART 5: ABSOLUTE DIFFERENCES
# ==========================================

# Fetch the min and max numbers again from our current list
min_age = min(ages)
max_age = max(ages)

# abs() turns any negative result into a positive number (absolute distance)
# Example: abs(19 - 22.75) becomes abs(-3.75), which outputs 3.75
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

# Print out how far away the min and max values sit from the overall average
print(f"Absolute distance from min to average: {min_diff}")
print(f"Absolute distance from max to average: {max_diff}")


# ==========================================
# PART 6: FINDING THE MIDDLE OF A LIST
# ==========================================

# An example list containing 6 country names
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina']
n = len(countries)

# Find the middle mathematical pivot point using floor division
middle_index = n // 2

if n % 2 == 1:
    # For an ODD list length, create a list wrapping the single center country
    middle_countries = [countries[middle_index]]
else:
    # For an EVEN list length, collect the two elements framing the center line
    middle_countries = [countries[middle_index - 1], countries[middle_index]]

print(f"Total countries in list: {n}")
print(f"The middle country(ies): {middle_countries}")


# ==========================================
# PART 7: SPLITTING A LIST INTO TWO HALVES
# ==========================================

# Adding 1 before floor division ensures an extra item lands in the first list if 'n' is odd
split_index = (len(countries) + 1) // 2

# Slicing notation [:split_index] copies items from index 0 up to (but excluding) the split index
first_half = countries[:split_index]

# Slicing notation [split_index:] copies items from the split index to the very end of the list
second_half = countries[split_index:]

# Print verification sizes to prove the list split successfully
print(f"Total countries: {len(countries)}")
print(f"First half length: {len(first_half)}")
print(f"Second half length: {len(second_half)}")


# ==========================================
# PART 8: LIST UNPACKING WITH OPERATORS
# ==========================================

# A specific mixed list of country names
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Unpacking maps indices 0, 1, and 2 directly to country1, country2, and country3.
# The * operator gathers ALL remaining items into a brand-new list named scandic_countries.
country1, country2, country3, *scandic_countries = countries

# Print the three unpacked string variables and the final gathered sublist
print(f"First Country: {country1}")
print(f"Second Country: {country2}")
print(f"Third Country: {country3}")
print(f"Scandic Countries: {scandic_countries}")
