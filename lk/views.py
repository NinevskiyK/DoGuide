from django.shortcuts import render
from search.models import Excursion
from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm
from .forms import ProfileForm

def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            p = profile_form.save(commit=False)
            p.user = user
            p.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
