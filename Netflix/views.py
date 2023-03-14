from django.shortcuts import render
from .forms import RegisterForm, LoginForm, SearchForm
from .models import Movie
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index_view(request):
    """ home page view """

    data = {}

    categories_to_display = ['Action', 'Adventure']

    # dictionary to map each category
    for category_name in categories_to_display:
        movies = Movie.objects.filter(category__name=category_name)
        if request.method == 'POST':
            search_text = request.POST.get('search_text')
            movies = movies.filter(name__icontains=search_text)

        data[category_name] = movies[:20]

    search_form = SearchForm()
    return render(request, 'Netflix/index.html',
                  {
                    'data': data.items(),
                    'search_form': search_form
                   }
                  )


def register_view(request):
    """ registration view """

    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 'Netflix/register.html', locals())
    else:
        # handle form submission
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            User.objects.create(
                first_name=request.POST.get('firstname'),
                last_name=request.POST.get('lastname'),
                email=request.POST.get('email'),
                username=request.POST.get('email'),
                password=make_password(request.POST.get('password'))
            )
            return HttpResponseRedirect('/login')

        return render(request, 'Netflix/register.html', locals())


def login_view(request):
    """ login view """
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'Netflix/login.html', locals())

    else:
        # get user credentials
        username = request.POST['email']
        password = request.POST['password']

        # authenticate
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        # if credentials are wrong redirect to login
        render(request, 'Netflix/login.html',
               {
                   'wrong_credentials': True,
                   'login_form': LoginForm(request.POST)
               })


def logout_view(request):
    """" logout view """

    logout(request)
    return HttpResponseRedirect('/')

def watch_movie_view(request):
    """ watch  view """
    movie_pk = request.GET.get('movie_pk')

    try:
        movie = Movie.objects.get(pk=movie_pk)
    except Movie.DoesNotExist:
        movie = None
    
    return render(request, 'Netflix/watch_movies.html', {'movie': movie})