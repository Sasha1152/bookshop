from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_books_list, name='books_list'),
    path('<int:book_id>', views.retrieve, name='book'),
    path('create', views.create, name='create'),
    path('update', views.update, name='update'),
]
