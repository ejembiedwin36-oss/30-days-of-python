person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check for 'skills' key and print the middle skill
if 'skills' in person and person['skills']:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    print(skills_list[middle_index])

# 2. Check for 'skills' key and check if 'Python' exists
if 'skills' in person:
    print('Python' in person['skills'])

# 3. Determine the developer role based on skills
if 'skills' in person:
    skills_set = set(person['skills'])
    
    # Using .issubset() to check if the required skill combinations exist
    if skills_set == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print('unknown title')

# 4. Check marital status and country, then print in the requested format
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
