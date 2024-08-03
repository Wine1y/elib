from typing import Any

from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationFrom,
                                       UserChangeForm as DjangoUserChangeForm,
                                       AuthenticationForm as DjangoUserAuthForm)
from django.db.transaction import atomic
from django import forms

from .models import User, UserType, Librarian, Reader

class UserCreationForm(DjangoUserCreationFrom):

    class Meta:
        model = User
        fields = ("username",)

class LibrarianCreationForm(UserCreationForm):
    
    @atomic
    def save(self, commit: bool=True) -> Any:
        user = super().save(commit=False)
        user.user_type = UserType.LIBRARIAN
        user.save()

        Librarian.objects.create(user=user)
        return user

class ReaderCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=35)
    last_name = forms.CharField(max_length=35)
    address = forms.CharField(max_length=120)


    @atomic
    def save(self, commit: bool=True) -> Any:
        user = super().save(commit=False)
        user.user_type = UserType.READER
        user.save()

        Reader.objects.create(
            user=user,
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            address=self.cleaned_data.get("address")
        )
        return user

class UserChangeForm(DjangoUserChangeForm):

    class Meta:
        model = User
        fields = ("username",)

class UserAuthForm(DjangoUserAuthForm):
    ...