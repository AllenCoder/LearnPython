# 获取对象信息

a = type(123)
print(a)
b = type('str')
print(b)
c = type(None)
print(c)

d = type(123) == type(456)
e = type(123) == int
f = type('abc') == type('123')
g = type('abc') == str
h = type('abc') == type(123)

print(' d ==', d, ' e ==', e, ' f==', f, ' g ==', g, ' h==', h)

import types


def fn():
    pass


a = type(fn) == types.FunctionType
print(a)
b = type(abs) == types.BuiltinFunctionType
print(b)

c = type(lambda x: x) == types.LambdaType
print(c)

d = type((x for x in range(10))) == types.GeneratorType
print(d)

c = dir(abs)
print(c)
d = 'ABC'.lower()
print(d)


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

c = hasattr(obj, 'x')  # 有属性 ’X' 吗

print(c)

d = hasattr(obj, 'y')

print(d)
e = setattr(obj, 'y', 19)

print(e)

f = hasattr(obj, 'y')
print(f)

g = getattr(obj, 'y')

print(g)
print(obj.y)

h = getattr(obj, 'z', 404)

print(h)

fn = getattr(obj, 'power')
k = fn()
print(k)
