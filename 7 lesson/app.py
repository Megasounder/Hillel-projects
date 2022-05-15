import sqlite3
from typing import List, Dict

from flask import Flask, render_template

app = Flask(__name__)


def get_movies() -> List[Dict[str, str]]:
    with sqlite3.connect('movies.sqlite') as db_connection:
        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()
        movies_cursor = cursor.execute("""
            SELECT name, rating, director FROM movies 
        """)
        movies = []
        for item in movies_cursor:
            movies.append(dict(item))
        return movies



@app.route('/')
def movies():
    movie_list = get_movies()

    return render_template('movies.html', movies=movie_list, enumerate=enumerate)


if __name__ == '__main__':
    app.run()
