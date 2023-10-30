from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    Review form set up
    """
    class Meta:
        model = Review
        fields = ('stars', 'body')
