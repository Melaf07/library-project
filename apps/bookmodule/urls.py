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
    path('html5/search/', views.search, name="books.search"),
    path('simple/query', views.simple_query, name="books.query"),
    path('complex/query', views.complex_query, name="books.cquery"),
    # path('lab8/task1', views.task1, name="books.t1"),
    # path('lab8/task2', views.task2, name="books.t2"),
    # path('lab8/task3', views.task3, name="books.t3"),
    # path('lab8/task4', views.task4, name="books.t4"),
    #path('lab8/task5', views.task5, name="books.t5"),
    #path('lab8/task7', views.task7, name="books.t7"),
    path('lab9/task1', views.task1, name="books.t1"),
    path('lab9/task2', views.task2, name="books.t2"),
    path('lab9/task3', views.task3, name="books.t3"),
    path('lab9/task4', views.task4, name="books.t4"),
    












]


  