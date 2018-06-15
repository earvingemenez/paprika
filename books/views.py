from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from utils.mixins import Q
from .serializers import BookSerializer, ChapterSerializer, PageSerializer


class Books(Q, ViewSet):
    """ books endpoint
    """
    serializer_class = BookSerializer

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def list(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._filter(self._model, **self.request.query_params), many=True)

        return Response(serializer.data, status=200)


class Book(Q, ViewSet):
    """ book endpoint
    """
    serializer_class = BookSerializer

    def detail(self, *args, **kwargs):
        serializer = self.serializer_class(self._get(self._model, **kwargs))
        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data,
                                           instance=self._get(self._model, **kwargs))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)


class Chapters(Q, ViewSet):
    """ chapters endpoint
    """
    serializer_class = ChapterSerializer

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data,
                                           book_id=kwargs.get('id'))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def list(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._filter(self._model, **self.request.query_params), many=True)

        return Response(serializer.data, status=200)


class Chapter(Q, ViewSet):
    """ chapter endpoint
    """
    serializer_class = ChapterSerializer

    def detail(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._get(self._model, id=kwargs.get('chapter_id')))

        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data,
                        instance=self._get(self._model, id=kwargs.get('chapter_id')))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)


class Pages(Q, ViewSet):
    """ pages endpoint
    """
    serializer_class = PageSerializer

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def list(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._filter(self._model, **self.request.query_params), many=True)

        return Response(serializer.data, status=200)


class Page(Q, ViewSet):
    """ page endpoint
    """
    serializer_class = PageSerializer

    def detail(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._get(self._model, id=kwargs.get('page_id')))

        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data,
                        instance=self._get(self._model, id=kwargs.get('page_id')))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)