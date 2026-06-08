from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# tasks = ["dinner", "grocery"]

# A class to represent the form
class NewTaskForm(forms.Form):
    # Define the form as inputing character
    task = forms.CharField(label="New Task")
    # Define the priority as integer
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    # A very often seeing pattern in django
    # Create a variable and implement logic in the web pages
    return render(request, "index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        # if the form is valid, we take the data from the form
        # get the task, add that into our list named tasks
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # adding a redirect link back to our orignal page
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # if the form is not valid, we can display any error that come out
            return render(request, "add.html", {
                "form": form
            })

    return render(request, "add.html", {
        "form": NewTaskForm()
    })