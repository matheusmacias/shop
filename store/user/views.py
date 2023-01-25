from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login
from django.contrib import messages


def Userlogin(request):
    context = {

    }
    return render(request, 'user/login.html', context)


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home_page")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")

    form = UserForm()

    context = {
        "form": form
    }
    return render(request, 'user/register.html', context)
