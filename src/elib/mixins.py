from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin as DjangoLoginRequiredMixin

from users.models import UserType


class LoginRequiredMixin(DjangoLoginRequiredMixin):
    login_url = "/accounts/signin"

class IsReaderMixin(UserPassesTestMixin):
    def test_func(self) -> bool:
        return self.request.user.user_type == UserType.READER

class IsLibrarianMixin(UserPassesTestMixin):
    def test_func(self) -> bool:
        return self.request.user.user_type == UserType.LIBRARIAN