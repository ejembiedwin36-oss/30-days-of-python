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
# slice out the first three and last three item
print(food_stuff_lt[0:2])
print(food_stuff_lt[11:])
print(len(food_stuff_lt))


#char = del food_stuff_lt
#print(char)
result = ('mango' in food_stuff_lt)
print(result)

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
verify_countries = ('Estonia' in nordic_countries)
print(verify_countries)
go_again = ('Iceland' in nordic_countries)
print(go_again)