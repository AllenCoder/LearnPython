std1 ={'name':'Michael','score':98}
std2 ={'name':'Bob','score':81}

def print_score(std):
    print('%s: %s' % (std['name'],std['score']))
class Student(object):
    def __init__(self,name,score):
        self.__name =name
        self.__score =score
    def print_score(self):
        print('%s :%s' % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <=score <=199:
            self.__score =score
        else:
            raise ValueError('bad score')
bart =Student('Bart Simpson',59)
lisa =Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()