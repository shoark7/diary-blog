from django import forms
from .models import Category


class WriteForm(forms.Form):
    CATEGORIES = ((p.category, p.category) for p in Category.objects.all())

    categories = forms.ChoiceField(choices=CATEGORIES, widget=forms.Select)
    title = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)
