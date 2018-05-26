from django import forms

class WineDescForm(forms.Form):
    desc = forms.CharField(max_length=500, widget=forms.Textarea)