from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('watch/', views.watch_movie_view, name='watch_movie'),
    path('logout', views.logout_view, name='logout'),

]





