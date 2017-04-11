print(abs(-100))
print(max(1,2,4,5,1589))
print(int(12.99))
print(str(123))
print(bool(1))
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

n1 = 255
print(hex(255))
n2 =100000
print(hex(n2))

#定义函数

def my_abs(x):
    if x >=0:
        return x
    else:
        return -x

print(my_abs(-100))
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

#练习

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

# ax2 + bx + c = 0

# 的两个解。

# 提示：计算平方根可以调用math.sqrt()函数：


import math


import math
def quadratic(a,b,c):
    s=b*b-4*a*c
    if s<0:
        print('')
    else:
        s1=math.sqrt(s)
        x1=(-b+s1)/(2*a)
        x2=(-b-s1)/(2*a)
    return x1,x2
print(quadratic(1,5,6))

def power(x): return x*x;
print(power(2500000))
def my_abs(x):
    if not isinstance(x ,(int,float)):
        raise TypeError("错误的参数类型")
    if x >=0:
        return x
    else:
        return -x
print(my_abs(1000))
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum
print(calc([1,2,3]))


def calc1(*numbers):
    sum =0
    for n in numbers:
        sum = sum+n*n
    return sum
print(calc1(1,2,3,4))



def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(100))
L = [] 
n = 1
while n <=99:
    L.append(n)
    n = n+2
print(L)