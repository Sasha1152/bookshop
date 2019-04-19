import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book



def get_books_list(request):
    books_list = Book.objects.all()
    return render(request, 'books.html', {'books': books_list})


def get_book(request, id):
    book = Book.objects.get(id=id)
    return HttpResponse(book)

def create_book(request):
    data = json.loads(request.body)
    new_book = Book.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new book where id={new_book.id}.')


def delete_book(request):
    data = json.loads(request.body)
    try:
        book = Book.objects.get(id=data['id'])
        book.delete()
        return HttpResponse(f'{request.method} method activated! Deleted book where id={data["id"]}.')
    except Book.DoesNotExist:
        return HttpResponse(f'Sorry, but book where id={data["id"]} does not exist')


def update_book(request):
    data = json.loads(request.body)
    try:
        book = Book.objects.get(id=data['id'])
        for key in data.keys():
            if key in book.__dict__.keys():
                book.__dict__[key] = data[key]
        book.save()
        return HttpResponse(f'{request.method} method activated! The book #{book.id} was updated"')
    except Book.DoesNotExist:
        return HttpResponse(f'Sorry, but book where id={data["id"]} does not exist')
