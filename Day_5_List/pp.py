# pp Means personal practical.
"""empty_list = [] # list()
print(len(empty_list))

# Lists with initial values. We use len() to find the length of a list.

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_tech = ['HTML', 'CSS', 'JS', 'React', 'Rudux', 'NOde', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norwa']

# print the list and it's lenght 
print('Fruits:', fruits)
print('Number of fruits', len(fruits))
print('Vegetables:', vegetables)
print('Number of Vegetables:', len(vegetables))
print('Animal_products:', animal_products)
print('Number of animal_products:', len(animal_products))
print('Web_technologies:', web_tech)
print('Number of web technologies:', len(web_tech))
print('Countries:', countries)
print('Number of countries:', len(countries))"""

# Accessing List Items Using Positive Indexing

Fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = Fruits[0]
print(first_fruit) # banana
second_fruits = Fruits[1]
print(second_fruits)  # orange
third_fruits = Fruits[2]
print(third_fruits)  # mango
last_fruits = Fruits[3]
print(last_fruits, "\n")  # lemon


# Accessing List Items Using Negative Indexing


Fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = Fruits[-4]
print(first_fruit) # banana
second_fruits = Fruits[-1]
print(second_fruits)  # orange
third_fruits = Fruits[-2]
print(third_fruits)  # mango
last_fruits = Fruits[-3]
print(last_fruits, '\n')  # lemon

# another Method.(Reverse)
first_fruit = Fruits[-1]
print(first_fruit) # banana
second_fruits = Fruits[-2]
print(second_fruits)  # orange
third_fruits = Fruits[-3]
print(third_fruits)  # mango
last_fruits = Fruits[-4]
print(last_fruits)  # lemon
print(Fruits)
print(Fruits[::-1])



# Unpacking List Items
lst = ['item1', 'item2', 'item3', '[item4]', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

# First Example
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruits, third_fruits, *rest = fruits
print(first_fruit)
print(second_fruits)
print(third_fruits)
print(rest)

# Second Example about unpacking list
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)


# Third Example about unpacking list
countries = ['Germany', 'France', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(countries)
print(es)

# Slicing Items from a List
#positive indexing
fruit = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruit[0:4]

all_fruits = fruit[0:]
orange_and_mango = fruit[1:3]
orange_mango_and_lemon = fruit[1:]
orange_and_lemon = fruit[::2]
every_thing = all_fruits, orange_and_lemon, orange_mango_and_lemon, orange_and_lemon
print(every_thing)

#nagative indexing
all_fruits = fruits[-4:] 
orange_and_mango = fruits[-3:-1] 
orange_mango_lemon = fruits[-3:] 
reverse_fruits = fruits[::-1]
reverse_every_fruits = all_fruits, orange_and_mango, orange_mango_lemon, reverse_fruits
print(reverse_every_fruits)


# List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False