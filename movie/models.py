from django.db import models

# Create your models here.
<<<<<<< HEAD
class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    genres = models.CharField(max_length=100)

    def __str__(self):
        return self.movieid + '|' + self.title

    @staticmethod
    def get_name():
        return 'movie'
=======
>>>>>>> 8bd88c93c991ce647e25dc99385f55fe90056418
