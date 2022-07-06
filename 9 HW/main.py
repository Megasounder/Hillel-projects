import sqlite3
from random import randint

def create_db_and_tables() -> None:
    with sqlite3.connect('warner.sqlite') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS professions(
                id INTEGER PRIMARY KEY NOT NULL,
                profession VARCHAR(20) NOT NULL)
        """)

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS genders(
                id INTEGER PRIMARY KEY NOT NULL,
                gender VARCHAR(18) NOT NULL)
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
    return print('___db and tables was created___')


def insert_values_into_parent_tables() -> None:
    with sqlite3.connect('warner.sqlite') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute(f"""
            INSERT INTO  genders(id, gender)
            VALUES (1, 'male'), (2, 'female'), (3, 'transgender')
        """)
        cursor.execute("""
            INSERT INTO professions(profession)
            VALUES  ('actor'), ('producer'), ('operator'), ('engineer'), ('stage_manager'), ('designer'), ('painter'), ('director')
        """)
        cursor.close()
        db_connection.commit()
    return print('values was inserted')
    
    
def fill_table_peoples() -> None:
    with sqlite3.connect('warner.sqlite') as db_connection:
        cursor = db_connection.cursor()
        cursor.execute(f"""
        INSERT INTO peoples(name, surname, gender, age, email, profession, salary)
        VALUES 
        ('Ben', 'Affleck', 'male', {randint(20, 68)}, 'affleck@email.com', 'actor', {randint(2500, 500000)}), 
        ('Sarah', 'Connor', 'female', {randint(20, 68)}, 'sarahconora@email.com', 'actor', {randint(2500, 500000)})
     
       
     
     
     """)
    cursor.close()
    db_connection.commit()
    return print('input successfull')


create_db_and_tables()   # створить базу даних (довільне ім'я)
insert_values_into_parent_tables()  # Створить таблицю з професіями (записати рандомні значення)
    # Створить таблицю зі гендерами (має бути як мінімум два гендери, інши на ваш вибір)
    # Створить таблицю people з атрибутами id (обов'язково), ім'я(обов'язково), прізвище(обов'язково), стать(обов'язково) foreign key на таблицю з гендерами, зарплата, посада як foreign key на таблицю з професіями, email, вік(обов'язково)

fill_table_peoples()    # Згенерує 20 записів на ваш смак причому для тих полів які не обов'язкові вказувати вказувати дані вибирково наприклад з 20 тільки 5 мають email, 10 посада - тощо а зарплата і вік генерується за допомогою функції рандом
    # Додати два записи для Laurence Wachowski та Andrew Wachowski стать чоловік інші дані довільні
    # Змінити стать для Laurence Wachowski та Andrew Wachowski на жінка
    # Змінити ім'я для Laurence Wachowski на Lana
    # Змінити ім'я для Andrew Wachowski на Lilly
    # Додати новий гендер
    # Змінити довільний людині гендер на новий
    # Вивести всіх людей з новим гендером
    # додати для всіх записів в яких немає email - email який складатиместья з імені і прізвища та довільний хост, тобто для людини Sarah Connor email має бути sarah.connor@sky.net причому що email має генеруватися засобами sql приклад:
    # INSERT INTO artist
    # SELECT "SQLite" || "CONCAT"
    # FROM artists;
