from django import forms
from clubs.models import Clubs_info

class ClubsForm(forms.ModelForm):
    class Meta:
        model = Clubs_info
        fields = ['name', 'description']

class JoinClubForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        label='Club Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter club name'}),
    )
    