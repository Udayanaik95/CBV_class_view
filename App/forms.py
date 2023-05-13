from django import forms
from App.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'