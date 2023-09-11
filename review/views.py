from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.


def get_home_page(request):
    return render(request, 'index.html')


def leave_review(request):

    review_form = ReviewForm()

    return render(
        request,
        "index.html",
        {
            "review_form": review_form

        },
    )
