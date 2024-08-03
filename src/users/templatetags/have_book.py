from django import template


from users.models import User
from books.models import Book


register = template.Library()

@register.filter(name="have_book")
def have_book(user: User, book: Book) -> bool:
    return user.books.contains(book)
