from .views import *
from .serializers import *
from .permissions import AllForOtherReadOnly
from rest_framework import viewsets, filters


def drf_books_table_id(request):
    books_data = Books.objects.all().values('id', 'name', 'description', 'author_id').order_by('id')
    return render(request, 'drf_books_table_id.html', {'books': books_data})


def drf_books_authors_table_id(request):
    books_authors_data = BooksAuthors.objects.all().values('id', 'first_name', 'last_name').order_by('id')
    return render(request, 'drf_books_authors_table_id.html', {'books_author': books_authors_data})


def drf_readers_table_id(request):
    readers_data = Readers.objects.all().values('id', 'first_name', 'last_name', 'phone').order_by('id')
    return render(request, 'drf_readers_table_id.html', {'readers': readers_data})


def drf_books_readers_table_id(request):
    books_readers_data = BooksReaders.objects.all().values('id', 'book_id', 'reader_id').order_by('id')
    return render(request, 'drf_books_readers_table_id.html', {'books_readers': books_readers_data})


def drf_marks_books_table_id(request):
    marks_books_data = (MarksBooks.objects.all().values('id', 'mark', 'date_issue', 'reader_id', 'book_id')
                        .order_by('id'))
    return render(request, 'drf_marks_books_table_id.html', {'marks_books': marks_books_data})


class BooksAuthorViewSet(viewsets.ModelViewSet):
    queryset = BooksAuthors.objects.all()
    serializer_class = BooksAuthorSerializer
    permission_classes = (AllForOtherReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllForOtherReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Readers.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = (AllForOtherReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class BooksReaderViewSet(viewsets.ModelViewSet):
    queryset = BooksReaders.objects.all()
    serializer_class = BooksReaderSerializer
    permission_classes = (AllForOtherReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class MarksBookViewSet(viewsets.ModelViewSet):
    queryset = MarksBooks.objects.all()
    serializer_class = MarksBookSerializer
    permission_classes = (AllForOtherReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class AuthorBooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('id')
    serializer_class = BooksSerializer
    permission_classes = (AllForOtherReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['author__first_name', 'author__last_name', 'name']
    ordering_fields = ['author__first_name', 'author__last_name', 'id', 'name']
