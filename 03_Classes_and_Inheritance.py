# Item 22 Prefer Helper Classes Over Bookkeeping with Dictionaries and Tuples
class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Issac Newton')
book.report_grade('Issac Newton', 90)
print(book.average_grade('Issac Newton'))

class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
book.average_grade('Albert Einstein')

# test
dic = {}
lis = dic.setdefault('abc',[])
lis
dic
lis = dic.setdefault('abc','aaa')
dic

import collections
Grade = collections.namedtuple('Grade',('score','weight'))
class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)
albert.average_grade()

# In[] Item 23
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)

def log_missing():
    print('Key added')
    return 0

current = {'green':12, 'blue':3}
increments = [('red',5),
              ('blue', 17),
              ('orange', 9)]
result = collections.defaultdict(log_missing, current)
print('Before', dict(result))
for key, amount in increments:
    result[key] += amount
print('After: ', dict(result))

def increments_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = collections.defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increments_with_report(current, increments)
assert count == 2

class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = collections.defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2

class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
assert callable(counter)
result = collections.defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
