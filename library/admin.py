from django.contrib import admin
from .models import *


class BooksAuthorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'author_id']
    list_filter = ['author_id']


class BooksReadersAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_id', 'reader_id']


class ReadersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone']
    list_filter = ['phone']


class MarksBooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'mark', 'date_issue', 'reader_id', 'book_id']
    list_filter = ['mark']


admin.site.register(BooksAuthors, BooksAuthorsAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(BooksReaders, BooksReadersAdmin)
admin.site.register(Readers, ReadersAdmin)
admin.site.register(MarksBooks, MarksBooksAdmin)
