from django.conf import settings
from django.contrib.postgres.fields import JSONField

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.mixins import W


class Book(W, models.Model):
    """ book model
    """
    DRAFT = 'draft'
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    STATUSES = (
        (DRAFT, 'Draft'),
        (ACTIVE, 'Active'),
        (INACTIVE, 'In-Active'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, unique=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=10, choices=STATUSES, default=DRAFT)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.id and not self.title:
            # generate a title based on the author's
            # existing list of books
            self.title = self.generate_title(
                self._meta.model, author=self.author)

        return super(Book, self).save(*args, **kwargs)


class Chapter(W, models.Model):
    """ chapter model
    """
    DRAFT = 'draft'
    ACTIVE = 'active'
    STATUSES = (
        (DRAFT, 'Draft'),
        (ACTIVE, 'Active'),
    )

    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(null=True, blank=True)
    position = models.IntegerField(default=0)

    status = models.CharField(max_length=10, choices=STATUSES, default=DRAFT)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.book}) Chapter {self.position}: {self.title}"

    def save(self, *args, **kwargs):
        if not self.id and not self.title:
            # generate a title based on the book's
            # existing chapters
            self.title = self.generate_title(
                self._meta.model, book=self.book)

        return super(Chapter, self).save(*args, **kwargs)


class Page(models.Model):
    """ page model
    """
    chapter = models.ForeignKey('Chapter', on_delete=models.SET_NULL, null=True)
    content = JSONField(default={}, null=True, blank=True)

    page_number = models.IntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.chapter}: page. {self.page_number}"



# SIGNALS

@receiver(post_save, sender=Book)
def auto_create_chapter_page(sender, instance=None, created=False, **kwargs):
    if created:
        # Create a new blank chapter
        chapter = Chapter.objects.create(book=instance)

        # Create a new blank page that is connected/part
        # of the blank chapter
        Page.objects.create(chapter=chapter)