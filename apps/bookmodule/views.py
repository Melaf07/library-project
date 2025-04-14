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

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'books/bookList.html', {'books':newBooks})
    else:
        return render(request, 'books/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

from .models import Book

def simple_query(request):
    if not Book.objects.exists(): 
        Book.objects.create(title="Continuous Delivery", author="J.Humble and D. Farley",price='120.00',edition='3')
        Book.objects.create(title="Reversing: Secrets of Reverse Engineer", author="E. Eilam",price='97.00',edition='2')
        Book.objects.create(title="The Hundred-Page Machine Learning Book", author="Andriy Burkov",price='100.00',edition='4')
        Book.objects.create(title="Clean Code", author="Robert C. Martin", price='85.00', edition='1')
        Book.objects.create(title="Design Patterns: Elements of Reusable Object-Oriented Software", author="Erich Gamma et al.", price='70.00', edition='2')
        Book.objects.create(title="Introduction to the Theory of Computation", author="Michael Sipser", price='95.00', edition='3')
        Book.objects.create(title="Python Crash Course", author="Eric Matthes", price='75.00', edition='2')
        Book.objects.create(title="Deep Learning with Python", author="François Chollet", price='50.00', edition='2')
    mybooks = Book.objects.all()  # <- multiple objects
    return render(request, 'books/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks= books =Book.objects.filter(author__isnull = False).filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'books/booklist.html', {'books':mybooks})
    else:
        return render(request, 'books/indexx.html')

from django.db.models import Q

def task1(request):
    mybooks = Book.objects.filter(Q(price__lte = 80))
    if mybooks.exists():
        return render(request, 'books/bookprice.html', {'books': mybooks})
    else:
        return render(request, 'books/indexx.html')    

def task2(request):
    mybooks = Book.objects.filter(Q(edition__gte=3) & ( Q(title__icontains='co') | Q(author__icontains='co')))
    if mybooks.exists():
        return render(request, 'books/booklist.html', {'books': mybooks})
    else:
        return render(request, 'books/indexx.html') 

def task3(request):
    mybooks = Book.objects.filter(~Q(edition__gte=3) & ( ~Q(title__icontains='co') | ~Q(author__icontains='co')))
    if mybooks.exists():
        return render(request, 'books/booklist.html', {'books': mybooks})
    else:
        return render(request, 'books/indexx.html') 
    
def task4(request):
    mybooks = Book.objects.order_by('title')
    return render(request, 'books/booklist.html', {'books': mybooks})
 
from django.db.models import Sum , Min , Max , Count , Avg

def task5(request):
    stats = Book.objects.aggregate(total_books=Count('id'),total_price=Sum('price'),
        ave_price=Avg('price'),max_price=Max('price'),min_price=Min('price'),
    )

    return render(request, 'books/stats.html', {'stats': stats})

from .models import Student, Address


def task7(request):
    data = Student.objects.values('address__city').annotate(total=Count('id')).order_by('-total')
    return render(request, 'books/student.html', {'data': data})