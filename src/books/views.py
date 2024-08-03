from django.views.generic import ListView
from django.db.models import QuerySet
from elib.mixins import LoginRequiredMixin, IsReaderMixin, IsLibrarianMixin

from .models import Book
from users.models import BookOwnership


class BooksListView(ListView):
    paginate_by = 5
    model = Book
    template_name = "books_list.html"

    def get_queryset(self) -> QuerySet[Book]:
        return self.model.objects.order_by('name')

class BookOwnersListView(LoginRequiredMixin, IsLibrarianMixin, ListView):
    paginate_by = 5
    model = BookOwnership
    template_name = "book_owners_list.html"

    def get_queryset(self) -> QuerySet[BookOwnership]:
        return self.model.objects.order_by("date_issued")

class MyBooksListView(LoginRequiredMixin, IsReaderMixin, ListView):
    paginate_by = 5
    model = BookOwnership
    template_name = "my_books_list.html"

    def get_queryset(self) -> QuerySet[BookOwnership]:
        return self.model.objects.filter(user=self.request.user).order_by("book__name")
