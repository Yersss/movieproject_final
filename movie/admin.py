from django.contrib import admin
from .models import Movie, Seen, Genre, Expect
# Register your models here.

admin.site.register(Movie)
admin.site.register(Seen)
admin.site.register(Genre)
admin.site.register(Expect)
