from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Book, Author, Language, Genre


def index(request):
    """
    Display function for the site's home page.
    """

    # Get genres
    genres = ''
    for value in Genre.objects.all():
        genres += value.name + ', '
    genres = genres[:-2]

    # Get author's info
    author_data = Author.objects.all()

    # Get book's info
    book_data = Book.objects.all()

    # Number of visits to this view, as counted in the session variable.
    new_visits = request.session.get('new_visits', 0)
    request.session['new_visits'] = new_visits + 1

    context = {'author_data': author_data,
               'book_data': book_data,
               'new_visits': new_visits,
               'genre': Genre,
               }

    # Drawing an HTML template index.html with data inside
    # context variable
    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 12


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


class UserFavoritesBooksListView(LoginRequiredMixin, generic.ListView):
    """
    A class-based view that shows the user's book favorites
    """
    model = Book
    template_name = 'catalog/favorite_user_books.html'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter(favorites=self.request.user)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
