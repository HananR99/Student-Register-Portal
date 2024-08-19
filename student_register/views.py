from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm, StudentForm
from .models import Student

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None and user.is_superuser:
                auth_login(request, user)
                return redirect('student_list')  # Redirect to the student list page or another page after login
    else:
        form = CustomLoginForm()
    return render(request, 'student_register/login.html', {'form': form})

@login_required(login_url='/login/')  # Redirect to login if not authenticated
def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "student_register/student_list.html", context)

@login_required(login_url='/login/')
def student_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "student_register/student_form.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')

@login_required(login_url='/login/')
def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')

def logout_view(request):
    auth_logout(request)
    return redirect('/login')
