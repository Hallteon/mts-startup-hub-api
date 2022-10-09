from django import forms

from events.models import Event, Platform


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        platform = forms.ModelChoiceField(queryset=Platform.objects.all(), to_field_name='platform')
        fields = ('name', 'platform', 'description', 'goals', 'equipment', 'date')
        widgets = {'name': forms.TextInput(),
                   'platform': forms.TextInput(),
                   'description': forms.TextInput(),
                   'goals': forms.TextInput(),
                   'equipment': forms.TextInput(),
                   'date': forms.TextInput()}
