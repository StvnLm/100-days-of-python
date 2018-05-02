from collections import namedtuple
from collections import defaultdict
import csv
import urllib.request

movie_data = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
movie_csv = 'movies.csv'
urllib.request.urlretrieve(movie_data, movie_csv)
movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movie_csv):
    """Extracts all movies from the CSV and stores them in a dictionary
    where the keys are directors and the values is a list of movies in named tuples"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movieName = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = movie(title=movieName, year=year, score=score)
            directors[director].append(m)
    return directors

directors = get_movies_by_director()
print(directors['Christopher Nolan'])
