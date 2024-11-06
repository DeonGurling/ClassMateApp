from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from main.forms import UserForm, EducatorForm, StudentForm, AssignmentForm
from django.core.files.storage import FileSystemStorage
from .models import Assignments


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

@staff_member_required
def admin_home(request):
    return render(request, 'main/admin_dash.html', {})

@login_required(login_url='/educator/sign-in/')
def educator_home(request):
    return render(request, 'educator/home.html', {})

@login_required(login_url='/student/sign-in/')
def student_home(request):
    return render(request, 'student/home.html', {})



def educator_sign_up(request):
    user_form = UserForm()
    educator_form = EducatorForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        educator_form = EducatorForm(request.POST, request.FILES)

        if user_form.is_valid() and educator_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_educator = educator_form.save(commit=False)
            new_educator.user = new_user
            new_user.is_active = False
            new_educator.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password'],
            ))

            return redirect(educator_home)

    return render(request,'educator/sign_up.html', {
    'user_form': user_form,
    'educator_form': educator_form
    })

def ed_upload(request):
    if request.method =='POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request, 'educator/upload.html')

def assignment_list(request):
    assignments = Assignments.objects.all()
    return render(request, 'educator/assignment_list.html', {
        'assignments':assignments
    })

def upload_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'educator/upload_assignment.html', {
        'form': form
    })

def delete_assignment(request, pk):
    if request.method == 'POST':
        assignment = Assignments.objects.get(pk=pk)
        assignment.delete()
    return redirect(assignment_list)


def student_sign_up(request):
    user_form = UserForm()
    student_form = StudentForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST, request.FILES)

        if user_form.is_valid() and student_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_student = student_form.save(commit=False)
            new_student.user = new_user
            new_user.is_active = False
            new_student.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password'],
            ))

            return redirect(student_home)

    return render(request,'student/sign_up.html', {
    'user_form': user_form,
    'student_form': student_form
    })
