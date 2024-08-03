from typing import Any

from django.db import models

from .user import User, UserType
from users.managers import UserManager


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_number = models.AutoField(primary_key=True)

class LibrarianManager(UserManager):
    def get_queryset(self) -> models.QuerySet[User]:
        return super().get_queryset().filter(user_type=UserType.LIBRARIAN)

    def create(self, **kwargs: Any) -> User:
        kwargs["user_type"] = UserType.LIBRARIAN
        return super().create(**kwargs)
    
    def create_user(self, username,  password, **extra_fields):
        user = self.create(username=username, **extra_fields)
        user.set_password(password)
        user.save()

        Librarian.objects.create(user=user)
        return user

class LibrarianUser(User):
    objects = LibrarianManager()
    class Meta:
        proxy = True
        verbose_name = "Librarian"

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.TextField(max_length=35)
    last_name = models.TextField(max_length=35)
    address = models.TextField(max_length=120)

class ReaderManager(UserManager):
    def get_queryset(self) -> models.QuerySet[User]:
        return super().get_queryset().filter(user_type=UserType.READER)
    
    def create(self, **kwargs: Any) -> User:
        kwargs["user_type"] = UserType.READER
        return super().create(**kwargs)

class ReaderUser(User):
    objects = ReaderManager()

    class Meta:
        proxy = True
        verbose_name = "Reader"