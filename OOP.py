class Animal(object):
    pass
# 大象
class Mammal(Animal):
    pass
# 小鸟

class Bird(Animal):
    pass
# 各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying')  
class Dog(Mammal,Runnable):
    pass


class Bat(Mammal,Flyable):
    pass

# MixIn
class Dog(Mammal,RunnableMixIn,CarnivorousMix):
    pass

# 多线程 TCP服务
class MyTCPServer(TCPServer,ForkingMixIn):
    pass

# 多线程 UDP服务
class MyUDPSerVer(UDPServer,ThreadingMixIn):
    pass

class MyTCPServer(TCPServer,CoroutineMixIn):
    pass