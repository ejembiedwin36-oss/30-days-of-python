dog = {}

dog.update({
    'Name': 'loveth',
    'Color': 'red',
    'Breed': 'breed retriever',
    'Leg': 4,
    'Age': 3,
})
print(dog)

# another way of it
"""
# 2. Now you can add items to it
dog['name'] = 'Loveth'
dog['color'] = 'Red'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3

print(dog)
"""

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

res = student
print(len(res))

student_skills = student['skills']
print("skills value:0", student_skills)

skills_type = type(student_skills)
print("Data type:", skills_type)
print('Modifying Items in a Dictionary')

student['skills'] = ['python', 'java'],
print(student, '\n')

student_keys = list(student.keys())
print(student_keys, '\n')

student_values = list(student.values())
print(student_values)