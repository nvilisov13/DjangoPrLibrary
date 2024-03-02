from django.urls import path, include
from . import views
from . import drfviews
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'drf_authors_book', drfviews.BooksAuthorViewSet)
router.register(r'drf_book', drfviews.BookViewSet)
router.register(r'drf_author_books', drfviews.AuthorBooksViewSet)
router.register(r'drf_reader', drfviews.ReaderViewSet)
router.register(r'drf_books_reader', drfviews.BooksReaderViewSet)
router.register(r'drf_marks_book', drfviews.MarksBookViewSet)

urlpatterns = [
    path('', views.index),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('views_all_books', views.views_all_books),
    path('add_authors', views.add_authors),
    path('add_books', views.add_books),
    path('add_readers', views.add_readers),
    path('take_book', views.take_book),
    path('return_book', views.return_book),
    path('rate_graph.html', views.rate_graph),
    path('author_change.html', views.author_change),
    path('book_change.html', views.book_change),
    path('authors_del.html', views.authors_del),
    path('views_all_readers.html', views.views_all_readers),
    path('reader_change.html', views.reader_change),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('drf_books_authors_table_id.html', drfviews.drf_books_authors_table_id),
    path('drf_books_table_id.html', drfviews.drf_books_table_id),
    path('drf_readers_table_id.html', drfviews.drf_readers_table_id),
    path('drf_books_readers_table_id.html', drfviews.drf_books_readers_table_id),
    path('drf_marks_books_table_id.html', drfviews.drf_marks_books_table_id),
]
