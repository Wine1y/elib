from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from django.utils.translation import gettext_lazy as _

from books.models import Book, BookSerializer
from users.models import BookOwnership, BookOwnershipSerializer
from api.permissions.users import IsReader


class BookIDSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class BooksListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.order_by("id")

class MyBooksListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsReader]
    serializer_class = BookOwnershipSerializer

    def get_queryset(self):
        return BookOwnership.objects.filter(user=self.request.user).order_by("book__name")

class TakeBookView(GenericAPIView):
    permission_classes = [IsAuthenticated, IsReader]
    serializer_class = BookIDSerializer

    def post(self, request: Request) -> Response:
        serializer = BookIDSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(pk=serializer.validated_data["id"])
        except Book.DoesNotExist:
            return Response({"detail": _("Book not found")}, status=status.HTTP_404_NOT_FOUND)

        if request.user.books.contains(book):
            return Response({"detail": _("You already have this book")}, status=status.HTTP_403_FORBIDDEN)
        
        request.user.books.add(book)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReturnBookView(GenericAPIView):
    permission_classes = [IsAuthenticated, IsReader]
    serializer_class = BookIDSerializer

    def post(self, request: Request) -> Response:
        serializer = BookIDSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(pk=serializer.validated_data["id"])
        except Book.DoesNotExist:
            return Response({"detail": _("Book not found")}, status=status.HTTP_404_NOT_FOUND)
        
        if not request.user.books.contains(book):
            return Response({"detail": _("You do not own this book")}, status=status.HTTP_404_NOT_FOUND)
        
        request.user.books.remove(book)
        return Response(status=status.HTTP_204_NO_CONTENT)