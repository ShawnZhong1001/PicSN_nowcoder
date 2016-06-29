# -*- coding: utf-8 -*-

def log(level, *args, **kwargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            '''
            * 用来传递任意个无名字参数,这些参数通过Tuple的形式访问
            ** 用来传递任意个有名字参数,这些参数用dict来访问
            '''
            print level, 'Before calling', func.__name__
            print level, 'args: ', args, 'kvargs:', kvargs
            func(*args, **kvargs)
            print level, 'After calling', func.__name__

        return wrapper # 通过return来执行函数
    return inner

@log(level='INFO')
def hello(name, msg):
    print 'hello', name, msg

if __name__ == '__main__':
    hello(name='nowcoder', msg='i miss you') # 若不指明名字,则通过args传参