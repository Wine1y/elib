from django.contrib.auth.management.commands.createsuperuser import Command as SuperUserCommand

from users.models import LibrarianUser


class Command(SuperUserCommand):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.UserModel = LibrarianUser