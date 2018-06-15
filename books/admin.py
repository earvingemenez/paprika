from django.contrib import admin
from .models import Book, Chapter, Page


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display =  (
        'title',
        'author',
        'date_created',
        'date_updated',
        'status',
    )


class ChapterAdmin(admin.ModelAdmin):
    model = Chapter
    list_display = (
        '__str__',
        'position',
        'date_created',
        'date_updated',
        'status',
    )


class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = (
        'chapter',
        'page_number',
        'date_created',
        'date_updated',
    )



admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Page, PageAdmin)