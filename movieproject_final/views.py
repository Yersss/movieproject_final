from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from movie.models import *
from movie.models import addMovies

@csrf_protect
def index(request):
    data = {}
    # addMovies(request)

    return render(request, 'base.html', data)
