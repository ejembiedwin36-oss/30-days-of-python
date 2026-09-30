family_members = ('John', 'David', 'Mary', 'Jane', "Mr Joseph", "Mrs Margret")

# 1. Take the first 4 items (indexes 0, 1, 2, 3)
siblings = family_members[0:4]

# 2. Take everything from index 4 to the very end
parents = family_members[4:]

print("Siblings:", siblings)
# Output: ('John', 'David', 'Mary', 'Jane')

print("Parents:", parents)
# Output: ("Father's Name", "Mother's Name")
fruits = ('apple', 'orange', 'mango', 'lemon', 'banana')
vegetables = ('Spinach', 'Lettuce', ' Cabbage', 'Celery', 'Kale')
animal_products = ('meat', 'Dairy', 'poultry', 'seafood', )


food_stuff_tp = (fruits + vegetables + animal_products)
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print(food_stuff_lt[7:9])

