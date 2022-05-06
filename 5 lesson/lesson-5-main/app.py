from flask import Flask, render_template
import builtins

app = Flask('My Site')
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    return render_template('base.html', title='root')
#app.add_url_rule('/', hello_world)


@app.route('/about')
def about():
    items = [
        'Me',
        'Myself',
        'I'
    ]
    return render_template('about/about.html', title='about', items=items, **builtins.__dict__)


@app.route('/hello/<name>')
def about_user_str(name):
    return render_template('hello.html', some_var=name, pay_respect=False)

@app.route('/hello/<int:name>')
def about_user_2(name):
    return f'<H1>Number2 {name}</H1>'

@app.route('/hello/<int:name>/')
def about_user(name):
    return f'<H1>Number {name}</H1>'

@app.route('/hello/<float:name>')
def about_user_float(name):
    return f'<H1>Float {name}</H1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=21399)
