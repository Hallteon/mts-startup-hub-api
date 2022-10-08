from django.contrib import admin

from startups.forms import AddProgramForm, AddStageForm, AddStartupForm
from startups.models import ApplicationProgram, Stage, Startup


class StartupAdmin(admin.ModelAdmin):
    form = AddStartupForm
    list_display = ('id', 'name', 'website', 'stage', 'application_program')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class ProgramAdmin(admin.ModelAdmin):
    form = AddProgramForm
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class StageAdmin(admin.ModelAdmin):
    form = AddStageForm
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Startup, StartupAdmin)
admin.site.register(ApplicationProgram, ProgramAdmin)
admin.site.register(Stage, StageAdmin)
