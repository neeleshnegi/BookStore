from django.shortcuts import render,redirect
from .models import Book
# Create your views here.


def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        Book.objects.create(title=title,author=author,published_date=published_date)
        return redirect('read_book')
    return render(request,'books/create_book.html')

def read_book(request):
    books = Book.objects.all()
    return render(request,'books/read_book.html',{'books':books}) 


def update_book(request,book_id):
    book = Book.objects.get(id = book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('read_book')
    return render(request,'books/update_book.html',{'book':book})


def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('read_book')


