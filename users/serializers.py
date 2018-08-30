import datetime

from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.compat import authenticate

from .models import User


class AuthTokenSerializer(serializers.Serializer):
    """ auth token serializer
    """
    user = None

    email = serializers.CharField(label=_('Email'))
    password = serializers.CharField(label=_("Password"), trim_whitespace=False)

    def validate(self, data):
        email, password = data.values()

        if not email or not password:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        user = authenticate(request=self.context.get('request'),
                            email=email, password=password)
        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        self.user = user
        return data

    def get_token(self):
        """ get or generate a token that is valid for
            `settings.AUTH_TOKEN_EXPIRY_TIME`
        """
        if not self.user:
            msg = _('Unable to login with provided credentials.')
            raise serializers.ValidationError(msg, code="authorization")

        token, created = Token.objects.get_or_create(user=self.user)
        expiry_date = token.created + datetime.timedelta(days=settings.AUTH_TOKEN_EXPIRY_TIME)
        if not created and expiry_date < timezone.now():
            # delete token
            token.delete()
            # generate a new one
            token = Token.objects.create(user=self.user)

        return token


class AuthSerializer(serializers.ModelSerializer):
    """ auth user serializer
    """
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'confirm_password')

    def create(self, data):
        # pop the field which is not included in the model
        data.pop('confirm_password', None)

        instance = super(UserSerializer, self).create(data)
        instance.set_password(data['password'])
        instance.save()

        return data

    def validate_confirm_password(self, password2):
        password = self.initial_data.get('password')
        if password != password2:
            raise serializers.ValidationError(_('Password did not match.'))

        return password


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'handle',
            'image',
        )


class UserSerializer(serializers.ModelSerializer):
    """ user serializer
    """
    image = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    display_name = serializers.SerializerMethodField()
    subscribers = SubscriberSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'display_name',
            'title',
            'bio',
            'handle',
            'image',
            'cover',
            'subscribers',
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        return super(UserSerializer, self).__init__(*args, **kwargs)

    def update(self, instance, data):
        if not self.request.user or self.request.user != instance:
            raise serializers.ValidationError(_('You are not permitted to do this action.'))

        return super(UserSerializer, self).update(instance, data)

    def get_title(self, obj):
        return f"{obj.title}".title()

    def get_image(self, obj):
        if not obj.image: return None
        return f"{self.request.META['wsgi.url_scheme']}://{self.request.META['HTTP_HOST']}{obj.image.url}"

    def get_cover(self, obj):
        if not obj.cover: return None
        return f"{self.request.META['wsgi.url_scheme']}://{self.request.META['HTTP_HOST']}{obj.cover.url}"

    def get_display_name(self, obj):
        return obj.get_display_name


class PhotoSerializer(serializers.ModelSerializer):
    """ profile photo serializer
    """
    class Meta:
        model = User
        fields = ('id', 'image')


class CoverSerializer(serializers.ModelSerializer):
    """ profile photo serializer
    """
    class Meta:
        model = User
        fields = ('id', 'cover')


