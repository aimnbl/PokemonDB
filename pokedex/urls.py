from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemain),
    path('search/', views.search),
    path('pokemon/', views.pokeprofile)
]