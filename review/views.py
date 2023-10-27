from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.views import generic, View
from .models import Review

# Create your views here.


def review(request):
    reviews = Review.objects.order_by('-created_on').all()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review_form.instance.name = request.user.username
            review_form.save()
            review_form = ReviewForm()
    else:
        review_form = ReviewForm()

    return render(request, 'index.html', {'review_form': review_form,
                                          'reviews': reviews})


def menu(request):
    return render(request, 'menu.html')


def contact(request):
    return render(request, 'contact.html')
