from django.contrib import admin
from .models import Movie, Genre, Expect, Seen
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'movieid','year')
    list_filter =('year',)
    search_fields = ('title',)
    ordering = ['-year']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Expect)
admin.site.register(Seen)
