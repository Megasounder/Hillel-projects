import json
from pprint import pprint
from typing import NoReturn


class Movie:
    def __init__(self, name, rating, director):
        self.name = name
        self.rating = rating
        self.director = director

    def __repr__(self):
        return f'Movie("{self.name}", "{self.rating}", "{self.director}")'

    def __str__(self):
        return f'Movie: {self.name} with IMDB: {self.rating} directed by {self.director}'

def generate_movies():
    inception = {
        'name': 'Inception',
        'rating': '9.2',
        'director': 'Nolan'
    }
    inception_obj = Movie(**inception)
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
    with open('movies.json', 'w') as f:
        json.dump(movies, f, indent=2)


def get_movies() -> NoReturn:
    with open('movies.json') as f:
        for movie in json.load(f):
            print(f'{Movie(**movie)!r}')
        obj = Movie("Inception", "9.2", "Nolan")


if __name__ == '__main__':
    generate_movies()
    get_movies()