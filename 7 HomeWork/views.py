# from werkzeug.utils import redirect
# from flask import Flask, render_template, request, flash, url_for
#
# from app import InputForm
# from generate_db import Goods
#
#
# @app.route('/')
# def welcome_page():
#     return render_template('welcome.html')
#
#
#
#
# @app.route('/init_form.html', methods=['POST', 'GET'])
# def init_page(db_session=None):
#     form = InputForm(request.form)
#     if request.method == 'POST' and form.validate():
#         item = Goods(form.title.data, form.amount.data, form.price.data, form.category.data, form.buyer.data)
#         db_session.add(item)
#         flash('well done')
#         return redirect(url_for('/all_items.html'))
#     return render_template('init_form.html', form=form)
#
#
# @app.route('/all_items.html')
# def show_all():
#     return render_template('all_items.html')
#
#
# @app.route('/category.html')
# def filter_category():
#     return render_template('category.html')
#
#
# @app.route('/buyer.html')
# def filter_buyer():
#     return render_template('buyer.html')
#
#
#
