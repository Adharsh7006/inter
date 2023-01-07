from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from interview_app.forms import LoginForm, TeacherForm


def index(request):
    return render(request, 'index.html')


def teacher_register(request):
    login_form = LoginForm()
    teacher_form = TeacherForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        teacher_form = TeacherForm(request.POST, request.FILES)
        if login_form.is_valid() and teacher_form.is_valid():
            user = login_form.save(commit=False)
            user.is_teacher = True
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.info(request, 'Registration successful')
            return redirect('teacher_register')
    return render(request, 'teacher_register.html', {'login_form': login_form, 'teacher_form': teacher_form})
