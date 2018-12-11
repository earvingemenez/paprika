from django.urls import path, re_path
from .views import Login, Signup, User


urlpatterns = [
    path('auth/', User.as_view({
        'get': 'auth',
    }), name="user_auth"),

    path('auth/create/', Signup.as_view({
        'post': 'create',
    }), name="auth_signup"),

    path('auth/login/', Login.as_view(), name="auth_login"),

    path('<str:handle>/', User.as_view({
        'post': 'update',
        'get': 'get',
    }), name="user"),

    path('<str:handle>/image/', User.as_view({
        'post': 'upload_avatar',
    }), name="user_image"),

    path('<str:handle>/cover/', User.as_view({
        'post': 'upload_cover',
    }), name="user_cover"),
]