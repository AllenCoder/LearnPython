def now():
    print ("2015-3-25")
f =now
f();

print(now.__name__)
print(f.__name__)

def log(func):
    def wrapper(*args,**kw):
        print(" call %s():" %func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def nowlog():
    print('2015-3-25')

nowlog()

def logDecorator(text):
    def decorator(func):
        def warpper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return warpper
    return decorator

