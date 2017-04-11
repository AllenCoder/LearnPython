d = {'a': 1, 'b': 2, 'c': 3} 
for key in d:
   print(key)
for ch in 'ABC':
     print(ch)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

def fib(max):
    n,a,b =0,0,1
    while n<max:
        yield b
        a,b = b ,a+b
        n = n+1
    return 'done'
print(fib(6))
g = fib(6)
while True:
    try:
        x =next(g)
        print('g',x)
    except StopIteration as e:
        print('GeneratorExit',e.value)
        break
def triangles():
    L =[1]
    while True:
        yield L
        L.append(0)
        L =[L[i-1]+L[i] for i in range(len(L))]


