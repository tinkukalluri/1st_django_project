from django.conf.urls import url
from django.forms.forms import Form
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.
class newtaskform(forms.Form):
        task=forms.CharField(label="new task")
        priority=forms.IntegerField(label="priority",min_value=1,max_value=5)

error="error"
tasks3=["tinku","sindhu","sintin"]
tasks=[]


def index(request):
        if "tasks" not in request.session:
                request.session["tasks"]=[]
        return render(request,'tasks/index.html', {
        "tasks": request.session["tasks"]
        })
def add(request):   

        if request.method=="POST":
                form = newtaskform(request.POST)
                if form.is_valid():
                        task1=form.cleaned_data["task"]
                        task2=form.cleaned_data["priority"]
                        tasks.append(task1)
                        tasks.append(task2)
                        tasks.append(form.cleaned_data)
                        request.session["tasks"]+=tasks
                        return HttpResponseRedirect(reverse("tasks:task_index"))
                        
                else:
                        return render(request,"tasks/add.html",{
                                "form":form
                        })
        return render(request,'tasks/add.html',{
                "form":newtaskform()
                 })


