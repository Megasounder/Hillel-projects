from flask import Flask, render_template


app = Flask('FirstSite')

@app.route('/')
def hello_world():
    return '<H1> Hello WOOOORLDDDD </H1>'


@app.route('/about')
def about():
    return '<H1> This is additional page with information about me </H1>'
@app.route('/page123.html')    
def page123():
    return render_template('page123.html')    
if __name__=='__main__':
    app.run(debug=True)     