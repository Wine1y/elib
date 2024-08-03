from django.db import models
from rest_framework.serializers import ModelSerializer
from simple_history.models import HistoricalRecords


class Book(models.Model):
    name = models.TextField(max_length=250)
    author = models.TextField(max_length=150)
    genre = models.TextField(max_length=80)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f"{self.name} by {self.author}"


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "author", "genre"]