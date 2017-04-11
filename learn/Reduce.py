from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
    return x*10+y

print(reduce(fn,[1,3,5,7,9]))

# def normalize(name):
#     return name[0].upper()+name[1:].lower
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
L1 = ['adam', 'LISA', 'barT']

# def normalize(name):
#      return (i[0].upper() + i[1:].lower() for i in name)  #列表生成
# L2 = list(normalize(L1)