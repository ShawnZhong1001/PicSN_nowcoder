# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request, make_response, redirect, flash, \
    get_flashed_messages  # 导入Flask类,类的实例将成为WSGI应用
from jinja2 import Template
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)  # 创建类的实例;通过指定参数指明"按应用方式使用"还是"作为一个模块导入"
app.jinja_env.line_statement_prefix = '#'  # 设置行表达式
app.secret_key = 'nowcoder'


@app.route('/index')
@app.route('/')  # 使用route()装饰器告诉Flask触发函数的URL,把一个函数绑定到一个URL
def index():
    res = ''
    for msg, category in get_flashed_messages(with_categories=True):
        res = res + category + msg + '<br>'
    res += 'hello'
    return res


@app.route('/hello')
def hello_world():  # 生成相关联的URL,返回需要在用户浏览器中显示的信息
    return 'Hello World!'


# 变量规则
@app.route('/user/<username>')
def show_user_profile(username):  # 标记的部分作为关键字参数传递给函数
    return 'User %s' % username


@app.route('/post/<int:post_id>')  # converter作为一个转换器,为变量指定规则
def show_post(post_id):
    return 'Post %d' % post_id


# 唯一的URL/重定向行为
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# URL动态构建
# url_for()用于构建指定函数的URL
# 函数名作为第一个参数,其余对应URL中的变量,未知变量添加到URL中作为查询参数
with app.test_request_context():  # 正在处理一个请求
    print url_for('index')
    print url_for('hello_world', next='/')
    print url_for('show_user_profile', username='Shawn Zhong')


# HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# Jinja2 Template
# 基本方式是通过Template创建一个模板并渲染
template = Template('Hello {{name}}!')
template.render(name='Shawn Zhong')


@app.route('/profile/<int:uid>', methods=['GET', 'POST'])
def profile(uid):
    colors = ('red', 'green', 'yellow')
    infos = {'nowcoder': 'abc', 'google': 'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)


@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res = request.args.get('key', 'defaultkey') + '<br>'  # 对网页传入参数做参数解析,不传参时使用默认值
    res = res + request.url + '||' + request.path + '<br>'
    for property in dir(request):
        res = res + str(property) + '<br>' + str(eval('request.' + property)) + '<br>'
    response = make_response(res)
    response.set_cookie('nowcoderid', key)
    response.status = '404'
    response.headers['nowcoder'] = 'hello~'
    return response


@app.route('/newpath')
def newpath():
    return 'newpath'


@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code=code)


@app.errorhandler(404)  # 对异常情况做特殊处理
def page_not_found(error):
    print error
    return render_template('not_found.html', url=request.url), 404


@app.route('/log_in')
def log_in():
    app.logger.info('log in successfully!')
    flash('登陆成功', 'info')  # flash是页面与页面之间的消息传递,通过session唯一标识
    return 'ok'
    # return redirect('/')


@app.route('/log/<level>/<msg>/')
def log(level, msg):
    dict = {'warn': logging.WARN, 'error': logging.ERROR, 'info': logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level], msg)
    return 'logged:' + msg


def set_logger():
    info_file_handler = RotatingFileHandler('/Users/ShawnZhong/Desktop/info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('/Users/ShawnZhong/Desktop/warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('/Users/ShawnZhong/Desktop/error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__ == '__main__':  # 确保服务器只会在使用python解释器运行代码时运行,而不会作为模块导入时运行
    app.debug = True  # 打开调试模式,服务器在修改应用之后自动重启
    set_logger()
    app.run()  # 运行本地服务器和我们的应用
