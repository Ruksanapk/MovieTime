from django.shortcuts import render,redirect
from .views import *
from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        if 'add_to_favorites' in request.POST:
            movie.is_favorite = True
            movie.save()
        elif 'remove_from_favorites' in request.POST:
            movie.is_favorite = False
            movie.save()
    return render(request, 'movie_detail.html', {'movie': movie})

def favorites(request):
    favorite_movies = Movie.objects.filter(is_favorite=True)
    return render(request, 'favorites.html', {'favorite_movies': favorite_movies})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('movie_list')  
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'login.html')


def user_register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()

    return render(request,"register.html",{'form':form})



def search_results(request):
    query = request.GET.get('q', '')
    movies = Movie.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'movies': movies, 'query': query})
def user_logout(request):
    logout(request)
    return redirect ('user_login')
@login_required(login_url='user_login')
def movie(request):
     movies=Movie.objects.all()
     return render(request,'movie.html',{'movies':movies})