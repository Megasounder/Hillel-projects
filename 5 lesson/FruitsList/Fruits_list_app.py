from flask import Flask, render_template

app = Flask('Fruits')
app.url_map.strict_slashes = False


@app.route('/')
def welcome():
    title = 'FRUITS'
    items = ['Type /list, /filter/smtn, /show/num']
    return render_template('template.html', items=items, title=title)


@app.route('/list')
def list_of_fruits():
    title = 'LIST OF FRUITS'
    items = [i for i in open('fruits.txt')]
    return render_template('template.html', items=items, title=title)


@app.route('/show/<int:num>')
def print_rows(num: int):
    title = f'First  {num} elements'
    items = []
    with open('fruits.txt', 'r') as f:
        for line in f:
            items.append(line)
    return render_template('template.html', items=items[:num], title=title)


@app.route('/filter/<word>')
def find_fruit(word: str):
    title = f'Search result for: {word}'
    items = []
    with open('fruits.txt', 'r') as f:
        for line in f:
            if word in line:
                items.append(line)
    return render_template('template.html', items=items, title=title)


app.run()
