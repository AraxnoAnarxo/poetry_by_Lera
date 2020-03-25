from django import forms
from .models import Poem

class PoemForm(forms.ModelForm):
    # poem_title = forms.CharField(label="Название стихотворения")
    # poem_text = forms.CharField(label="Teкст стихотворения")

    class Meta:
        model = Poem
        fields = '__all__'