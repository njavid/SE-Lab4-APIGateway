from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('create-book/', views.createBook, name='create-book'),
    path('update-book/', views.updateBook, name='update-book'),
    # path('delete-book/', views.deleteBook, name='delete-book'),
    # path('read-book/', views.readBook, name='read-book'),

]