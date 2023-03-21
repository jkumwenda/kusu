from django import forms

class SearchForm(forms.Form):
    search_value = forms.CharField(required=False,label='', widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Your Name or Email ...'
        }
    ))

class RegisterForm(forms.Form):
    fullname = forms.CharField(required=False,label='Fullname', widget=forms.TextInput(
        attrs={
        'class':'form-control',
        }
    )) 
    email = forms.CharField(required=False,label='KUHeS Valid Email', widget=forms.TextInput(
        attrs={
        'class':'form-control',
        }
    ))    