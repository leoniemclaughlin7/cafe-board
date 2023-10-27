from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars', 'created_on')
    list_filter = ('stars', 'created_on')
