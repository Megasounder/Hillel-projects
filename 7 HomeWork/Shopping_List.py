
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

from flask import Flask, render_template


app = Flask(__name__)


#
# def get_movies() -> List[Dict[str, str]]:
#     with sqlite3.connect('movies.sqlite') as db_connection:
#         db_connection.row_factory = sqlite3.Row
#         cursor = db_connection.cursor()
#         movies_cursor = cursor.execute("""
#             SELECT name, rating, director FROM movies
#         """)
#         movies = []
#         for item in movies_cursor:
#             movies.append(dict(item))
#         return movies
#
@app.route('/')
def welcome_page():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()
