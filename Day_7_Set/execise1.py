it_companies = {'Google', 'meta', 'Youtub', 'Facabook'}
it_companies.add('Twitter')
print(it_companies)

st1 = {'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7'}
st2 = {'item3', 'item5'}
st3 = st1.intersection(st2)
print(st3)


val = {'toyotal', 'lexus', 'corolar', 'picnic'}
val.remove('corolar')
print(val)

fruits = {'apple', 'banana', 'orange', 'cherry'}
# .remove() raises a keyerror and crashes your program 
fruits.remove('apple')
# .discard() does notthing and lets you code continue running smoothly
fruits.discard("banana")
print(fruits)
