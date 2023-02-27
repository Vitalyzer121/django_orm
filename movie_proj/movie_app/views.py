from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie, Director, Actor
from django.views.generic import ListView, DetailView


# Create your views here.

def show_all_movie(request):
    #movies = Movie.objects.order_by('name')
    movies = Movie.objects.annotate(
        true_bool = Value(True),
        false_bool = Value(False),
        str_field = Value('hello'),
        int_field = Value(123),
        new_budget = F('budget')+100,
        ffff=F('budget') * F('year'),
    )

    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg
    })

def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

def show_directors(request):
    name_directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {
        'name_directors' : name_directors
    })

def one_dir(request, id_dir):
    dir = get_object_or_404(Director, id=id_dir)
    return render(request, 'movie_app/director_info.html', {
        'dir': dir
    })

def show_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/actors.html', {
        'actors' : actors
    })

def info_actor(request, id_dir):
    actor = get_object_or_404(Actor, id=id_dir)
    return render(request, 'movie_app/info_actor.html', {
        'actor': actor
    })

class ListFeedBack(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor

class DetailFeedBack(DetailView):
    template_name = 'movie_app/detail_actor.html'
    model = Actor