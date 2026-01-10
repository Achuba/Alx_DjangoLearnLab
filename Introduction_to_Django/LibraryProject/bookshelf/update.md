# Updating a Book instannce

**Python command:**

```python

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

##Expected output:
<Book: Nineteen Eighty-Four>
```
