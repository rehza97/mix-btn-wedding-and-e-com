from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class ResisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','password1','password2','first_name','last_name','age','phone','gender','address']