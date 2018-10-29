'''
import pickle
l = [1,2,3]
a=pickle.dumps(l)
print(a)


d = {"id":1, "name": "贾敏强", "phone_number":"15801396646"}
b = pickle.dumps(d)
print(b)
c = pickle.loads(b)
print(c)

import pickle
class Record:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


with open("d:/Record.dat", "wb") as f:
    pickle.dump(Record, f)
with open("d:/Record.dat", "rb") as f:
    print(pickle.load(f))

record = Record("贾敏强", "15801396646")
with open("d:/record.dat", "wb") as f:
    pickle.dump(record, f)
with open("d:/record.dat", "rb") as f:
    print(pickle.load(f))



#递归函数
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))

i=0
def test():
    return test()

if __name__ == "__main__":
    try:
        test()
        i += 1
    except RecursionError as e:
        print('except:', e)
        print (i)

LL=[1,2,3,[4,[5,6],7],8,9]

def alist(list_1):
    for i in list_1:
        if type(i)==list:
            alist(i)

        else:
            print(i)

alist(LL)



#闭包函数
def npower():
    n = 3
    def  power(x):
        return x ** n
    return power

if __name__ == "__main__":
    f = npower()
    print(f(2))
    print(f.__closure__)
    print(f.__closure__[0].cell_contents)


import time

def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper

@decorator
def func():
    print("hello world")
    time.sleep(1)

func()


def out_f(arg):
    print("out_f" + arg)
    def decorator(func):
        def inner():
            func()
        return inner
    return decorator

@out_f("123")
def func():
    print("hello word")


it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break



class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self
fibs = Fibs()

for f in fibs:
    if f > 1000:
        print(f)
        break


L = [[1, 2],[3, 4],[5,]]
def flat(L):
    for sublist in L:
        for e in sublist:
            yield e

for num in flat(L):
    print(num)



while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

g = flat(L)
next(g)
next(g)
print(g.send(5))

def gen():
    sum = 0
    for i in range(10):
        x = (yield sum)
        sum += x
g = gen()
next(g)
print(g.send(7))
print(g.send(8))
'''
import os

g = os.walk("D:/Work/python-dev/python-dev")
print(next(g))
print(next(g))
print(next(g))
print(next(g))




