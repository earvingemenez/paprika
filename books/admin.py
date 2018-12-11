from django.contrib import admin
from .models import Book, Chapter, Page, Category, Tag, Read


class BookAdmin(admin.ModelAdmin):

    def tagged(self, obj):
        return ", ".join(obj.tags.all().values_list('name', flat=True))

    model = Book
    list_display = (
        'title',
        'author',
        'code',
        'price',
        'category',
        'tagged',
        'date_created',
        'date_updated',
        'status',
    )
    readonly_fields = ('code',)
    filter_horizontal = ('tags',)


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


class TagAdmin(admin.ModelAdmin):
    model = Tag


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class ReadAdmin(admin.ModelAdmin):
    model = Read
    list_display = (
        'book',
        'page',
        'user',
        'date_updated',
        'date_created'
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.register(Read, ReadAdmin)
