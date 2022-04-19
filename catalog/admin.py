from django.contrib import admin
from .models import Author, Genre, Language, Book

# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(Book)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'), ('short_biography', 'biography'), 'photo']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    fields = ['title', 'author', 'summary', 'image', 'genre', 'language', 'isbn', 'favorites', ]
