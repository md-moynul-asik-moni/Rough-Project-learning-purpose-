from django import forms
from django.core import validators

class teacherRegistration(forms.Form):

    name = forms.CharField(label='Enter your name', label_suffix=':')
    add = forms.CharField()
    email = forms.EmailField(initial='ashik@gmail.com', disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    address = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)


    def clean(self):
        cleaned_data = super().clean()
        rp = self.cleaned_data['password']
        wp = self.cleaned_data['repassword']

        if rp!=wp:
            raise forms.ValidationError('Password does not match')


