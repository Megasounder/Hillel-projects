# from flask import Flask, render_template
#
#
# app = Flask('FirstSite')
#
# @app.route('/')
# def hello_world():
#     return '<H1> Hello WOOOORLDDDD </H1>'
#
#
# @app.route('/about')
# def about():
#     return '<H1> This is additional page with information about me </H1>'
# @app.route('/page123.html')
# def page123():
#     return render_template('page123.html')
# if __name__=='__main__':
#     app.run(debug=True)
#  Написати стайт який буде показувати контент файлу
# (файл будь який самі придумайте, головне шоб в ньому було багато лійній)
# і матиме три роути:
#
# /list   -   показує з використанням <ul><li></ul> тегів полінійно вміст файлу
# /filter/<word>  -    показує вміст файлу але тільки лінії які містять в собі слово яке ви ввели в посиланні
# /show/<number>  -  показує вміст файлу але тільки перші <number> ліній
#
#
# Кожна сторінка має мати заголовок на сторінці.
#
# А для сторіки /filter/<word> фразу "Результати пошуку для {{ word }}:"
#
# А для сторіки /show/<number> фразу "Перші {{ number }} ліній файлу:"
#
#
#
# Використовуйте розширення темплейтів.
#
# Файл відкривайте і зчитуйте контент файлу в функції яка обробляє роут

from flask import Flask

app = Flask('MySite')


@app.route('/')
def hello_world():
    return '<H1> Hello' \
           'WORLD</H1>'


@app.route('/about')
def about():
    return '<H1> Yeeeeesss</H1>'


@app.route('/about/')
def about_folder():
    return '<H1> FOOOLDER</H1>'


@app.route('/hi/<int:name>')
def user_name(name):
    return f'<H1>Hello {name} </H1>'


@app.route('/hi/<int:name>/')
def user_name2(name):
    return f'<H1>Hello {name} </H1>'


print(f'1{__name__}')

if __name__ == '__main__':
    app.run()
