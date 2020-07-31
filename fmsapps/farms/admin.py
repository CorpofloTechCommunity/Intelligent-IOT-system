from django.contrib import admin

from .models import Farm

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'pressure',
        'temperature',
        'humidity',
        'speed'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }
    ordering = [
        'name',
        'speed'
    ]
