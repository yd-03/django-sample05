from django import forms
from .models import UploadImage


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ["image"]


class SettingForm(forms.Form):
    angle = forms.IntegerField()
    gray = forms.BooleanField(required=False)
