from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User


class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1500, help_text="Enter a brief description of the book")
    image = models.ImageField(upload_to='book_image', blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=17, help_text="Enter a book's ISBN")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined, so we can specify the object above.
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    favorites = models.ManyToManyField(User, help_text='Choose favorite books', related_name='created', blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        genre = [genre.name for genre in self.genre.all()[:3]]
        if len(genre) >= 2:
            genre_string = ''
            for value in genre:
                genre_string += value + ', '
            return genre_string[:-2]
        else:
            return genre
    display_genre.short_description = 'Genre'


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    short_biography = models.TextField(max_length=550, default='Write a little about the author')
    biography = models.TextField(max_length=10000, default='Write more about the author',
                                 help_text='Enter information about writer')
    photo = models.ImageField(upload_to='photo', blank=True, null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f'{self.last_name}, {self.first_name}'
