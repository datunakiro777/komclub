from django import forms
from events.models import Events

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'description', 'rules', 'last_date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder' : 'შეჯიბრის სახელი..'}),
            'description' : forms.Textarea(attrs={'placeholder' : 'ინფორმაცია შეჯიბრის შესახებ..'}),
            'rules' : forms.Textarea(attrs={'placeholder' : 'დასაცავი წესები..'}),
            'last_date' : forms.DateInput(attrs={'type' : 'date', 'placeholder' : 'საბოლოო თარიღი გაწევრიანების.'})
        }