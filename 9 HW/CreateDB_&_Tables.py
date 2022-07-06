import sqlite3

#
# def create_database_file(warner):
#     """ Create database """
#     conn = None
#     try:
#         conn = sqlite3.connect(warner)
#         print('database file was created')
#     except Error as e:
#         print(e)
#     return conn
#
#
# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)
#
#
# def main():
#     database = "Warner.db"
#
#     sql_create_table_profession = """ CREATE TABLE IF NOT EXISTS profession (
#                                         id integer PRIMARY KEY,
#                                         title text NOT NULL,
#                                         amount FLOAT,
#                                         price FLOAT,
#                                         category text,
#                                         buyer text
#                                     );"""
#
#     # create a database connection
#     conn = create_database_file('goods.db')
#
#     # create tables
#     if conn is not None:
#         # create projects table
#         create_table(conn, sql_create_table_profession)
#         conn.close()
#     else:
#         print("Error! cannot create the database connection.")
#


with sqlite3.connect('warner.sqlite') as db_connection:
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS professions(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            profession VARCHAR(20) NOT NULL)
    """)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS genders(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            gender VARCHAR(10) NOT NULL)
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS peoples(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(20) NOT NULL,
            surname VARCHAR(20) NOT NULL,
            age INTEGER NOT NULL,
            email VARCHAR(50),
            profession VARCHAR(20) NOT NULL,
            gender VARCHAR(50) NOT NULL,
            salary INTEGER (50),
            FOREIGN KEY (profession) REFERENCES professions (profession)
            FOREIGN KEY (gender) REFERENCES genders (gender))
            """)
    cursor.close()
    db_connection.commit()


    # cursor.execute("""
    #     INSERT INTO
    #         movies(name, rating, director)
    #     VALUES
    #         ('Inception', 9.1, 'Nolan'),
    #         ('6 sense', 9.1, 'Ш`ямалан');
    # """)

    # cursor.execute("""
    #     INSERT INTO
    #         movies(name, rating, director)
    #     VALUES (?, ?, ?)
    # """, ('Inception', 9.1, 'Nolan'))
    #
    # cursor.execute("""
    #     INSERT INTO
    #         movies(name, rating, director)
    #     VALUES (:name, :rating, :director)
    # """, {
    #     'name': 'Inception',
    #     'rating': '9.2',
    #     'director': 'Nolan'
    # })
    # cursor.executemany("""
    #     INSERT INTO
    #         movies(name, rating, director)
    #     VALUES (:name, :rating, :director)
    # """, [{
    #     'name': 'Inception',
    #     'rating': '9.2',
    #     'director': 'Nolan'
    # }, {
    #     'name': 'Star Wars',
    #     'rating': '10',
    #     'director': 'Lucas'
    # }])
    # with open('movies.json') as f:
    #     movies = json.load(f)
    #     cursor.executemany("""
    #         INSERT INTO
    #             movies(name, rating, director)
    #         VALUES (:name, :rating, :director)
    #     """, movies)
    #
    # cursor.close()
    # db_connection.commit()

# with sqlite3.connect('movies.sqlite') as db_connection:
#     db_connection.row_factory = sqlite3.Row
#     cursor = db_connection.cursor()
#     movies = cursor.execute("""
#         SELECT name, rating, director FROM movies
#     """)
#     for item in movies:
#         print(dict(item))