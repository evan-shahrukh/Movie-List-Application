from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        "movie" : list(movies.values())
    }
    return JsonResponse(data)

def movie_detail(request,id):
    detail = Movie.objects.get(id=id)
    data = {
        "name" : detail.name,
        "description" : detail.description,
        "Active" : detail.active,
    }
    return JsonResponse(data)