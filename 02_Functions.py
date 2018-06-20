# Item14
if not None:
    print('if statement is run')
if not True:
    print('if statement is run')
if not False:
    print('if statement is run')
if 0 is None:
    print('if statement is run')
if 0 is False:
    print('if statement is run')
if 0 == False:
    print('if statement is run')

# In[] Item15
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sort_priority(numbers, group)
print(numbers)

# In[] Item16 Use not list.append but generator (yield)
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text,1):
        if letter == ' ':
            yield index
test_text = 'Four score and seven years ago...'
result = index_words_iter(test_text)
for i in result:
    print(i, end=',')

# In[] Item17
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result

visits = [15,35,80]
percentages = normalize(visits)
print(percentages)

def read_visits_test():
    yield 15
    yield 35
    yield 80
it = read_visits_test()
percentages = normalize(it)
print(percentages)

def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100*value/total
        result.append(percent)
    return result

percentages = normalize_func(lambda: read_visits_test())
percentages

iter(read_visits_test())
iter(read_visits_test())

class ReadVisits(object):
    def __iter__(self):
        yield 15
        yield 35
        yield 80

def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers): # An iterator — bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15,35,80]
normalize_defensive(visits)
visits = ReadVisits()
normalize_defensive(visits)
it = iter(visits)
normalize_defensive(it)

# In[] Item21
1e500
1 / (10**500)
