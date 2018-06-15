from django.shortcuts import get_object_or_404


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







