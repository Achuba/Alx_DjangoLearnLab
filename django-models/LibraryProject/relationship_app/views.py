from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic import View
from django.shortcuts import render
from relationship_app.models import Author, Book, Library, Librarian

from .query_samples import query_books_by_author, list_books_in_library, get_librarian_of_library

# Create your views here.

def list_books(request):
   books = Book.objects.all()
   return render(request, 'relationship_app/list_books.html', {'books': books})

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