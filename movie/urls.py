from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('base/', base, name='base'),
    path('movie_list/', movie_list, name='movie_list'),
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('home/', home, name='home'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movie_detail/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('favorites/', favorites, name='favorites'),
    path('search_movies/', search_results, name='search_movies'),
    path('search_results/', search_results, name='search_results'),
   
    path('logout/',user_logout,name='logout'),
   
]