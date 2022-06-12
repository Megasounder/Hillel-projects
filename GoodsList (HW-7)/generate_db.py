import sqlite3
from sqlite3 import Error


def create_database_file(goods):
    """ Create database """
    conn = None
    try:
        conn = sqlite3.connect(goods)
        print('database file was created')
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "goods.db"

    sql_create_list_of_goods_table = """ CREATE TABLE IF NOT EXISTS goods (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        amount FLOAT,
                                        price FLOAT,
                                        category text,
                                        buyer text
                                    );"""

    # create a database connection
    conn = create_database_file('goods.db')

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_list_of_goods_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
