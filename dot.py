import csv

import os
path = "/home/bozyanv/Desktop/movieproject_final"

from movie.models import Movie

with open('movies_new.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Movie(movieid=row['movie_id'], title=row['movie_title'], year=row['release_date'])
	for i in row['genre']:
	   genre = Genre.objects.get(genre = i)
	   genre.save()
	   p.genres.add(genre)
    	p.save()

exit()
