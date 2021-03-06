from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from utils.mixins import Q
from .serializers import (
    AuthTokenSerializer,
    AuthSerializer,
    UserSerializer,
    PhotoSerializer,
    CoverSerializer,
)


class Login(APIView):
    """ token authentication
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    render_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, *args, **kwargs):
        """ accepts post data that serves as user credentials and
            validates it. Returns a generated token if the
            credentials are valid.
        """
        serializer = self.serializer_class(
            data=self.request.data,
            context={'request': self.request}
        )
        
        serializer.is_valid(raise_exception=True)
        return Response({
            'token'   : serializer.get_token().key,
            'user_id' : serializer.user.id,
        })


class Signup(ViewSet):
    """ user registration
    """
    serializer_class = AuthSerializer

    def create(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)


class User(Q, ViewSet):
    """ user endpoint
    """
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        serializer = self.serializer_class(
            instance=self._get(self._model, handle=kwargs.get('handle')),
            request=self.request)
        return Response(serializer.data, status=200)

    def update(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data,
                                           instance=self._get(self._model, id=kwargs.get('id')),
                                           request=self.request)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)

    def auth(self, *args, **kwargs):
        return Response(self.serializer_class(
            instance=self.request.user,
            request=self.request).data, status=200)

    def upload_avatar(self, *args, **kwargs):
        serializer = PhotoSerializer(data=self.request.data,
                                     instance=self._get(self._model, id=kwargs.get('id')))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(self.serializer_class(
            serializer.instance, request=self.request).data, status=200)

    def upload_cover(self, *args, **kwargs):
        serializer = CoverSerializer(data=self.request.data,
                                     instance=self._get(self._model, id=kwargs.get('id')))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(self.serializer_class(
            serializer.instance, request=self.request).data, status=200)





