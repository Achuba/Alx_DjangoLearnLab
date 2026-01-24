from django.views.generic import View
from django.shortcuts import render , redirect , get_object_or_404
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.shortcuts import render
from bookshelf.models import Author, Book, Library, Librarian
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .query_samples import query_books_by_author, list_books_in_library, get_librarian_of_library
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here
def home(request):
    return render(request, "bookshelf/home.html")

def list_books(request):
   books = Book.objects.all()
   return render(request, 'bookshelf/list_books.html', {'books': books})    
class LibraryDetailView(View):
    model = Library
    template_name = 'bookshelf/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        context['librarian'] = Librarian.objects.get(library=library)
        return context
    
class UserLoginView(LoginView):
    template_name = 'bookshelf/login.html'
class UserLogoutView(LogoutView):
    next_page = 'login'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list-books')
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "Admin"


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "Librarian"


def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "bookshelf/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "bookshelf/librarian_view.html")
@user_passes_test(is_member)
def member_view(request):
    return render(request, "bookshelf/member_view.html")


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        library_id = request.POST.get('library')
        Book.objects.create(title=title, author_id=author_id, library_id=library_id)
        return redirect('list-books')
    return render(request, 'bookshelf/add_book.html')

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('list-books')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list-books')
    return render(request, 'bookshelf/delete_book.html', {'book': book})