from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexx, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.format, name="books.formatting"),
    path('html5/listing/', views.list, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),
]


  