from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Book

class BookAdmin(SimpleHistoryAdmin):
    model = Book
    list_display = ("name", "id", "genre", "author")
    list_filter = ("genre",)
    fieldsets = (
        (None, {"fields": ("name", "author", "genre")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name", "author", "genre"
            )}
        ),
    )
    search_fields = ("name", "author")
    ordering = ("name", "author", "genre")

admin.site.register(Book, BookAdmin)