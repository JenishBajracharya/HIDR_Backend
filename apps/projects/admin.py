from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'featured')
    search_fields = ('title', 'category')
    list_filter = ('category', 'featured')