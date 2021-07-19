from django.urls import path
#from . import views
from .views import CharacterDetailView, CharacterView, HomeView


urlpatterns = [
    #path('', views.home, name="home"),
    path('',HomeView.as_view(), name="home"),
    path('character/<int:pk>', CharacterDetailView.as_view(), name="characterDetail"),
    path('character', CharacterView.as_view(), name="character"),
]
