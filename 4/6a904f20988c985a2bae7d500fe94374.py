# import time
#
# begin = time.time()
#
# for i in range(1000000):
#     pass
#
# end = time.time()
#
# print(end - begin)
#
# #0.33610057830810547
# #0.44580817222595215
# #0.26993680000305176
# #0.26180148124694824
# #0.2582550048828125


#
# import timeit
#
# def f():
#     for i in range(1000):
#         pass
#
#
# statement = "f()"
# setup = "from __main__ import f"
#
#
# print(timeit.timeit(statement, setup=setup, number=100))


# import timeit
#
#
# def fact(n):
#     if n <= 1:
#         return 1
#
#     return fact(n - 1) * fact(n - 2) * n
#
#
# cache = dict()
#
#
# def cached_fact(n):
#     global cache
#
#     if n <= 1:
#         return 1
#
#     if n in cache:
#         return cache[n]
#     else:
#         res = cached_fact(n - 1) * cached_fact(n - 2) * n
#         cache[n] = res
#         return res
#
#
# statement = "fact(20)"
# setup = "from __main__ import fact"
#
# print(timeit.timeit(statement, setup=setup, number=100))
#
# statement = "cached_fact(20)"
# setup = "from __main__ import cached_fact"
#
# print(timeit.timeit(statement, setup=setup, number=100))


# import hashlib
# import cProfile
#
# cProfile.run("[i for i in range(199*99)]")




import sys



# print(sys.getsizeof([]))
# print(sys.getsizeof([1,2,3]))
# print(sys.getsizeof([[1,2,3,4],[1,2,3,4],[1,2,3,4]]))

# class A:
#     def __init__(self):
#         self.s = 213
#         self.t = 32
#         self.r = 32
#         self.i = 32
#         self.q = 32
#         self.z = 32
#         self.x = 32
#
# class B:
#     __slots__ = ['s', 't']
#
#     def __init__(self):
#         self.s = 213
#         self.t = 32
#
#
#
# a = A()
# b = B()
#
# a.pppp = 23432423
#
# print(a.pppp)

# b.werwer = 324234423

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))







#
# for i in range():
#     for j in range():
#         for k in range():
#             pass






# def f():
#     pass
#
#
# def g(func):
#     pass
#
#



# def decor(func):
#     def f():
#         print("begin")
#         func()
#         print("end")
#
#     return f
#
#
# def my_func():
#     print("My func")
# def my_func2():
#     print("My func2")
#
#
#
# # my_func()
#
#
#
# rr = decor(my_func)
# rr2 = decor(my_func2)
#
# rr()
# rr2()









#
#
# def meat():
#     print("Meat")
#
#
#
# def bread(func):
#     def f():
#         print("Bread")
#         func()
#         print("/Bread")
#
#     return f
#
#
# def salad(func):
#     def f():
#         print("Salad")
#         func()
#         print("/Salad")
#
#     return f
#
# def onion(func):
#     def f():
#         print("Onion")
#         func()
#         print("/Onion")
#
#     return f
#
#
#
#
#
# res = bread(onion(salad(meat)))
# res2 = onion(salad(bread(meat)))
#
# res()
# print()
# res2()









#
# def decor(func):
#     def f(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(res)
#         return res
#
#     return f
#
# @decor
# def sum(a,b):
#     return a + b
#
# @decor
# def multiply(a,b,c):
#     return a * b * c
#
#
# # sum = decor(sum)
#
# sum(1,2)
# multiply(1,b=2,c=3)





















# def ingredient(name):
#     def decor(func):
#         def f():
#             print(name)
#             func()
#             print(f"/{name}")
#
#         return f
#     return decor
#
# @ingredient("Bread")
# @ingredient("Salad")
# @ingredient("Onion")
# @ingredient("Pepper")
# def meat():
#     print("Meat")
#
# meat()


# meat_and_salad = ingredient("Salad")(meat)
# bread = ingredient("Bread")(meat_and_salad)
#
# bread()



# res = bread(onion(salad(meat)))
# res2 = onion(salad(bread(meat)))
#
# res()
# print()
# res2()



# import timeit
#
#
#
#
#
# def cache(func, memory=dict()):
#     def f(n):
#
#         if n in memory:
#             return memory[n]
#         else:
#             res = func(n)
#             memory[n] = res
#             return res
#
#     return f
#
#
#
#
# def fact(n):
#     if n <= 1:
#         return 1
#
#     return fact(n - 1) * fact(n - 2) * n
#
#
# cached_fact = cache(fact)
#
# statement = "fact(20)"
# setup = "from __main__ import fact"
#
#
# print(timeit.timeit(statement, setup=setup, number=100))
#
# statement = "cached_fact(20)"
# setup = "from __main__ import cached_fact"
#
#
# print(timeit.timeit(statement, setup=setup, number=100))






# import random
#
# def f(a=dict()):
#     a[random.randint(1,100)] = 21
#     print(a)
#
#
#
# f()
# f()
# f()
# f()
# f()
# f()
# f()
# f()
# f()




















#
# try:
#     pass
# except:
#     pass





# exceptions

# a = 1
# b = 0
# try:
#     print(a / b)
# except Exception:
#     print("Zero div error")
#
#
# print("Hello, world!")
#
# def f():
#     print(1 / 0)
#     print('f')
#
#
# def g():
#     try:
#         f()
#     except ZeroDivisionError:
#         print("Zeroerror")
#     print('g')
#
#
#
# def r():
#     g()
#     print('r')




# r()



def f():
    raise Exception("My exception")
    print('f')


def g():
    f()
    print('g')



def r():
    try:
        g()
    except ZeroDivisionError:
        print("Zeroerror")
    finally:
        print("Finally")
    print('r')


r()


