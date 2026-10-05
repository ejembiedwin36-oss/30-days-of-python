
# Create an empty dictionary for the dog
dog = {}

# Populate the dog dictionary with multiple attributes at once using the update method
dog.update({
    'Name': 'loveth',
    'Color': 'red',
    'Breed': 'breed retriever',
    'Leg': 4,
    'Age': 3,
})
print(dog)

# Alternative method (Commented out): Individual key assignment
"""
# Initialize and add key-value pairs one by one
dog = {}
dog['name'] = 'Loveth'
dog['color'] = 'Red'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3
print(dog)
"""

# Create and initialize a student dictionary with personal details and skills
student = {
    'first_name' : 'Edwin',
    'last_name' : 'Ejembi', 
    'gender' : 'Male',
    'age' : 23,
    'marrital_status' : 'False',
    'skills' : {'graphic designer', 'pragrammer', 'driver'},
    'counry' : 'Nigerai', 
    'city' : 'otukpo',
    'address' : 'housa quater',
}
print(student)

# Reference the student dictionary and get the total number of keys (length)
res = student
print(len(res))

# Access and print the specific value assigned to the 'skills' key
student_skills = student['skills']
print("skills value:", student_skills)

# Check and print the data type of the 'skills' value (currently a Set)
skills_type = type(student_skills)
print("Data type:", skills_type)

print('Modifying Items in a Dictionary')

# Modify the 'skills' key by overwriting it with a new list of programming languages
student['skills'] = ['python', 'java']  # Fixed: Removed the trailing comma
print(student, '\n')

# Extract all keys from the student dictionary and convert them into a list
student_keys = list(student.keys())
print(student_keys, '\n')

# Extract all values from the student dictionary and convert them into a list
student_values = list(student.values())
print(student_values, '\n')

# Convert the dictionary into a list of (key, value) tuples using the items() method
student_tuples = list(student.items())
print(student_tuples, '\n')

# Delete a single specific key-value pair ('age') from the student dictionary
del student['age']
print(student)

# Completely delete the student dictionary variable from memory
del student
