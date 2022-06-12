import sqlite3
from typing import List

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from form_model import MyInputForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VerySecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goods.db'


db = SQLAlchemy(app)


class ListItem(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    amount = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float, nullable=True)
    category = db.Column(db.String(40))
    buyer = db.Column(db.String(20), nullable=True)

    def __init__(self, title, amount, price, category, buyer):
        self.title = title
        self.amount = amount
        self.price = price
        self.category = category
        self.buyer = buyer


def get_goods() -> List:
    with sqlite3.connect('goods.db') as db_connection:
        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()
        goods_cursor = cursor.execute("""
            SELECT title, amount, price, category, buyer FROM goods
        """)
        goods = []
        for item in goods_cursor:
            goods.append(dict(item))
        return goods


def get_by_category() -> List:
    with sqlite3.connect('goods.db') as db_connection:
        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()
        goods_cursor = cursor.execute("""
               SELECT distinct category FROM goods
           """)
        goods = []
        for item in goods_cursor:
            goods.append(dict(item))
        return goods


def get_by_customer() -> List:
    with sqlite3.connect('goods.db') as db_connection:
        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()
        goods_cursor = cursor.execute("""
               SELECT distinct buyer FROM goods
           """)
        goods = []
        for item in goods_cursor:
            goods.append(dict(item))
        return goods


@app.route('/')
def welcome_page():
    return render_template('welcome.html')


@app.route('/input_form.html', methods=['GET', 'POST'])
def init_page():
    form = MyInputForm()
    if request.method == 'POST':
        title = request.form['title']
        amount = request.form['amount']
        price = request.form['price']
        category = request.form['category']
        buyer = request.form['buyer']
        record = ListItem(title, amount, price, category, buyer)
        db.session.add(record)
        db.session.commit()
        return redirect("/all_items.html")
    return render_template("input_form.html", form=form)


@app.route('/all_items.html')
def show_all():
    items = get_goods()
    return render_template('all_items.html', items=items)


@app.route('/category.html')
def filter_category():
    items = get_by_category()
    return render_template('category.html', items=items)


@app.route('/buyer.html')
def filter_buyer():
    items = get_by_customer()
    return render_template('buyer.html', items=items)


@app.route('/<filtered>')
def fil(filtered):
    items = get_goods()
    target = filtered
    return render_template('filtered.html', items=items, target=target)


if __name__ == '__main__':
    app.run()

