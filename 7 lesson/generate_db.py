import json
import sqlite3

with sqlite3.connect('movies.sqlite') as db_connection:
    cursor = db_connection.cursor()
    """
    cursor.execute('''
        DROP TABLE movies;
    ''')
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL,
            rating REAL,
            director VARCHAR(20) NOT NULL
        )
    """)
    cursor.execute("""
        DELETE FROM movies;
    """)
    cursor.execute("""
        INSERT INTO 
            movies(name, rating, director) 
        VALUES 
            ('Inception', 9.1, 'Nolan'),
            ('6 sense', 9.1, 'Ш`ямалан');
    """)

    cursor.execute("""
        INSERT INTO 
            movies(name, rating, director) 
        VALUES (?, ?, ?)
    """, ('Inception', 9.1, 'Nolan'))

    cursor.execute("""
        INSERT INTO 
            movies(name, rating, director) 
        VALUES (:name, :rating, :director)
    """, {
        'name': 'Inception',
        'rating': '9.2',
        'director': 'Nolan'
    })
    cursor.executemany("""
        INSERT INTO 
            movies(name, rating, director) 
        VALUES (:name, :rating, :director)
    """, [{
        'name': 'Inception',
        'rating': '9.2',
        'director': 'Nolan'
    }, {
        'name': 'Star Wars',
        'rating': '10',
        'director': 'Lucas'
    }])
    with open('movies.json') as f:
        movies = json.load(f)
        cursor.executemany("""
            INSERT INTO 
                movies(name, rating, director) 
            VALUES (:name, :rating, :director)
        """, movies)

    cursor.close()
    db_connection.commit()

with sqlite3.connect('movies.sqlite') as db_connection:
    db_connection.row_factory = sqlite3.Row
    cursor = db_connection.cursor()
    movies = cursor.execute("""
        SELECT name, rating, director FROM movies 
    """)
    for item in movies:
        print(dict(item))