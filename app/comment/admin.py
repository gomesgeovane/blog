from django.contrib import admin
from .model import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author__full_name', 'article__name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('=id', 'author__full_name', 'article__name')
    ordering = ('id',)
    readonly_fields = ('id', 'created_at',)

    fieldsets = (
        ('Informations', {
            'fields': ('author', 'article', 'content', 'created_at'),
        }),
    )

    add_fieldsets = (
        ('Add', {
            'fields': ('author', 'article', 'content', 'created_at'),
        }),
    )