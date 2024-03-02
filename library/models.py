from django.db import models


class BooksAuthors(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя автора')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия автора')

    class Meta:
        verbose_name = 'автора книг'
        verbose_name_plural = 'Авторы Книг'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name}'


class Books(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название книги')
    description = models.TextField(blank=True, verbose_name='Описание книги')
    author = models.ForeignKey(BooksAuthors, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'Книги'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id} - {self.name} {self.description} | {self.author}'


class Readers(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = models.CharField(max_length=12, null=True, verbose_name='Телефон')

    class Meta:
        verbose_name = 'читателя'
        verbose_name_plural = 'Читатели'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name} {self.phone}'


class BooksReaders(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Книга')
    reader = models.ForeignKey(Readers, on_delete=models.CASCADE, verbose_name='Читатель')

    class Meta:
        verbose_name = 'книгу которая на руках у читателя'
        verbose_name_plural = 'Книги на руках'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id} - {self.book} {self.reader}'


class MarksBooks(models.Model):
    mark = models.SmallIntegerField(verbose_name='Оценка')
    date_issue = models.DateField(auto_now_add=True, verbose_name='Дата оценки')
    reader = models.ForeignKey(Readers, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Книга')

    class Meta:
        verbose_name = 'оценку книге'
        verbose_name_plural = 'Оценки книгам'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id} - {self.mark} {self.date_issue} || {self.reader} || {self.book}'
