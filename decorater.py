#coding=utf8

def log(level,*args,**kwargs):
    def inner(func):
        '''
            *无名字参数
            **有名字参数
            :param func:
            :return:
            '''

        def wrapper(*args, **kvargs):
            print level,'before calling ', func.__name__
            print level,'arge', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print level,'end calling ', func.__name__

        return wrapper
    return inner
@log(level='INFO')
def hello():
    print 'hello'
@log(level='XXX')
def hello2(name):
    print 'hello',name


if __name__ == '__main__':
    hello()
    hello2(name='zjl')