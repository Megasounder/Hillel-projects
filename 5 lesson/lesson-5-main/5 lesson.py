from flask import Flask

app = Flask ('MySite')
@app.route('/')
def hello():
    return '<H1>hello</H1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

