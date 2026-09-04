from django.contrib import admin
from .model import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'author__full_name', 'count_views', 'count_likes', 'published_at', 'created_at')
    list_filter = ('status', 'published_at', 'created_at')
    search_fields = ('name', 'author__full_name')
    ordering = ('name',)
    filter_horizontal = ('views', 'likes')
    readonly_fields = ('created_at', 'published_at', 'count_views', 'count_likes')
    prepopulated_fields = {'slug': ('name',),}

    fieldsets = (
        ('Informations', {
            'fields': ('author', 'name', 'slug', 'content', 'status', 'published_at', 'created_at', 'views', 'likes', 'count_views', 'count_likes'),
        }),
    )

    add_fieldsets = (
        ('Add', {
            'fields': ('author', 'name', 'slug', 'content', 'status', 'published_at', 'created_at', 'views', 'likes'),
        }),
    )