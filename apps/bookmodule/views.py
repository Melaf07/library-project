from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "books/index.html" , {"name": name})  

from django.http import HttpResponse
def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1)) 

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, "books/show.html", context)

def indexx(request):
    return render(request, "books/indexx.html")
 
def list_books(request):
    return render(request, 'books/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'books/one_book.html')
 
def aboutus(request):
    return render(request, 'books/aboutus.html')

def links(request):
    return render(request, 'books/links.html')
def format(request):
    return render(request, 'books/formatting.html')
def list(request):
    return render(request, 'books/list.html')
def tables(request):
    return render(request, 'books/tables.html')