from types import MethodType


#  动态添加属性
class Student(object):
    pass


s = Student()
s.name = 'Michael'  #尝试给实例绑定一个属性：
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(30)  #AttributeError: 'Student' object has no attribute 'set_age'


Student.set_age =set_age
s2.set_age(50)

print(s2.age)


class StudentA(object):
    __slots__=('name','age') #用 定义允许绑定的属性名称
s =StudentA();
s.name ='Michael'
s.age =25
# s.score =99  #AttributeError: 'StudentA' object has no attribute 'score'