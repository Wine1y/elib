from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View

from users.models import UserType
from books.views import BooksListView, BookOwnersListView


class IndexView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_anonymous or request.user.user_type == UserType.READER:
            return BooksListView.as_view()(request, *args, **kwargs)
            
        return BookOwnersListView.as_view()(request, *args, **kwargs)
                