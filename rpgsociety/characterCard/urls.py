from django.urls import path
#from . import views
from .views import CharacterDetailView, CharacterView, HomeView, MapView


urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('character', CharacterView.as_view(), name="character"),
    path('character/<int:pk>', CharacterDetailView.as_view(), name="characterDetail"),
    path('map', MapView.as_view(), name="map"),
]
