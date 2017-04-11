a =list(range(1,11))
print(a)

L = [];
for x in range(1,11):
    L.append(x*x)
print(L)
a = [x*x for x in range(1,11)]
print(a)

a =[x*x for x in range(1,11) if x %2 ==0]
print(a)

b = [m+n for m in 'ABC' for n in 'XYZ']
print(b)

import os # 导入os模块，模块的概念后面讲到
file =[d for d in os.listdir(".")]
print(file)

d ={'x':'A','y':'B','z':'C'}

for k,v in d.items():
    print(k,"=",v)

d ={'x':'A','y':'B','z':'C'}
e =[k + '='+v for k,v in d.items()]
print(e)

L =['Hello',"World",'IBM','Apple']
c = [s.upper() for  s in L]
print(c)

L1 =['Hello',18,"World",'IBM','Apple']
L2 =[s.lower() if isinstance(s,str) else s for s in  L1]
print(L2)