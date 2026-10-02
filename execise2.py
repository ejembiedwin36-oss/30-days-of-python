a = {'item1', 'item2', 'item3', 'item4'}
b = {'item5', 'item6', 'item7', 'item6'}
c = a.union(b)
print(c)


a = {'item1', 'item2', 'item3', 'item4'}
b = {'item5', 'item6', 'item7', 'item6'}
d = a.union(b)
print(d)

bag = {'item1', 'item2', 'item3', 'item4'}
box = {'item5', 'item1', 'item4', 'item6'}
bag.intersection(box)
print(bag)
box.intersection(bag)
print(box)

A = {'mango', 'apple', 'banana'}
B = {'lemon', 'orange', 'cherry'}
x = A.union(B)
print(x)
w = B.union(A)
print(w)


A = {'mango', 'apple', 'banana'}
B = {'lemon', 'orange', 'cherry'}

# Find items unique to A and unique to B
result = A.symmetric_difference(B)
print(result)

char = del result
print(char)