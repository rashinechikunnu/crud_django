from django import forms
from django.forms import ModelForm
from .models import actor

class actorForm(ModelForm):
     
     gender_choices=[
        ('Male','Male'),
        ('Female','Female'),
    ]
     gender = forms.ChoiceField(choices= gender_choices, widget = forms.RadioSelect , required=False)
     class Meta:
         model = actor
         fields = "__all__"

    
         
