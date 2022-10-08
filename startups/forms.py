from django import forms
from startups.models import ApplicationProgram, Stage, Startup


class AddStartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        application_program = forms.ModelChoiceField(queryset=ApplicationProgram.objects.all(), to_field_name='application_program')
        stage = forms.ModelChoiceField(queryset=Stage.objects.all())
        fields = ('name', 'application_program', 'website', 'stage', 'description')
        widgets = {'name': forms.TextInput(),
                   'website': forms.TextInput(),
                   'description': forms.TextInput()}


class AddProgramForm(forms.ModelForm):
    class Meta:
        model = ApplicationProgram
        fields = ('name',)
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Введите название программы'})}


class AddStageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ('name',)
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Введите стадию разработки'})}