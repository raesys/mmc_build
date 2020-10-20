from django.contrib import admin
from .models import Category, Guide

from tinymce.widgets import TinyMCE 
from django.db import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class GuideAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title/date', {'fields': ['title', 'published_date']}),
        ('URL', {'fields': ['slug']}),
        ('Category', {'fields': ['category']}),
        ('Content', {'fields': ['content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Guide, GuideAdmin)
