from django.contrib import admin

from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'firstname', 'lastname')
    list_display_links = ('id', 'email')
    search_fields = ('id', 'email', 'firstname', 'lastname')


admin.site.register(CustomUser, CustomUserAdmin)