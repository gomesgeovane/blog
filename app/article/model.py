from django.db import models
from app.profile.model import Profile
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.text import slugify
from django.utils.timezone import now

class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLIC = 'PB', 'Public'

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='articles')
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, default=Status.DRAFT, choices=Status.choices)
    published_at = models.DateTimeField(blank=True, null=True)
    views = models.ManyToManyField(Profile, related_name='views_articles', blank=True)
    likes = models.ManyToManyField(Profile, related_name='likes_articles', blank=True)

    @property
    def content_html(self):
        return markdownify(self.content)

    @property
    def count_views(self):
        return self.views.count()

    @property
    def count_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)

        if self.status == self.Status.PUBLIC and not self.published_at:
            self.published_at = now()
        elif self.status == self.Status.DRAFT:
            self.published_at = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name