from .models import User

class AuthUser(object):
    """ mixin class for authenticated user
    """
    def __init__(self, *args, **kwargs):
        return super(AuthUser, self).__init__(*args, **kwargs)

    def is_signedin(self, _id):
        """ check if the user 
        """
        return self.request.user.id = _id