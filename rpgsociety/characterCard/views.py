from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Character, Home, Map
# def home(request):
#     return render(request, 'home.html',{})


class HomeView(ListView):
    model = Home
    template_name = "home.html"


class CharacterDetailView(DetailView):
    model = Character
    template_name = "characterDetail.html"


class CharacterView(ListView):
    model = Character
    template_name = "character.html"


class MapView(ListView):
    model = Map
    template_name = "map.html"


def gallery(request):
    return render(request, 'gallery.html', {})
