from django import forms

class BookForm(forms.ModelForm):
    name = forms.CharField(max_length=20,required=True,label='NAME')
    check = forms.BooleanField(required=False,label='Present')


