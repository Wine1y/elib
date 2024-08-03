from typing import List, Tuple, Optional

from django.db.models import QuerySet, Count
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, ReaderUser, LibrarianUser
from .forms import ReaderCreationForm, LibrarianCreationForm, UserChangeForm


class BookInline(admin.TabularInline):
    model = User.books.through
    extra = 0

class HaveBooksFilter(admin.SimpleListFilter):
    title = _("have books")
    parameter_name = "have_books"

    def lookups(self, request, model_admin, ) -> List[Tuple[str]]:
        return [
            ("yes", "Have books right now"),
            ("no", "Have no books right now")
        ]
    
    def queryset(self, request, queryset: QuerySet[ReaderUser]) -> Optional[QuerySet[ReaderUser]]:
        if self.value() == "yes":
            return queryset.annotate(books_count=Count("books")).filter(books_count__gt=0)
        if self.value() == "no":
            return queryset.annotate(books_count=Count("books")).filter(books_count__lt=1)

class ReaderUserAdmin(DjangoUserAdmin):
    add_form = ReaderCreationForm
    form = UserChangeForm
    model = ReaderUser
    list_display = ("username", "first_name", "last_name", "address", "id", "is_staff")
    list_filter = ("is_staff", HaveBooksFilter)
    readonly_fields = ["first_name", "last_name", "address"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Reader Info", {"fields": ("first_name", "last_name", "address")}),
        ("Permissions", {"fields": ("is_staff", "groups", "user_permissions")}),
    )
    inlines = (BookInline,)
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "first_name", "last_name", "address", "is_staff", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username", "id", "first_name", "last_name", "address")
    ordering = ("username", "id",)

    @admin.display(ordering="reader__first_name")
    def first_name(self, user):
        return user.reader.first_name
    
    @admin.display(ordering="reader__last_name")
    def last_name(self, user):
        return user.reader.last_name
    
    @admin.display(ordering="reader__address")
    def address(self, user):
        return user.reader.address
    

class LibrarianUserAdmin(DjangoUserAdmin):
    add_form = LibrarianCreationForm
    form = UserChangeForm
    model = LibrarianUser
    list_display = ("username", "id", "staff_number", "is_staff")
    list_filter = ("is_staff", )
    readonly_fields = ["staff_number"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Librarian Info", {"fields": ("staff_number",)}),
        ("Permissions", {"fields": ("is_staff", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username", "id")
    ordering = ("username", "id")

    @admin.display(ordering="librarian__staff_number")
    def staff_number(self, user):
        return user.librarian.staff_number

admin.site.register(ReaderUser, ReaderUserAdmin)
admin.site.register(LibrarianUser, LibrarianUserAdmin)
