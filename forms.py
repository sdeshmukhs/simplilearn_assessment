from django import forms
from .models import Userinfo

class UserinfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = "__all__"