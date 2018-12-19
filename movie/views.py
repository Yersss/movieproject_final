from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from movie.models import *
from django.http import HttpResponse
from .models import addMovies
import json
import math
import csv
import pandas as pd
import numpy as np

# Create your views here.
def add_seen(request, movie_id):
    if request.is_ajax():
        history = Seen.objects.filter(movieid_id=movie_id, username=request.user.get_username())
        if len(history) == 0:
            new_record = Seen(movieid_id=movie_id, username=request.user.get_username())
            new_record.save()
            return HttpResponse('1')
        else:
            history.delete()
            return HttpResponse('0')

def add_expect(request, movie_id):
    if request.is_ajax():
        history = Expect.objects.filter(movieid_id=movie_id, username=request.user.get_username())
        if len(history) == 0:
            new_record = Expect(movieid_id=movie_id, username=request.user.get_username())
            new_record.save()
            return HttpResponse('2')
        else:
            history.delete()
            return HttpResponse('0')

@csrf_protect
def detail(request, model, id):
    #items = []
    try:
        if model.get_name() == 'movie' and id != 'None':
            label = 'actor'
            object = model.objects.get(movieid=id)
            items = ''
            for i in object.genres.all():
                items = items + i.genre +', '
            if request.user.get_username() != '':
                seen_list = [str(x).split('|')[1] for x in
                             Seen.objects.filter(username=request.user.get_username())]
                expect_list = [str(y).split('|')[1] for y in
                               Expect.objects.filter(username=request.user.get_username())]
                if id in seen_list:
                    object.flag = 1
                if id in expect_list:
                    object.flag = 2
    except:
        return render(request, '404.html')
    return render(request, '{}_list.html'.format(label), {'items': items, 'number': len(items), 'object': object})

def whole_list(request, model, page):
    page = int(page)
    objects = model.objects.all()
    total_page = int(math.ceil(len(objects) / 10))
    if page > total_page:
        return render(request, '404.html')
    last_item_index = 10 * page if page != total_page else len(objects)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects[10 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request, '{}_list.html'.format(model.get_name()), data)

@csrf_protect
def seen(request, movie_id):
    if request.POST:
        try:
            d = Seen.objects.get(username=request.user.get_username(), movieid_id=movie_id)
            d.delete()
        except:
            return render(request, '404.html')
    records = Seen.objects.filter(username=request.user.get_username())
    movies = []
    for record in records:
        movie_id = str(record).split('|')[1]
        movies.append(Movie.objects.get(movieid=movie_id))
    return render(request, 'seen.html', {'items': movies, 'number': len(movies)})


def expect(request, movie_id):
    if request.POST:
        try:
            d = Expect.objects.get(username=request.user.get_username(), movieid_id=movie_id)
            d.delete()
        except:
            return render(request, '404.html')
    records = Expect.objects.filter(username=request.user.get_username())
    movies = []
    for record in records:
        movie_id = str(record).split('|')[1]
        movies.append(Movie.objects.get(movieid=movie_id))
    return render(request, 'expect.html', {'items': movies, 'number': len(movies)})

def profile(request):
    genres_all = []
    movies = Seen.objects.filter(username = request.user.get_username())
    # print(movies.movieid_id)
    for i in movies:
        for y in i.movieid.genres.all():
            genres_all.append(y.genre)
    counts = [1]*len(genres_all)
    for i in range(len(genres_all)):
        for y in range(len(genres_all)):
            if(i==y):
                continue
            if(genres_all[i]==genres_all[y]):
                counts[i]+=1
    ids = []
    max = 0
    for i in range(len(counts)):
        if(counts[i]>=max):
            ids.append(i)
            max = counts[i]
    genres_recom = []
    for i in ids:
        if(counts[i]!=max):
            continue
        genres_recom.append(genres_all[i])
    genres_recom = set(genres_recom)
    genres_recom = list(genres_recom)
    movies_all = Movie.objects.all()
    GGG = []
    for i in movies_all:
        ggg = []
        for y in i.genres.all():
            ggg.append(y.genre)
        GGG.append(ggg)
    movies_recom = []
    for i in range(len(GGG)):
        cnt = 0
        for y in GGG[i]:
            for z in genres_recom:
                if(y==z):
                    cnt+=1
        movies_recom.append(cnt)

    recom = []
    max = 0
    for i in range(len(movies_recom)):
        if(movies_recom[i]>=max):
            recom.append(i)
            max = movies_recom[i]

    final = []
    for i in recom:
        final.append(movies_all[i])

    data = {}
    data['rec'] = final
    data['genres'] = genres_recom

    genres_new = []
    counts_new = []
    for i in range(len(genres_all)):
        if(genres_all[i] not in genres_new):
            genres_new.append(genres_all[i])
            counts_new.append(counts[i])

    all = []
    for i in range(len(genres_new)):
        all.append(genres_new[i] + ' ' + str(counts_new[i]))
    data['all'] = all


    return render (request, 'profile.html', data)

def search(request):
    if request.GET.get('search'):
        search_value = request.GET['search']
        movies = Movie.object.filter(title__contains=search_value)
        return render(request, 'movie/movie_search.html', {'movies': movies, 'search_value': search_value, 'query_string0': query_string})
