from django import forms
from clubs.models import Clubs_info

class ClubsForm(forms.ModelForm):
    class Meta:
        model = Clubs_info
        fields = ['name', 'description']
    