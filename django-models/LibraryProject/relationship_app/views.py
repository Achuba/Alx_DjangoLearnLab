from django.shortcuts import render
from .models import Book
from django.views.generic import View
from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian

from .query_samples import query_books_by_author, list_books_in_library, get_librarian_of_library

# Create your views here.

def book_list_view(request):
    books = Book.objects.select_related ('author', 'library')
    output = '\n '.join([f"{book.title} by {book.author.name}" for book in books])
    return render (request, 'book_list.html', {'output': output})


class LibraryDetailView(View):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        context['librarian'] = Librarian.objects.get(library=library)
        return context