from django.db import models
import csv
import os
# Create your models here.
#
class Genre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre

class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.movieid + '|' + self.title

    @staticmethod
    def get_name():
        return 'movie'



class Seen(models.Model):
    username = models.CharField(max_length=150)
    movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.username + '|' + self.movieid.movieid


class Expect(models.Model):
    username = models.CharField(max_length=150)
    movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.username + '|' + self.movieid.movieid

def addMovies(request):
    with open('movies_new.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        genres = []
        for row in reader:
            p = Movie(movieid=row['movie_id'], title=row['movie_title'], year=row['release_date'])
            i = row['genre']
            i = i.replace('[', '')
            i = i.replace(']', '')
            i = i.replace("'",'')
            i = i.replace(' ', '')
            arr = i.split(',')
            # for k in arr:
            #     if k not in genres:
            #         genres.append(k)
            p.save()
            for j in arr:
               genre = Genre.objects.get(genre = j)
               genre.save()
               p.genres.add(genre)
               p.save()
