from django.contrib import admin
from .models import Category, Series, Tutorial

from tinymce.widgets import TinyMCE 
from django.db import models


class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title/date', {'fields': ['title', 'published']}),
        ('URL', {'fields': ['slug']}),
        ('Series', {'fields': ['series']}),
        ('Content', {'fields': ['content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Series)
admin.site.register(Tutorial, TutorialAdmin)
