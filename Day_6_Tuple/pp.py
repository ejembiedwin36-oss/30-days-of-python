# creating a Tuple
"""empty_tuple = ()
empty_tuple = tuple()

tpl = ('item1', 'item2', 'item3', 'item4')
firt_item = tpl[0]
second_item = tpl[1]
print(firt_item)     # item1
print(second_item)   # item2
print(tpl[::-1])  # revers



# possitive indexing to access tuple item
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(first_fruit)    # banana
print(second_fruit)   # orange
print(last_index)     # 3
print(fruits[::-1])  # revers
print(last_fruit, '\n')     # lemon


# nagative indexing to access tuple item
tple = ('item1', 'item2', 'item3', 'item4')
first_item = tple[-4]  # item2
second_item = tple[-3] # item2
print(first_item)
print(second_item)
print(fruits[::-1])  # revers

fruit = ('banana', 'mango', 'orange', 'lemon')
first_fruits = fruit[-4]  # banana
second_fruits = fruit[-3] # mango
last_fruits = fruit[-1]   # lemon
print(first_fruits)
print(second_fruits)
print(last_fruits)
print(fruits[::-1])  # revers
print('Next is Slicing tuples \n')

# slicing tuple (positive)
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]
all_items = tpl[0:]
middle_two_items = tpl[1:3]
print(all_items)
print(all_items)
print(middle_two_items)
print(fruits[::-1])  # revers


friuts = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]
print(all_fruits)
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)
print(fruits[::-1])   # revers

# Range of Negative Indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]
middle_two_items = tpl[-3:-1]
print(all_items)
print(middle_two_items)


fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1] 
orange_to_the_rest = fruits[-3:]
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)"""


#Changing Tuples to Lists
names = ('joy', 'loveth', 'mercy', 'blessing')
names = list(names)
names[0] = 'peter'
print(names)
names = tuple(names)
print(names)

# Checking an Item in a Tuple
names = ('joy', 'loveth', 'mercy', 'blessing')
print('loveth' in names)

# Joining Tuples
tpl1 = ('banana', 'mango', 'orange', 'lemon')
tpl2 = ('item1', 'item2', 'item3', 'item4')
tpl3 = tpl1 + tpl2
print(tpl3)

# Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits)  # it shows error
