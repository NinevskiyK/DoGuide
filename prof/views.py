from django.shortcuts import render
from django.shortcuts import get_object_or_404
from lk.models import Profile
from django.contrib.auth.models import User
from .forms import ExcursionForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def My_profile(request):
    profile_copy = request.user.profile
    context = {'profile': profile_copy, 'yours': True}
    return render(request, 'Profile_detail.html', context)

@login_required
def Profile_detail(request, pk):
    profile_copy = (get_object_or_404(User, pk=pk)).profile
    context = {'profile': profile_copy, 'yours': False}
    return render(request, 'Profile_detail.html', context)

@login_required
def Excursions(request, pk):
    user_copy = (get_object_or_404(User, pk=pk))
    context = {'user': user_copy}
    return render(request, 'User_excursions.html', context)

@login_required
def My_excursions(request):
    user_copy = request.user
    context = {'user': user_copy}
    return render(request, 'User_excursions.html', context)

@login_required
def New_excursion(request):
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES)
        if form.is_valid():
            excursion = form.save(commit=False)
            excursion.Made_by = request.user
            excursion.Img = request.FILES['Img']
            excursion.save()
            return HttpResponseRedirect(reverse('excursion-detail', args=[excursion.pk]))
    else:
        form = ExcursionForm()
    return render(request, 'New_excursion.html', {'form': form})

@login_required
def Profile_update(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        form.save()
        return HttpResponseRedirect(reverse('my-profile'))
    else:
        form = ProfileForm()
    return render(request, 'Profile_update.html', {'form': form})


