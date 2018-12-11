from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from django.utils import timezone

from utils.mixins import Q, DT
from .serializers import (
    BookSerializer,
    ChapterSerializer,
    PageSerializer,
    ReadSerializer
)


class Books(DT, Q, ViewSet):
    """ books endpoint
    """
    serializer_class = BookSerializer
    #permission_classes = (IsAuthenticated,)

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def list(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._filter(
                self._model,
                status=self._model.ACTIVE,
                **self.request.query_params.dict(),
            ),
            many=True)

        return Response(serializer.data, status=200)

    def featured(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._filter(
                self._model,
                is_featured=True,
                status=self._model.ACTIVE,
            ),
            many=True)

        return Response(serializer.data, status=200)

    def new_releases(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._filter(
                self._model,
                status=self._model.ACTIVE,
            ).order_by('-date_published'),
            many=True)

        return Response(serializer.data, status=200)


class Book(Q, ViewSet):
    """ book endpoint
    """
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        serializer = self.serializer_class(self._get(self._model, **kwargs))
        
        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data,
            instance=self._get(self._model, **kwargs))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)


class Chapters(Q, ViewSet):
    """ chapters endpoint
    """
    serializer_class = ChapterSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data,
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
    permission_classes = (IsAuthenticated,)

    def detail(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._get(
                self._model,
                id=kwargs.get('chapter_id')
            ))

        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data,
            instance=self._get(self._model, id=kwargs.get('chapter_id'))
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)


class Pages(Q, ViewSet):
    """ pages endpoint
    """
    serializer_class = PageSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def list(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._filter(
                self._model,
                chapter__id=kwargs['chapter_id'],
                **self.request.query_params
            ),
            many=True)

        return Response(serializer.data, status=200)


class Page(Q, ViewSet):
    """ page endpoint
    """
    serializer_class = PageSerializer
    permission_classes = (IsAuthenticated,)

    def detail(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._get(self._model, id=kwargs.get('page_id'))
        )

        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data,
            instance=self._get(self._model, id=kwargs.get('page_id'))
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)


class Reads(Q, ViewSet):
    """ user reading logs
    """
    serializer_class = ReadSerializer
    permission_classes = (IsAuthenticated,)

    def reads(self, *args, **kwargs):
        serializer = self.serializer_class(
            self._filter(
                self._model,
                user=self.request.user,
                book__status='active',
                **self.request.query_params
            ),
            many=True)

        return Response(serializer.data, status=200)

