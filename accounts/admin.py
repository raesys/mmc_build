from django.contrib import admin
from .models import Profile, Project, Chat


# admin.site.site_header = ""
# admin.site.site_title = ""
# admin.site.index_title = ""


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'phone', 'email', 'interest']

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    # full_name.short_description = 'Name in Full'


class ChatAdmin(admin.ModelAdmin):
    list_display = ['subject', 'message', 'author']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project)
admin.site.register(Chat, ChatAdmin)