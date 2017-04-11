class Dog(object):
 def run(self):
    print('running Dog!')


class Person(object):
    def run(self):
     print('running man!')


class Monster(Person,Dog ):
    pass

xueFengSaiSai = Monster()
xueFengSaiSai.run()