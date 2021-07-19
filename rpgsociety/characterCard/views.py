from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Character
# def home(request):
#     return render(request, 'home.html',{})


class HomeView(ListView):
    model = Character
    template_name = "home.html"


class CharacterDetailView(DetailView):
    model = Character
    template_name = "characterDetail.html"


class CharacterView(ListView):
    model = Character
    template_name = "character.html"
