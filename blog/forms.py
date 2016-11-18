from django import forms
from .models import Postear

class PostearForm(forms.ModelForm):
    class Meta:
        model = Postear
        fields = ('titulo','ISBN','Portada','Editorial','pais','years')
