from rest_framework import serializers

from utils.mixins import Q
from .models import Book, Chapter, Page, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    """ category serializer
    """
    class Meta:
        model = Category
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):
    """ category serializer
    """
    class Meta:
        model = Tag
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    """ book serializer
    """
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'code',
            'author',
            'title',
            'short_description',
            'cover',
            'summary',
            'status',
            'tags',
            'category',
            'price',
        )


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