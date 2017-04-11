print(int('12345'))

a=int ('12345',base=18)
print(a)
def int2 (x,base=2):
    return int(x,base)
b = int2('1000000')
print(b)

c = int2('100001001')
print(c)


#偏函数
import functools
int2 =functools.partial(int,base=2)
d = int2('10000000')
print('偏函数',d)

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %S!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()