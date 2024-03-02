from .models import *
from rest_framework import serializers


class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthors
        fields = ('__all__')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('__all__')


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readers
        fields = ('__all__')


class BooksReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksReaders
        fields = ('__all__')


class MarksBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarksBooks
        fields = ('__all__')


class BooksAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthors
        fields = ('id', 'first_name', 'last_name')


class BooksSerializer(serializers.ModelSerializer):
    author = BooksAuthorsSerializer()

    class Meta:
        model = Books
        fields = ('id', 'name', 'description', 'author')
