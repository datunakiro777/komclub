from django import forms
from clubs.models import Clubs_info, Comments

class ClubsForm(forms.ModelForm):
    class Meta:
        model = Clubs_info
        fields = ['name', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'comment-input',
                'placeholder': 'აქ შეგიძლია დაწერო კომენტარი...',
                'rows': 3,
            }),
        }
    