from django.urls import path

from api.views.books import BooksListView, MyBooksListView, TakeBookView, ReturnBookView

app_name = "books_api"
urlpatterns = [
    path('', BooksListView.as_view(), name="list_books"),
    path('my', MyBooksListView.as_view(), name="list_my_books"),
    path('take', TakeBookView.as_view(), name="take_book"),
    path('return', ReturnBookView.as_view(), name="return_book"),
]