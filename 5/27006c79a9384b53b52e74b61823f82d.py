import collections

# Point = collections.namedtuple("Point", ['x', 'y'])
# namedtuple()
# >>> # Basic example
# >>> Point = namedtuple('Point', ['x', 'y'])
# >>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
# >>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
# 33
# >>> x, y = p                # unpack like a regular tuple
# >>> x, y
# (11, 22)
# >>> p.x + p.y               # fields also accessible by name
# 33
# >>> p                       # readable __repr__ with a name=value style
# Point(x=11, y=22)
#
# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
# comma separated values
# id,name,value,age
# 1,2,3,4,5,6

# import csv
# for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
#     print(emp.name, emp.title)
#
# import sqlite3
# conn = sqlite3.connect('/companydata')
# cursor = conn.cursor()
# cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
# for emp in map(EmployeeRecord._make, cursor.fetchall()):
#     print(emp.name, emp.title)


# deque
# >>> from collections import deque
# >>> d = deque('ghi')                 # make a new deque with three items
# >>> for elem in d:                   # iterate over the deque's elements
# ...     print(elem.upper())
# G
# H
# I
#
# >>> d.append('j')                    # add a new entry to the right side
# >>> d.appendleft('f')                # add a new entry to the left side
# >>> d                                # show the representation of the deque
# deque(['f', 'g', 'h', 'i', 'j'])
#
# >>> d.pop()                          # return and remove the rightmost item
# 'j'
# >>> d.popleft()                      # return and remove the leftmost item
# 'f'
# >>> list(d)                          # list the contents of the deque
# ['g', 'h', 'i']
# >>> d[0]                             # peek at leftmost item
# 'g'
# >>> d[-1]                            # peek at rightmost item
# 'i'
#
# >>> list(reversed(d))                # list the contents of a deque in reverse
# ['i', 'h', 'g']
# >>> 'h' in d                         # search the deque
# True
# >>> d.extend('jkl')                  # add multiple elements at once
# >>> d
# deque(['g', 'h', 'i', 'j', 'k', 'l'])
# >>> d.rotate(1)                      # right rotation
# >>> d
# deque(['l', 'g', 'h', 'i', 'j', 'k'])
# >>> d.rotate(-1)                     # left rotation
# >>> d
# deque(['g', 'h', 'i', 'j', 'k', 'l'])
#
# >>> deque(reversed(d))               # make a new deque in reverse order
# deque(['l', 'k', 'j', 'i', 'h', 'g'])
# >>> d.clear()                        # empty the deque
# >>> d.pop()                          # cannot pop from an empty deque
# Traceback (most recent call last):
#     File "<pyshell#6>", line 1, in -toplevel-
#         d.pop()
# IndexError: pop from an empty deque
#
# >>> d.extendleft('abc')              # extendleft() reverses the input order
# >>> d
# deque(['c', 'b', 'a'])


# stat = dict()
#
# s = "awdwwdadawdwdwaadwdawdad"
#
# for i in s:
#     if i in stat:
#         stat[i] += 1
#     else:
#         stat[i] = 1
#
# print(stat)

# s = "awdwwdadawdwdwaadwdawdad"
# c = collections.Counter(s)
#
# print(c.most_common(2))
# print(list(c.elements()))
# print(c)
#
# s = "London is a capital of the GB London London is "
# c = collections.Counter(s.split(' '))
#
# print(c.most_common(2))
# print(list(c.elements()))
# print(c)
# Counter
# >>> c = Counter()                           # a new, empty counter
# >>> c = Counter('gallahad')                 # a new counter from an iterable
# >>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
# >>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args
#
# >>> c = Counter(a=4, b=2, c=0, d=-2)
# >>> sorted(c.elements())
# ['a', 'a', 'a', 'a', 'b', 'b']
#
# >>> Counter('abracadabra').most_common(3)  # doctest: +SKIP
# [('a', 5), ('r', 2), ('b', 2)]
#
# >>> c = Counter(a=4, b=2, c=0, d=-2)
# >>> d = Counter(a=1, b=2, c=3, d=4)
# >>> c.subtract(d)
# >>> c
# Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
#
# >>> c = Counter(a=3, b=1)
# >>> d = Counter(a=1, b=2)
# >>> c + d                       # add two counters together:  c[x] + d[x]
# Counter({'a': 4, 'b': 3})
# >>> c - d                       # subtract (keeping only positive counts)
# Counter({'a': 2})
# >>> c & d                       # intersection:  min(c[x], d[x]) # doctest: +SKIP
# Counter({'a': 1, 'b': 1})
# >>> c | d                       # union:  max(c[x], d[x])
# Counter({'a': 3, 'b': 2})


# defaultdict
# >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# >>> d = defaultdict(list)
# >>> for k, v in s:
# ...     d[k].append(v)
# ...
# >>> sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
#
# from collections import defaultdict
# d = defaultdict(lambda: "<missing>")
#
# d["name"] = "<missing>"
#
# d.update(name='John', action='ran')
# print('%(name)s %(action)s to %(object)s' % d)
# 'John ran to <missing>'

# d = dict()
#
# d["name"] = []
# d["name1"] = []
# d["name2"] = []
# d["name3"] = []
#

# LRU

# from collections import OrderedDict
# # OrderedDict
# d = OrderedDict.fromkeys('abcde')
# d.move_to_end('b')
#
# print(d)

# >>> ''.join(d.keys())
# 'acdeb'
# >>> d.move_to_end('b', last=False)
# >>> ''.join(d.keys())
# 'bacde'


# SOLID
# S
# single
# responsibility
#
#
# class Order{
# calculateSum();
# getItems();
# getItemsCount();
# }
#
#
# class OrderRepository{
# load()
# save();
#
# }
#
#
# class OrderViewer{
# printOrder()
# };
#
#
# O
# Open - closed
# principle
#
# L
# Liskov
# substitution
#
# I
# Interface
# segregation
# D
# Dependency
# inversion

# JSON, CSV, XML
# Парсинг
# Картинки


# print("1. Add")
# print("2. Sub")
# print("3. Mul")
# print("4. Div")
# command = int(input("Input command: "))
#
# if command == 1:
#     pass
# elif command == 2:
#     pass
# elif command == 3:
#     pass
# elif command == 4:
#     pass
#
# def add():
#     pass
#
# def sub():
#     pass
#
# commands = {
#     "add": add,
#     "sub": sub,
#
# }


# class MyList:
#     def append(self, i):
#         print(i)
#
#     def __str__(self):
#         return "MyList"
#
# m = MyList()
# # m = []
#
#
# for i in range(10):
#     m.append(i)
#
#
# print(m)


# public interface File(){
#     String read();
#     void write(String data);
# }
#
# public interface FileReader(){
#     String read();
# }
# public interface FileWriter(){
#     void write(String data);
# }


#
# extends class_name
# implements interface_name
#













# JavaScript Object Notation
# JSON


# d = {
#     "gfgf":345,
#     3454: 435,
#     345.345: 345,
#     True: 4354,
#     None: 4355,
#     # (4,5,6):3534
# }
# # Сериализация
#
# import json
# with open("data,json","w") as f:
#     f.write(json.dumps(d))
#
#
# with open("data,json","r") as f:
#     print(json.loads(f.read())["null"] )


# Comma Separated Values


from bs4 import BeautifulSoup


soup = BeautifulSoup("<data><employee>Hello</employee></data>", "xml")

print(soup.find("employee").text)
# eXtensible Markup Language