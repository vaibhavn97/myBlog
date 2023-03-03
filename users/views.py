from django.shortcuts import render, redirect
from .forms import UserRegisterationForm, UserUpdationForm
from django.contrib import messages
from .models import Profile

# Create your views here.
def register(request):
    form = UserRegisterationForm()
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request, 'Invalid Crendentials')

    return render(request, 'users/register.html', {'form':form})

def profile_view(request, pk):
    form = UserUpdationForm(instance=request.user.profile)
    profile = Profile.objects.filter(user=pk)[0]
    if request.method == 'POST' and profile.user==request.user:
        form = UserUpdationForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()

    return render(request, 'users/profile.html', {'prof':profile, 'form':form})