from django import forms

from events.models import Event


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'platform', 'description', 'goals', 'equipment', 'date', 'time', 'add_information')
        widgets = {'name': forms.TextInput(),
                   'platform': forms.TextInput(),
                   'description': forms.TextInput(),
                   'goals': forms.TextInput(),
                   'equipment': forms.TextInput(),
                   'date': forms.TextInput(),
                   'time': forms.TextInput(),
                   'add_information': forms.TextInput()}
