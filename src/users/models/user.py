from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from ..managers import UserManager
from books.models import Book, BookSerializer

class UserType(models.IntegerChoices):
    LIBRARIAN = (1, _("Librarian"))
    READER = (2, _("Reader"))

class User(AbstractBaseUser, PermissionsMixin):
    username = models.TextField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    signup_date = models.DateTimeField(default=timezone.now)
    user_type = models.IntegerField(choices=UserType.choices, default=UserType.READER)
    books = models.ManyToManyField(Book, through="BookOwnership")

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return f"{self.username}(#{self.id})"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "signup_date", "user_type"]

class BookOwnership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(default=timezone.now)

class BookOwnershipSerializer(ModelSerializer):
    book = BookSerializer()
    seconds_owning = SerializerMethodField("get_seconds_owning")

    def get_seconds_owning(self, book_ownership: BookOwnership) -> str:
        return round(timezone.now().timestamp()-book_ownership.date_issued.timestamp())

    class Meta:
        model = BookOwnership
        fields = ["book", "date_issued", "seconds_owning"]