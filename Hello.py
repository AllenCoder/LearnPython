print(len('ABBBBDSNNDJNSFJN:'))
print(chr(65))
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[-1])
classmates.append(1522)
print(classmates)
classmates.insert(8, "task")
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(2)
print(classmates)

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][1])
classmates = ('Michael', 'Bob','Michael','Michael','Michael' 'Tracy')
print(classmates.count('Michael'))
t = (1,)
print(t)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

age = 25
if age>26:
    print("大于26岁")
elif age<23:
    print("小于23岁")
else:
    print("实际年龄是：",age)
s = input("请输入年龄 ：")
age = int(s)
print(age)

height = 1.73
weight = 75
bmi = weight/ (height*height)
if bmi < 18.5:
    print("体重过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
elif bmi >32:
    print("过于肥胖")


