# Deleting a Book instannce

**Python command:**

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

## Expected output:
<QuerySet []>

```
