#coding=utf-8

from flask import Flask,render_template,request,make_response,redirect,flash,get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler
app=Flask(__name__)
app.jinja_env.line_statement_prefix='#'
app.secret_key='nowcoder'

@app.route('/index/')
@app.route('/')
def index():
    res=''
    for msg,category in get_flashed_messages(with_categories=True):
        res=res+msg+category+'<br>'
    return res

@app.route('/profile/<int:uid>/', methods=['GET','POST'])#带参数类型转化的url   /参数补齐
def profile(uid):
    # return 'profile:'+str(uid)
    colors=('red','green')
    infos={'nowcoder':'abc','google':'def'}

    return render_template('profile.html',uid=uid,colors=colors)
@app.route('/request')
def request_demo():
    key=request.args.get('key','defaultkey')+'<br>'
    res=request.args.get('key','defaultkey')+'<br>'
    res=res+request.url+'<br>'+request.path+'<br>'
    for property in dir(request):
        res=res+str(property)+'|==|'+str(eval('request.'+property))+'<br>'
    response=make_response(res)
    response.set_cookie('nowcoderid',key)
    response.status='404'
    response.headers['nowcoder']='hello'
    return response
@app.route('/newpath')
def newpath():
    return 'newpath'
@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath',code=code)

@app.errorhandler(404)
def page_not_fount(error):
    print error
    return render_template('not_found.html',url=request.url),404
@app.errorhandler(400)
def exception_page(error):
    return 'exception'

@app.route('/admin')
def admin():
    key=request.args.get('key')
    if key=='admin':
        return 'hello admin'
    else:
        return 'hello user'

@app.route('/login')
def login():
    app.logger.info('log success')
    flash('登陆成功','info')
    return redirect('/index')

@app.route('/log/<level>/<msg>')
def log(level,msg):
    dict={'warn':logging.WARN,'error':logging.ERROR,'info':logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level],msg)
    return 'logged:'+msg

def set_logger():
    info_file_handler=RotatingFileHandler('log/info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler=RotatingFileHandler('log/warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler=RotatingFileHandler('log/error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)
if __name__ == '__main__':
    set_logger()
    app.run(debug=True)