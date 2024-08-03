from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import login
from django.http import HttpResponse

from .models import User
from .forms import LibrarianCreationForm, ReaderCreationForm, UserAuthForm


class LibrarianCreateView(CreateView):
    model = User
    form_class = LibrarianCreationForm
    template_name = "librarian_signup.html"

    def form_valid(self, form: LibrarianCreationForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect("index")

class ReaderCreateView(CreateView):
    model = User
    form_class = ReaderCreationForm
    template_name = "reader_signup.html"

    def form_valid(self, form: ReaderCreationForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect("index")

class UserLoginView(LoginView):
    template_name = "signin.html"
    next_page="/"
    authentication_form=UserAuthForm

class UserLogoutView(LogoutView):
    next_page="/"