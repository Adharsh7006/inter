from django.contrib.auth.forms import UserCreationForm
from django import forms


from interview_app.models import Login


class LoginForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'email', 'contact', 'image')
