# Retrieving a Book instannce

**Python command:**

```python

book = Book.objects.get(title="1984")
book.title, book.author, book.published_year

## Expected output:
('1984', 'George Orwell', 1949)
```
