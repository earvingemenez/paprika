import timeago
import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone

from users.models import User


class Q(object):
    """ helper class used for queries
    """
    def __init__(self, *args, **kwargs):
        return super(Q, self).__init__(*args, **kwargs)

    @property
    def _model(self):
        try:
            return self.serializer_class.Meta.model
        except Exception as e:
            return None

    def _get(self, _model, **kwargs):
        """ get an object based on the keyword arguments
            returns 404 if not found.
        """
        return get_object_or_404(_model, **kwargs)

    def _filter(self, _model, **kwargs):
        """ get the list of objects based on the keyword arguments
        """
        return _model.objects.filter(**kwargs)


class W(Q):
    """ helper class used for writing books
    """
    def __init__(self, *args, **kwargs):
        return super(Q, self).__init__(*args, **kwargs)

    def generate_code(self):
        """ generate a random unique 8 length character
            which will serve as the book's identifier
        """
        return User.objects.make_random_password(length=8)

    def generate_title(self, _model, _format="UNTITLED-", **kwargs):
        """ generate an untitled name with the index
            as the unique character.
        """
        q = self._filter(_model, title__icontains=_format, **kwargs) \
                .values_list('title', flat=True)
        titles = set(f"{_format}{i}" for i in range(q.count())) - set(q)

        # check if there are existing titles. If not just create a
        # title with the latest number suffix + 1
        if not titles:
            return f"{_format}{q.count()}"

        return f"{next(iter(titles))}"

    def autoindex(self, _model, **kwargs):
        """ generate auto index.
        """
        return self._filter(_model, **kwargs).count() + 1


class DT(object):
    """ helper class used for managing time and dates
    """
    def __init__(self, *args, **kwargs):
        return super(DT, self).__init__(*args, **kwargs)

    def time_ago(self, dt):
        """ get the time interval of the specified datetime
            and the current datetime. It also automatically
            formats it to minutes, hrs, days, years.
        """
        return timeago.format(dt, timezone.now())

    def days_ago(self, dt, days=1):
        """ get the past datetime based on the number of
            days specified.
        """
        return dt - datetime.timedelta(days=days)










