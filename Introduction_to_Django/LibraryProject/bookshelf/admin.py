from django.contrib import admin
from Introduction_to_Django.LibraryProject.bookshelf.models import Book

# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')

    list_filter = ('author', 'published_year')

    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
