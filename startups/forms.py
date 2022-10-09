from django import forms
from startups.models import Program, Stage, Startup


class AddStartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        application_program = forms.ModelChoiceField(queryset=Program.objects.all(), to_field_name='program')
        stage = forms.ModelChoiceField(queryset=Stage.objects.all())
        fields = ('name', 'program', 'website', 'presentation', 'stage', 'description')
        widgets = {'name': forms.TextInput(),
                   'website': forms.TextInput(),
                   'presentation': forms.TextInput(),
                   'description': forms.TextInput()}


class AddProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name',)
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Введите название программы'})}


class AddStageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ('name',)
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Введите стадию разработки'})}