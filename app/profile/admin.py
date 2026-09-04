from django.contrib import admin
from .model import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user__email', 'count_following', 'count_followers')
    list_filter = ('user__is_active', 'user__is_staff', 'user__is_superuser')
    search_fields = ('full_name', 'user__email')
    ordering = ('full_name',)
    filter_horizontal = ('following',)
    readonly_fields = ('count_following', 'count_followers')

    fieldsets = (
        ('Informations', {
            'fields': ('user', 'full_name', 'bio', 'image', 'following'),
        }),
        ('Connections', {
            'classes': ('collapse',),
            'fields': ('count_following', 'count_followers')
        })
    )

    add_fieldsets = (
        ('Add', {
            'fields': ('user', 'full_name', 'bio', 'image', 'following'),
        }),
    )