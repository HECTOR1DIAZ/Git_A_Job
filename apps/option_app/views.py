from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def sign_in_page(request):
    return render(request,'sign_in.html')

def dashboard(request):
    user=User.objects.get(id=request.session['user_id'])
    all_jobs=Job.objects.all()
    context = {
        
        'user' : user,
        'all_jobs': all_jobs
                }
    
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        return render(request,'dashboard.html', context)

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        User.objects.create(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            email=request.POST['email'],
            password=request.POST['password'])
        last_user = User.objects.last()
        request.session['user_id'] = last_user.id
        request.session['user_name'] = last_user.first_name
        messages.success(request, 'Registration Complete')
        return redirect('/dashboard')
    
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        userlogin = User.objects.get(email=request.POST['loginEmail'])
        request.session['user_id'] = userlogin.id
        request.session['user_name'] = userlogin.first_name
        messages.success(request, 'Logged in!')
        return redirect('/dashboard')
    
def create(request):
    errors = User.objects.job_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create_page')
    else:
        user = User.objects.get(id=request.session['user_id'])
        Job.objects.create(title=request.POST['title'],desc=request.POST['desc'],location=request.POST['location'],worker=user)
        last_job = Job.objects.last()
        request.session['job_id'] = last_job.id
    
        return redirect('/dashboard')

        
def create_page(request):
    user=User.objects.get(id=request.session['user_id'])
    context = {
        "user":user
        
    }
    
    return render(request,'create.html', context)
        
def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request,id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/dashboard')

def view_job(request,id):
    job = Job.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    context = {
        "job" : job,
        "user" : user   
        
        
    }
    return render(request, 'view.html',context)

def edit(request,id):
    job = Job.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    context = {
        "job" : job,
        "user" : user
        
        
    }
    return render(request, 'edit.html',context)


def edit_job(request,id):
    errors = User.objects.job_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create_page')
    else:
        job = Job.objects.get(id=id)
        job.title=request.POST['title']
        job.desc=request.POST['desc']
        job.location=request.POST['location']
        job.save()
        return redirect('/dashboard')
