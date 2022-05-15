import csv


def generate_movies():
    inception = {
        'name': 'Inception',
        'rating': '9.2',
        'director': 'Nolan'
    }
    pulp_fiction = {
        'name': 'Pulp Fiction',
        'rating': '10',
        'director': 'Tarantino'
    }
    sixth_sense = {
        'name': '6 sense',
        'rating': '9.1',
        'director': 'Ш\'ямалан'
    }
    movies = [
        inception,
        pulp_fiction,
        sixth_sense
    ]
    with open('movies.csv', 'w', newline='') as f:
        writer = csv.writer(f,)
        writer.writerow(['name', 'rating', 'director'])
        for item in movies:
            items_to_write = []
            for key in ['name', 'rating', 'director']:
                items_to_write.append(item[key])
            writer.writerow(items_to_write)


def get_movies():
    with open('movies.csv') as f:
        reader = csv.reader(f)
        header = next(reader)
        movie_list = []
        for line in reader:
            movie = dict(zip(header, line))
            movie_list.append(movie)
        print(movie_list)


def generate_dict_movies():
    inception = {
        'name': 'Inception',
        'rating': '9.2',
        'director': 'Nolan'
    }
    pulp_fiction = {
        'name': 'Pulp Fiction',
        'rating': '10',
        'director': 'Tarantino'
    }
    sixth_sense = {
        'name': '6 sense',
        'rating': '9.1',
        'director': 'Ш\'ямалан'
    }
    movies = [
        inception,
        pulp_fiction,
        sixth_sense
    ]
    with open('movies_dict.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'rating', 'director'])
        writer.writeheader()
        writer.writerows(movies)

def get_dict_movies():
    with open('movies_dict.csv') as f:
        reader = csv.DictReader(f)
        print(list(item for item in reader))

if __name__ == '__main__':
    generate_dict_movies()
    get_dict_movies()