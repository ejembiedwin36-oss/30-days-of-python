
"""for num in range(1, 10):
    print(num)

    # Slicing Items from a List

fruit = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruit[0:4]

all_fruits = fruit[0:]
orange_and_mango = fruit[1:3]
orange_mango_and_lemon = fruit[1:]
orange_and_lemon = fruit[::2]
every_thing = all_fruits, orange_and_lemon, orange_mango_and_lemon, orange_and_lemon
print(every_thing, '\n')"""

#nagative indexing
fruits = ['banana', 'orange', 'mango', 'lemon']

all_fruits = fruits[-4:] 
orange_and_mango = fruits[-3:-1] 
orange_mango_lemon = fruits[-3:] 
reverse_fruits = fruits[::-1]
reverse_every_fruits = all_fruits, orange_and_mango, orange_mango_lemon, reverse_fruits
print(reverse_every_fruits)

