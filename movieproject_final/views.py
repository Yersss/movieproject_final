from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from movie.models import *


@csrf_protect
def index(request):
    data = {}
    return render(request, 'base.html', data)
