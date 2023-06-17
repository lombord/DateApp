from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import Profile
from .forms import ProfileForm


def profilesPage(request: HttpRequest):
    context = {'profiles': Profile.objects.all()}
    return render(request, 'base_app/home.html', context)


def profilePage(request: HttpRequest, pk: str):
    context = {'profile': Profile.objects.get(pk=pk)}
    return render(request, 'base_app/profile.html', context)


def registerPage(request: HttpRequest):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base_app/register.html', context)
