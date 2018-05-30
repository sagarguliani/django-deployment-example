from django import forms
from django.contrib.auth.models import User
from basic_app.models import User_Profile_Info

class User_Form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class User_Profile_Info_Form(forms.ModelForm):
    class Meta():
        model = User_Profile_Info
        fields = ('portfolio_site','profile_pic')
