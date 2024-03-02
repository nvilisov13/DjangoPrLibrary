from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import *
from django.db.models import Avg
from django.db.models.functions import Round


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logout.html')


def index(request):
    return render(request, 'index.html')


def views_all_books(request):
    books_data = (Books.objects.all()
                  .values('id', 'author__id', 'author__first_name', 'author__last_name', 'name', 'description')
                  .annotate(avg_mark=Round(Avg('marksbooks__mark'), 2))
                  .order_by('id'))
    return render(request, 'views_all_books.html', {'books': books_data})


def get_authors(request):
    authors_data = (BooksAuthors.objects.all()
                    .values('id', 'first_name', 'last_name')
                    .order_by('first_name'))
    return authors_data


def add_authors(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        if first_name and last_name != '':
            author = BooksAuthors()
            author.first_name = first_name
            author.last_name = last_name
            author.save()
    return render(request, 'add_authors.html')


def add_books(request):
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        name_book = request.POST.get('name_book').strip()
        description = request.POST.get('description')
        if author_id and name_book != '':
            book = Books()
            book.name = name_book
            book.description = description
            book.author_id = author_id
            book.save()
    return render(request, 'add_books.html', {'authors': get_authors(request)})


def add_readers(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        telephone = request.POST.get('telephone').strip()
        if first_name and last_name != '':
            reader = Readers()
            reader.first_name = first_name
            reader.last_name = last_name
            reader.phone = telephone
            reader.save()
    return render(request, 'add_readers.html')


def take_book(request):
    books_data = Books.objects.exclude(pk__in=BooksReaders.objects.values_list('book', flat=True)).order_by('name')
    readers_data = Readers.objects.all().values('id', 'first_name', 'last_name').order_by('first_name')
    if request.method == 'POST':
        book_id = request.POST.get('book_id').strip()
        reader_id = request.POST.get('reader_id').strip()
        if book_id and reader_id != '':
            book_reader = BooksReaders()
            book_reader.book_id = request.POST.get('book_id')
            book_reader.reader_id = request.POST.get('reader_id')
            book_reader.save()
    return render(request, 'take_book.html', {'book': books_data, 'reader': readers_data})


def return_book(request):
    global book_reader
    books_data = (BooksReaders.objects.exclude(pk__in=Books.objects.values_list('name', flat=True))
                  .order_by('book__name'))
    if request.method == 'POST':
        book_id = request.POST.get('book_id').strip()
        mark = request.POST.get('mark')
        if book_id != '':
            try:
                book_reader = BooksReaders.objects.get(book=book_id)
                if mark != 0:
                    mark_book = MarksBooks()
                    mark_book.mark = mark
                    mark_book.reader_id = book_reader.reader_id
                    mark_book.book_id = book_reader.book_id
                    mark_book.save()
                book_reader.delete()
            except book_reader.DoesNotExist:
                return HttpResponseNotFound('<h1>Объект модели BooksReaders не существует в базе данных</h1>')
            except:
                return HttpResponseNotFound('<h1>Возникла ошибка при удалении связи книги с её читателем '
                                            'из Базы Данных</h1>')
    return render(request, 'return_book.html', {'book': books_data})


def rate_graph(request):
    book = {}
    marks_book = {}
    if request.method == 'GET':
        book_id = request.GET.get('book_id')
        if (book_id != '') and (book_id.isnumeric()):
            book = Books.objects.get(id=book_id)
            marks_book = MarksBooks.objects.filter(book_id=book_id).order_by('date_issue')
    return render(request, 'rate_graph.html', {'book': book, 'mark_book': marks_book})


def authors_del(request):
    books_authors = BooksAuthors.objects.filter(books__isnull=True)
    if request.method == 'POST':
        sel_authors = request.POST.getlist('authors[]')
        try:
            book_authors = BooksAuthors.objects.filter(id__in=sel_authors)
            book_authors.delete()
        except book_authors.DoesNotExist:
            return HttpResponseNotFound('<h1>Объект модели BooksAuthors не существует в базе данных</h1>')
        except:
            return HttpResponseNotFound('<h1>Возникла ошибка при удалении BooksAuthors из Базы Данных</h1>')
    return render(request, 'authors_del.html', {'books_author': books_authors})


def author_change(request):
    global author_id
    global book_author
    if request.method == 'GET':
        author_id = request.GET.get('author_id')
        if (author_id != '') and (author_id.isnumeric()):
            book_author = BooksAuthors.objects.get(id=author_id)
    if request.method == 'POST':
        del_author = request.POST.get('del_author')
        if del_author:
            try:
                book_author.delete()
            except book_author.DoesNotExist:
                return HttpResponseNotFound('<h1>Данные об авторе книг  не найдены в Базе Данных</h1>')
            except:
                return redirect('/authors_del.html')
        else:
            try:
                book_author.first_name = request.POST.get('first_name')
                book_author.last_name = request.POST.get('last_name')
                book_author.save()
            except:
                return HttpResponseNotFound('<h1>Не удалось внести данные об авторе книг в Базу Данных</h1>')
    return render(request, 'author_change.html', {'books_author': book_author})


def book_change(request):
    global book_id
    global book
    global authors
    if request.method == 'GET':
        book_id = request.GET.get('book_id')
        if (book_id != '') and (book_id.isnumeric()):
            book = Books.objects.get(id=book_id)
            authors = BooksAuthors.objects.exclude(id=book_id).order_by('first_name')
    if request.method == 'POST':
        del_book = request.POST.get('del_book')
        book = Books.objects.get(id=book_id)
        if del_book:
            try:
                book.delete()
            except book.DoesNotExist:
                return HttpResponseNotFound('<h1>Книга или её связанные данные не найдены в Базе Данных</h1>')
            except:
                return HttpResponseNotFound('<h1>Возникла ошибка при удалении книги из Базы Данных</h1>')
        else:
            try:
                book.name = request.POST.get('book_name')
                book.description = request.POST.get('book_desc')
                book.author_id = request.POST.get('author_sel')
                book.save()
            except:
                return HttpResponseNotFound('<h1>Возникла ошибка при изменении книги в Базе Данных</h1>')
    return render(request, 'book_change.html', {'books': book, 'books_authors': authors})


def views_all_readers(request):
    readers_data = Readers.objects.all()
    if request.method == 'POST':
        try:
            reader_del = Readers.objects.get(id=request.POST.get('del_reader'))
            reader_del.delete()
        except:
            return HttpResponseNotFound('<h1>Возникла ошибка при удалении Readers из Базы Данных</h1>')
    return render(request, 'views_all_readers.html', {'reader': readers_data})


def reader_change(request):
    global reader
    if request.method == 'GET':
        reader_id = request.GET.get('reader_id')
        if (reader_id != '') and (reader_id.isnumeric()):
            reader = Readers.objects.get(id=reader_id)
    if request.method == 'POST':
        reader.first_name = request.POST.get('first_name')
        reader.last_name = request.POST.get('last_name')
        reader.phone = request.POST.get('phone')
        reader.save()
    return render(request, 'reader_change.html', {'reader_sel': reader})
