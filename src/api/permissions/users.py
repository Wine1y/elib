from rest_framework import permissions
from rest_framework.request import Request

from users.models import UserType


class IsReader(permissions.BasePermission):
    def has_permission(self, request: Request, _view):
        return request.user.user_type == UserType.READER

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request: Request, _view):
        return request.user.user_type == UserType.LIBRARIAN