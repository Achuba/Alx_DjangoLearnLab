import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
import django 
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return [book.title for book in books]

def list_books_in_library(library_name):
    books = Book.objects.filter(library__name=library_name)
    return [book.title for book in books]

def get_librarian_of_library(library_name):
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        return librarian.name
    except Librarian.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None
