from review.views import leave_review
from django.urls import path


urlpatterns = [
    path('', leave_review, name='home'),
]
