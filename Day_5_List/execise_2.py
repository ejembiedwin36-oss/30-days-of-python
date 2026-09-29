age = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
age.sort()
print(age, '\n')

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = min(ages)
max_age = max(ages)

ages.append(min_age)
ages.append(max_age)
print(ages)


ages =[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
n = len(ages)

if n % 2 == 1:
    midian = ages[n // 2]
else:
    middle1 = ages[(n // 2) - 1]
    middle2 = ages[n // 2]
    median = (middle1 + middle2) / 2
print(f"Sorted ages: {ages}")
print(f"The median age is: {median}")

average_age = sum(ages) / len(ages)
print(average_age)

age_range = max(ages) - min(ages)
print(f" The range of the ages is: {age_range}")

min_age = min(ages)
max_age = max(ages)

min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

print(f"Absolute distance from min to aerage: {min_diff}")
print(f"Absolute distance from max to average: {max_diff}")

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina']
n = len(countries)

middle_index = n // 2
if n % 2 == 1:
    middle_countries = [countries[middle_index]]
else:
    middle_countries = [countries[middle_index - 1], countries[middle_index]]
print(f"Total countries inlist: {n}")
print(f"The middle country(ies): {middle_countries}")

split_index = (len(countries) + 1) // 2
first_half = countries[:split_index]
second_half = countries[split_index:]

print(f"Total countries: {len(countries)}")
print(f"First half length: {len(first_half)}")
print(f"Second half length: {len(second_half)}")


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic_countries = countries
print(f"First Country: {country1}")
print(f"Second Country: {country2}")
print(f"Third Country: {country3}")
print(f"Scandic Countries: {scandic_countries}")