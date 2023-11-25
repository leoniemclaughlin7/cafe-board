from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.views import generic, View
from .models import Review
from django.contrib import messages


def review(request):
    """
    View to display review and if post method then leave a review.
    """
    reviews = Review.objects.order_by('-created_on').all()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review_form.instance.name = request.user.username
            review_form.save()
            review_form = ReviewForm()
            messages.add_message(request, messages.SUCCESS,
                                'Your review has been successfully posted!')
    else:
        review_form = ReviewForm()

    return render(request, 'index.html', {'review_form': review_form,
                                          'reviews': reviews})


def menu(request):
    """
    View to render the menu.html page.
    """
    return render(request, 'menu.html')


def games(request):
    """
    View to render the menu.html page.
    """
    return render(request, 'games.html')
