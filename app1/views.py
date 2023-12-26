from django.shortcuts import render, redirect, HttpResponse
from app1.forms import EmployeeForm
from django.contrib.auth.models import User
from app1.models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def Home(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        form=EmployeeForm()
    
    data=Employee.objects.all()

    context={
        'form':form,
        'data':data,
    }
    return render(request,'app1/index.html',context)

def deleteview(request, id):
    var = Employee.objects.get(id = id)
    var.delete()
    return redirect('/')

def updateview(request, id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'app1/update.html',context)


def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("wrong password")
        else:        
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            # return HttpResponse('Hello')
            return redirect('login')
    return render(request, 'registration/signup.html')
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(username = username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('wrong')
    return render(request, 'registration/login.html')

def LogoutPage(request):
    return redirect('login')