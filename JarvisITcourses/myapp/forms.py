from django import forms
from django.contrib.auth.models import User 
from myapp.models import Student
class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='__all__'