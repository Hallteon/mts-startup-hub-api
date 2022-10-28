from django.contrib import admin
from events.forms import AddEventForm
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    form = AddEventForm
    list_display = ('id', 'name', 'platform', 'description', 'theme', 'date', 'time')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Event, EventAdmin)
