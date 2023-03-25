import csv
from typing import List
from typing import Dict
import random
import os

print("Movies collection")

movies_collection = []
path = os.path.join(os.getcwd(), 'Desktop','Kodilla','film','film.csv')

class Film:
    def __init__(self, name: str, year: int, genre: str, views: int) -> None:
        self.name = name
        self.year = year
        self.genre = genre
        self.views = views

    def __str__(self) -> str:
        return f'{self.name} ({self.year} {self.views})'

    def play(self) -> int:
        self.views += 1
        return self.views

class Serial(Film):
    def __init__(self, name: str, year: int, genre: str, views: int, season: int, episode: int) -> None:
        super().__init__(name, year, genre, views)
        self.season = season
        self.episode = episode
    
    def __str__(self) -> str:
        return f'{self.name}  S{self.season}E{self.episode}'
    
    def number_of_episodes(self) -> int:
        serial_name = input('Please enter name of serial: ')
        for movie in movies_collection:
            if serial_name == movie.name:
                print(movie.episode)


def add_serial():             
    with open(path, 'a', newline='') as csvfile:
        fieldnames = ['name', 'year', 'genre', 'views', 'season', 'episode']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        name = input('Enter name of serials:')
        year = int(input('Enter year: '))
        genre = input('Enter genre of serial:')
        views = int(input('Enter view: '))
        season = int(input('Enter season: '))
        episode = int(input('Enter episode: '))
        serial = Serial(name, year, genre, views, season, episode)
        writer.writerow({
            'name': serial.name,
            'year': serial.year,
            'genre': serial.genre,
            'views': serial.views,
            'season': serial.season,
            'episode': serial.episode})
        movies_collection.append(serial)
        print('Serial added successfully')

def get_film() -> List[Film]:
    print('List of films')
    list_film = []
    for movie in movies_collection:
        if isinstance(movie, Film):
            list_film.append(movie)
    return list_film
                                            
                                     
def get_serial() -> List[Serial]:
    print('List of serials')
    list_serial = []
    for serial in movies_collection:
        if isinstance(serial, Serial):
            list_serial.append(serial)
    return list_serial

def search() -> str:
    search_name = input('Please enter name of film to search: ')
    for movie in movies_collection:
        if search_name == movie.name:
            print(movie)

def generate_views() -> int:
    for movie in movies_collection:
        views = random.randint(1, 100)
        yield (movie, views)

def ten_generate_views(generate_views) -> int:
    for i in range(10):
        generate_views()

if __name__ == '__main__':
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            movies_collection.append(Film(name=row['name'], year=int(row['year']), genre=row['genre'], views=int(row['views'])))
    for movie in movies_collection:
        print(movie)
