from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #asosiy
    path('search/', views.search, name="search"),
    path('posts/', views.posts, name='posts'),
    path('post/<int:id>/', views.post, name='post'),
    path('catigories/', views.categories, name = "categories"),
    path('catigories/<int:id>/', views.category, name = 'category'),
    path('register/', views.register, name="register"),
    path('post/<int:id>/comment', views.comment, name="comment"),
] 