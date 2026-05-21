from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'date')
    search_fields = ('title', 'type')
    list_filter = ('type',)