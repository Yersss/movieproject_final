from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from movie.models import *
import pandas as pd
from movie.models import addMovies

@csrf_protect
def index(request):
    data = {}
    # addMovies(request)
    if request.user.is_authenticated:
        data = {'username': request.user.get_username()}
    newest_movies = Movie.objects.all().order_by('-year')
    newest = []
    for movie in newest_movies[:5]:
        try:
            newest.append({'movieid': movie.movieid, 'title': movie.title})
        except:
            continue
    #print(newest)
    data['newest'] = newest
    newest_movie_list = [movie.title for movie in newest_movies[:5]]
    most_viewed_list = pd.read_csv('most_viewed.csv')
    most_viewed = []
    for i in range(5):
        try:
            most_viewed.append({'movieid': str(most_viewed_list.iloc[i]['movie_id']), 'title': most_viewed_list.iloc[i]['movie_title']})
        except:
            continue
    data['most_viewed'] = most_viewed
    simple_recom_list = pd.read_csv('recom_simple.csv')
    simple_recom = []
    for i in range(5):
        try:
            simple_recom.append({'movieid': str(simple_recom_list.iloc[i]['movie_id']), 'title': simple_recom_list.iloc[i]['movie_title']})
        except:
            continue
    data['simple_recom'] = simple_recom
    #data['recommendation'] = get_recommendation(request, popular_movie_list)
    return render(request, 'base.html', data)

def get_recommendation(request, popular_movie_list):
    result = []
    movie_dict = search_index.data_in_memory['movie_dict']
    added_movie_list = []
    if request.user.is_authenticated:
        username = request.user.get_username()
        watched_movies = set([movie_dict[movie.movieid_id] for movie in Seen.objects.filter(username=username)] +
                             [movie_dict[movie.movieid_id] for movie in Expect.objects.filter(username=username)])
        unwatched_movies = set(search_index.data_in_memory['movie_list']) - watched_movies - set(popular_movie_list)
        genre_stats = {}
        for movie in watched_movies:
            for genre in movie.genres.split('|'):
                genre_stats[genre] = genre_stats.get(genre, 0) + 1
        movie_score = {}
        for movie in unwatched_movies:
            movie_score[movie.movieid] = movie.rate
            for genre in movie.genres.split('|'):
                movie_score[movie.movieid] += genre_stats.get(genre, 0) / len(watched_movies)
        sorted_list = sorted(movie_score.items(), key=operator.itemgetter(1), reverse=True)
        for item in sorted_list:
            movie = movie_dict[item[0]]
            result.append({'movieid': movie.movieid, 'poster': movie.poster})
            added_movie_list.append(movie)
            if len(result) == 8:
                break
    sorted_list = sorted(search_index.data_in_memory['movie_rating'].items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_list:
        movie = movie_dict[item[0]]
        if movie not in popular_movie_list and movie not in added_movie_list:
            result.append({'movieid': movie.movieid, 'poster': movie.poster})
        if len(result) == 10:
            break
    return [result[i] for i in random.sample(range(len(result)), 5)]
