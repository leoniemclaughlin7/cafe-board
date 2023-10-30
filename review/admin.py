from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Review admin set up, using list display to change
    the look of the review table and list filter so as admin
    can filter the reviews by number of stars and date.
    """
    list_display = ('name', 'stars', 'created_on')
    list_filter = ('stars', 'created_on')
