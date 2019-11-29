from django.contrib import admin

from .models import CBDPost


@admin.register(CBDPost)
class CBDPostAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'published_at',
    )
    ordering = (
        '-published_at',
    )
