from django.shortcuts import  render ,redirect
from lms_app.forms import BookForm
from lms_app.models import Category
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()


    book = Book.objects.all()
    count = Book.objects.filter(active=True).count()
    category =Category.objects.all()
    booksold = Book.objects.filter(status='sold').count()
    bookrental = Book.objects.filter(status='rental').count()
    bookavailble = Book.objects.filter(status='availble').count()
    context = {
        'book':book,
         'count':count,
         'category':category,
         'BookForm':BookForm,
         'CategoryForm':CategoryForm,
         'booksold':booksold,
         'bookrental':bookrental,
         'bookavailble':bookavailble
         }

    return render(request ,"index.html",context)
@csrf_exempt
def delete(request,id):
    book_delete = Book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')


    return render(request ,"delete.html",{})


@csrf_exempt
def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_update = BookForm(request.POST, request.FILES, instance=book_id)
        if book_update.is_valid():
            book_update.save()
            return redirect('/')
    else:
        book_update =  BookForm(instance=book_id)        

        

    context = {'book':book_update,}

    return render(request ,"update.html",context)

def books(request):
    ser = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            ser = ser.filter(title__icontains=title)
    book = ser
    category = Category.objects.all()
    context = {'book':book,'category':category,'CategoryForm':CategoryForm,}

    return render(request ,"books.html",context)

