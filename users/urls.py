from django.urls import path, re_path
from .views import Login, Signup, User


urlpatterns = [
    path('<int:id>/', User.as_view({
        'post': 'update',
        'get': 'detail',
    }), name="user"),
    path('<int:id>/image/', User.as_view({
        'post': 'upload_avatar',
    }), name="user_image"),

    path('auth/login/', Login.as_view(), name="auth_login"),
    path('auth/create/', Signup.as_view({
        'post': 'create',
    }), name="auth_signup"),
]