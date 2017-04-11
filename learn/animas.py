# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is Running....')

class Dog(Animal):
    
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat.....')
    
class Cat(Animal):
    def run(self,value =100):
        print('Cat is running...',value)

dog = Dog()
dog.run()

cat =Cat()
cat.run()
cat.run(10000)

a = list() # a 是list 类型
b = Animal() # b 是Ａｎｉｍａｌ类型
c = Dog() # c 是Dog类型

print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly .....')
run_twice(Tortoise())