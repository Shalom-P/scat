from django import forms
from django.forms import ModelForm, fields
from .models import Newcat,Newslearnwion

class Newcatform(ModelForm):
    class Meta:
        model = Newcat
        fields = ('sentence','label')


