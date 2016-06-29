# -*- coding: utf-8 -*-
from flask_script import Manager
from ex2 import app
manager = Manager(app)


# 为了交互,传入更多的参数
@manager.option('-n', '--name', dest='name', default='nowcoder')
def hello(name):
    print 'hello', name


@manager.command
def initialize_database():
    'initialize database'
    print 'database ...'


if __name__ == '__main__':
    manager.run()
