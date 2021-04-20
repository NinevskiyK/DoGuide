from django.shortcuts import render
from search.models import Excursion
from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import ExcursionForm, BookForm
from django.urls import reverse
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required
def Excursion_detail(request, pk):
    excursion_copy = get_object_or_404(Excursion, pk=pk)
    Excursion.create_json(e=excursion_copy)
    user = excursion_copy.Made_by
    can_edit = False
    if user == request.user:
        can_edit = True
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.excursion = excursion_copy
            book.save()
            return HttpResponseRedirect(reverse('excursion-detail', args=[pk])+'?book=1')
        else:
            return HttpResponseRedirect(reverse('excursion-detail', args=[pk])+'?book=0')
    else:
        form = BookForm()
    book = 2
    if 'book' in request.GET:
        if request.GET['book'] == '1':
            book = 1
        else:
            book = 0
    context = {'excursion': excursion_copy, 'user': user, 'can_edit': can_edit, 'form': form, 'book': book}
    return render(request, 'Excursion_detail.html', context)


@login_required
def Excursions(request):
    excursions = Excursion.objects.all()
    return render(request, 'Search.html', {'excursions': excursions})


@login_required
def Excursion_update(request, pk):
    excursion_copy = get_object_or_404(Excursion, pk=pk)
    data = {
        'Place': excursion_copy.Place,
        'Description': excursion_copy.Description,
        'Max_number': excursion_copy.Max_number,
        'Cost': excursion_copy.Cost,
        'Time': excursion_copy.Time,
        'City': excursion_copy.City,
        'Country': excursion_copy.Country,
        'Short_description': excursion_copy.Short_description,
        'Img': excursion_copy.Img
    }
    if excursion_copy.Made_by != request.user:
        return render(request, 'not_your_excursion.html')
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES, instance=excursion_copy)
        form.save()
        return HttpResponseRedirect(reverse('excursion-detail', args=[pk]))
    else:
        form = ExcursionForm(initial=data)
    return render(request, 'Excursion_edit.html', {'form': form})


@login_required
def Excursion_check(request, pk):
    excursion_copy = get_object_or_404(Excursion, pk=pk)
    books = excursion_copy.book_set.order_by('data')
    if excursion_copy.Made_by != request.user:
        return render(request, 'not_your_excursion.html')
    return render(request, 'Excursion_check.html', {'excursion': excursion_copy, 'books': books})


