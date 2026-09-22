# As i study i practice at the moment 
"""def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
print(all)"""

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument


first_name, last_name, city, contry, work = 'Edwin', 'Ejembi', 'at Otukpo', 'in Nigeria', 'as teacher'
print(first_name, last_name, city, contry, work)
print('First_name: ', first_name)
print('Last_name: ', last_name)
print('City:' , city)
print('Contry:' , contry)
print('Work:' , work)

"""first_name = input('what is your name: ')
age = input('how old are you: ')
gender = input('Are you a male or female: ')
skills = input('which skill do you learn: ')
print(first_name)
print(age)



print(type(first_name))
print(type(age))
print(type(gender))
print(type(20))
print(type('34'))
print(type(2.5))
print(type(2 + 4))
print(type([1, 2, 3, 4, 5]))
print(type([1,2,3]))
print(type(zip([1,3],[2,4])))  
print(type(True))
print(type({'name:', 'Edwin'}))"""


#convertion:
# int to float

num_int = 10
print('num_int ', num_int)
num_float = float(num_int)
print('num_float:', num_float)


# float to int
gravity = 10.0
print(int(gravity))




# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'


# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

