
# Cписок копупок
#
#
# покупка содержит:  Название, категория, кол-во, цена, логин автора.
# 1) Показати всі покупки
# 2) Показати всі покупки конкретної категорії (категорія передається через URL)
# 3) Показати всі покупки конкретного користувачаї (користувач передається через URL)
#
# Всі дані мають лежати в базі даних
# Для ініціалізації бази даних використовуйте окремий скріпт
# Для пошуку в базі даних використовуйте sql конструкції where та like
#
#
#
#
import sqlite3
from typing import List
from flask import Flask, render_template, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, IntegerField, FloatField
from werkzeug.utils import redirect



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goods.db'

db = SQLAlchemy(app)


class InputForm(Form):
    title = StringField('Title')
    amount = IntegerField('Amount')
    price = FloatField('Price')
    category = StringField('Category')
    buyer = StringField('Buyer')

class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    amount = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float, nullable=True)
    category = db.Column(db.String(40))
    buyer = db.Column(db.String(20), nullable=True)

db.create_all()

# def get_goods() -> List:
#     with sqlite3.connect('goods.sqlite') as db_connection:
#         db_connection.row_factory = sqlite3.Row
#         cursor = db_connection.cursor()
#         goods_cursor = cursor.execute("""
#             SELECT title, amount, price, category, buyer FROM goods
#         """)
#         goods = []
#         for item in goods_cursor:
#             goods.append(dict(item))
#         return goods
#

@app.route('/')
def welcome_page():
    return render_template('welcome.html')




@app.route('/init_form.html', methods=['POST', 'GET'])
def init_page():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        item = Goods(form.title.data, form.amount.data, form.price.data, form.category.data, form.buyer.data)
        db_session.add(item)
        flash('well done')
        return redirect(url_for('/all_items.html'))
    return render_template('init_form.html', form=form)


@app.route('/all_items.html')
def show_all():
    return render_template('all_items.html')


@app.route('/category.html')
def filter_category():
    return render_template('category.html')


@app.route('/buyer.html')
def filter_buyer():
    return render_template('buyer.html')




if __name__ == '__main__':
    app.run()
