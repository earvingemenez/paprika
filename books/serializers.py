from rest_framework import serializers

from utils.mixins import Q
from .models import Book, Chapter, Page


class BookSerializer(serializers.ModelSerializer):
    """ book serializer
    """
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'short_description', 'summary', 'status')


class ChapterSerializer(Q, serializers.ModelSerializer):
    """ chapter serializer
    """
    class Meta:
        model = Chapter
        fields = ('id', 'book', 'title', 'description', 'position', 'status')


class PageSerializer(serializers.ModelSerializer):
    """ page serializer
    """
    class Meta:
        model = Page
        fields = ('id', 'content', 'chapter', 'page_number')