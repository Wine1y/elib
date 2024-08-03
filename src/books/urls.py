from django.urls import path


from .views import MyBooksListView

app_name = "books"
urlpatterns = [
    path('my', MyBooksListView.as_view(), name='my_books'),
]