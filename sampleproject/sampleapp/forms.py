from django import forms

from sampleapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        labels={'roll':'Enter Roll','name':'Enter Name','city':'Enter City'}