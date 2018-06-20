import sys
print(sys.version_info)
print(sys.version)

# In[]
my_values = {'red':['5'],'green':[''], 'blue': ['0']}
my_values.get('red')
my_values.get('green',[''])[0] or 0
red = my_values.get('red',[""])
red = int(red[0]) if red[0] else 0
red

# In[]
values = [100,57,15,1,12,75,5,86,89,11]
it = (x for x in values)
print(it)
print(next(it))
for value in values:
    print(value)

# In[]
flavor_list = ['vanilla','chocolate','pecan','strawberry']
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
