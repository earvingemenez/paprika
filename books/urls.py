from django.urls import path, re_path
from .views import Books, Book, Chapters, Chapter, Pages, Page

BOOKS = ''
BOOK = f'{BOOKS}<str:code>/'
CHAPTERS = f'{BOOK}chapters/'
CHAPTER = f'{CHAPTERS}<int:chapter_id>/'
PAGES = f'{CHAPTER}pages/'
PAGE = f'{PAGES}<int:page_id>/'


urlpatterns = [
    path(f'{BOOKS}', Books.as_view({
        'post': 'create',
        'get': 'list',
    }), name="books"),
    path(f'{BOOK}', Book.as_view({
        'get': 'get',
    }), name="book"),

    path(f'{CHAPTERS}', Chapters.as_view({
        'post': 'create',
        'get': 'list',
    }), name="chapters"),
    path(f'{CHAPTER}', Chapter.as_view({
        'get': 'detail',
        'post': 'update',
    }), name="chapter"),

    path(f'{PAGES}', Pages.as_view({
        'post': 'create',
        'get': 'list',
    }), name="pages"),
    path(f'{PAGE}', Page.as_view({
        'get': 'detail',
        'post': 'updated',
    }), name="pages"),
]