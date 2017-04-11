# 在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n%2 !=1
print(list(filter(is_odd,[1,2,3,5,7,0,194,6,8,10]))) 

# 把一个序列中的空字符串删掉，可以这么写：

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A',"",'B',None,'C'," "])))

def _odd_iter():
    n =1
    while True:
        n = n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n >0
def primes():
    yield 2
    it =_odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n <1000:
        print(n)
    else:
        break