from django.contrib import admin

from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'created_at',
        'url',
        'response_code',
    )
