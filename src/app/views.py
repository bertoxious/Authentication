from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from app.forms import BasicDetailsForm, EducationForm
from app.models import BasicDetails, Education
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.


def Register(request):
    form = UserCreationForm
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save(commit=True)
            messages.success(request, 'Account created successfully for {}'.format(username))
            return redirect('login')
    return render(request, 'app/register.html',{'form':form})

@login_required
def View(request):
    education = EducationForm
    # education.users_id = request.user.id

    if request.method =="POST":
        # ef = EducationForm(request.POST,instance=User.objects.get(pk=request.user.id))
        ef = EducationForm(request.POST)
        ef.instance.username = request.user.username
        ef.instance.users_id = request.user.id
        if ef.is_valid():
            ef.save()
            messages.success(request,"Credentials Saved successfully!")
            return render(request,'app/view.html',{'education':ef})
        else:
            messages.info(request,"Error Occurred.")
            education = EducationForm()
    return render(request, 'app/view.html',{'education':education})

@login_required
def Delete(request,id):
    person = User.objects.get(pk=id)
    person.delete()
    messages.warning(request,"Account Deleted.")
    return redirect('login')

def Detail(request,id):
    
    if request.method == "POST":
        person = User.objects.get(pk=id)
        fm = EducationForm(request.POST,instance=person)
        if fm.is_valid():
            fm.save()
        else:
            person = User.objects.get(pk=id)
            fm = EducationForm(instance=person)
        return render(request,'app/detail.html',{'education':fm})