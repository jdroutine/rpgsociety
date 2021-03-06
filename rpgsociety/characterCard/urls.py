from django.urls import path
from .views import CharacterDetailView, CharacterView, HomeView, MapView, GalleryView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('character', CharacterView.as_view(), name="character"),
    path('character/<int:pk>', CharacterDetailView.as_view(), name="characterDetail"),
    path('map', MapView.as_view(), name="map"),
    path('gallery', GalleryView.as_view(), name="gallery"),
]
