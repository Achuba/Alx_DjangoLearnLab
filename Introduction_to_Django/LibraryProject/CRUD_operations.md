// **create.md**
book = Book.objects.create (
title="1984",
author="George Orwell",
published_year="1946"
)

// **retrieve.md**
book = Book.objects.get(title="1984")
book.title, book.author, book.published_year

// **Update**
book.title = "Nineteen Eighty-Four"
book.save()
book

// **Delete**
book.delete()
Book.objects.all()
