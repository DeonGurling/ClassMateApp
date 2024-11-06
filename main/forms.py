from django import forms

from django.contrib.auth.models import User
from main.models import Educators
from main.models import Students
from main.models import Assignments

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class EducatorForm(forms.ModelForm):
    class Meta:
        model = Educators
        fields = ('name', 'surname', 'phone', 'address', 'profile_pic')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('name', 'surname', 'phone', 'address', 'profile_pic')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ('title', 'advisor', 'pdf')

